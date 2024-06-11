## CentOS7-ansible自动化安装服务器初始化脚本

### 前言

本文主要是采用`ansible`软件在`CentOS7`服务器上自动化安装一些脚本

`ansible`是什么？

​	`ansible`利用`python`和`ssh`工具，可以批量完成服务器的一些安装、运行脚本、定时任务等工作



本文基于的场景是小规模、快速交互、上手难度等多方面进行技术选型。

下面开始做一些对比

| 软件                        | 上手难度 | 维护程度 | 扩展性 | 被控端是否需要安装软件 |
| --------------------------- | -------- | -------- | ------ | ---------------------- |
| ansible                     | 简单     | 简单     | 简单   | 无                     |
| docker-里面虚拟化一个CentOS | 简单     | 简单     | 差     | 需要安装docker         |
| Chef，Puppet或Salt          | 未测试   | 未测试   | 未测试 | 未测试                 |



简单来说，目前希望实现 小规模、快速交互、上手难度低等多种场景的自动化部署需求，只有`ansible`和 `docker-里面虚拟化一个CentOS  `这两种方式较为合适，不过没有选用`docker-里面虚拟化一个CentOS  `的方式有以下几点：

1. 迁移的时候镜像会很大
2. 打包好的镜像如果需要调整里面的一些配置、还是需要编写一部分的`bash`代码
3. 把所有的软件(比如把`mysql、redis`都放到`docker`里面去，总担心会有崩溃的问题)。并且像数据库不太建议安装到`docker`

最终还是选用了 `ansible` 作为自动化部署工具



### 实现原理

![image-20240611103541738](F:\liming\md\your_treasure_map\服务器\ansible\md\img\原理图)

控制端服务器通过SSH 将控制端上的命令发送到被控端服务器执行 



### 安装

本次 控制端服务器和被控端服务器 均为`CentOS7`



#### 下载

如果服务器没网，先设置`yum`的代理

```yaml
#设置代理
vi /etc/yum.conf

#在最后添加你的代理
proxy=http://192.168.230.1:7892

```



1. ##### 安装`ansible`

```bash
yum -y install epel-release    //更新本地安装库
# yum list all *ansible*   //查看相应的版本
# yum info ansible         //查看ansible的信息
yum install ansible      //开始安装
```

2. 建立` /tmp/ansible` 文件夹


```bash
mkdir -p   /tmp/ansible
```

3. 在`ansible`文件夹下建立如下几个文件夹、文件

   ```bash
   [root@localhost ansible]# ll
   total 12
   -rw-r--r--. 1 root root  37 Jun  6 10:09 ansible.cfg
   drwxr-xr-x. 4 root root  65 Jun  7 06:04 deploy
   drwxr-xr-x. 3 root root  24 Jun  6 10:19 dockerstore
   -rw-r--r--. 1 root root  94 Jun  7 12:22 hosts
   -rw-r--r--. 1 root root 261 Jun  7 11:58 playbook.yml
   drwxr-xr-x. 9 root root 109 Jun  7 11:57 plays
   drwxr-xr-x. 4 root root  88 Jun  7 06:06 script
   
   ```

   其中

   ​	`ansible.cfg`是全局配置文件

   ​	`hosts`  填写被控端的连接信息

   ​	`playbook.yml` 是具体的执行脚本配置



### 使用

鉴于我 已经把 `ansible` 写了一些，修改好`hosts`文件后，拿配置运行即可 
1. 设置被控端连接信息
    ```bash
    vi /tmp/ansible/hosts
    
    [all]
    192.168.230.232 ansible_ssh_user=root ansible_ssh_pass=youPassword  ansible_port=22
        
    ```

2. 设置时区、DNS、禁用selinux、yum 默认安装常用命令（必要操作）

   ```bash
   cd /tmp/ansible && ansible-playbook -i hosts playbook.yml
   ```
   
3. 安装docker、docker 安装mysql、redis（按需）

   ```bash
   #如果需要设置docker代理，那么先编辑 playbook-docker-proxy.yml文件,将里面的 proxy_url 修改成你的代理IP
   vi  /tmp/ansible/plays/docker/playbook-docker-proxy.yml
   
   
   #需要代理版本
   cd /tmp/ansible &&  ansible-playbook -i hosts plays/docker/playbook-docker-proxy.yml      plays/docker/playbook-mysql.yml plays/docker/playbook-redis.yml
   	
   #不需要代理版本
   
   cd /tmp/ansible &&  ansible-playbook -i hosts   plays/docker/playbook-mysql.yml plays/docker/playbook-redis.yml
   
   #默认mysql 端口 63306 ，账号/密码 root/blk@2024~NIUBI!mysql%mmm
   #挂载路径如下：
         # 挂载数据目录
          - /opt/dockerstore/mysql/data:/var/lib/mysql
          - /opt/dockerstore/mysql/conf/my.cnf:/etc/mysql/my.cnf
          - /opt/dockerstore/mysql/log:/var/log/mysql
          - /opt/dockerstore/mysql/mysql-files:/var/lib/mysql-files
   
   #默认redis 端口 61379 ，密码 blk@2024~NIUBI!redis%h
   #挂载路径如下：
         - /opt/dockerstore/redis/datadir:/data
         - /opt/dockerstore/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf
         - /opt/dockerstore/redis/log:/logs
   
   ```
   
4. 安装nginx(1.2.x)（按需）

   ```bash
   cd /tmp/ansible &&  ansible-playbook -i hosts   plays/nginx/playbook-nginx.yml  plays/nginx/playbook-nginx-conf.yml
   
   #默认开放 80、443端口 ，443端口生成的ssl证书是服务器生成的，会提示不安全
   #html文件夹默认放在 /var/www/localhost/public
   #配置文件默认放在 /etc/nginx/
   #反向代理放在 /etc/nginx/sites-available/localhost.conf
   #日志文件 
   	# access_log /var/log/nginx/access.log 
   	# error_log  /var/log/nginx/error.log 
   ```

5. 安装java(jdk21)（按需）

   ```bash
   cd /tmp/ansible &&  ansible-playbook -i hosts   plays/jdk/jdk_install_offline.yml
   ```



### 注

如果后续在使用过程中提示脚本 '\r' 、‘\n’ 字符问题，可以使用命令  `sed -i 's/\r$//' 填写有问题的脚本`



### 参考

[ansible使用教程（4W字长文，保姆级别教程，建议收藏）_51CTO博客_ansible 教程](https://blog.51cto.com/u_13540373/4850247#四、ansible使用入门)

[ansible入门快速上手使用教程_ansible使用教程-CSDN博客](https://blog.csdn.net/qq_33521184/article/details/122321996)

[1. ansible-playbook 变量定义与引用 - 温柔易淡 - 博客园 (cnblogs.com)](https://www.cnblogs.com/liaojiafa/p/9353760.html)