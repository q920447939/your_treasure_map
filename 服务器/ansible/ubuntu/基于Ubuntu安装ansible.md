# 基于Ubuntu安装ansible

注: 按需设置代理

系统代理:`/etc/profile`

```
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

其余代理见:[设置 ubuntu 中各种应用的代理 - 阅微堂](https://zhiqiang.org/it/proxy-of-application-in-ubuntu.html)

APT代理查看(通过`ios`安装方式可以看到):

```
cd /etc/apt/apt.conf.d
使用 ll 命令,会看到 proxy 字样文件,可以通过 cat 命令查看
```





## 主机端安装ansible

1. `sudo apt-get install ansible`
2. 验证`ansible --version `



由于当前主机端也没有很多软件,比如`docker`,那么我们可以基于`ansilbe playbook`安装必要的软件,此处以安装`docker`为例

## 被控端安装软件

此处为 被控端 = 主机端

准备好 `ansible.cfg`和 `hosts` 以及 docker 安装包 和play book (将此文件夹全部下载下来)

### 修改目标主机

修改`hosts`文件

比如我这里修改成:

```
[all]
127.0.0.1 ansible_ssh_user=root ansible_ssh_pass=youPassword  ansible_port=22

```

### 被控端安装sshpass

```
sudo apt install sshpass

#如果不安装,会提示  {"msg": "to use the 'ssh' connection type with passwords or pkcs11_provider, you must install the sshpass program"}
```



### 运行脚本

```
ansible-playbook -i hosts docker/install_docker.yml -e "http_proxy=http://192.168.229.1:17893"  #如果服务器没有网络,需要设置代理
```

