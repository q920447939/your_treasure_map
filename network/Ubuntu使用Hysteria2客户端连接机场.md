# Ubuntu使用Hysteria2客户端连接机场

目前机场提供的Hysteria2订阅链接

但是一般都是提供了GUI客户端

如果希望在Ubuntu上面使用代理,那么GUI客户端无法使用

所以需要一个无GUI的客户端,配置后连接机场



## 原理

一些基于 Hysteria2协议实现的客户端,本质上只是用了某个内核,而一般内核其实是不需要GUI的

所以我们只需要知道内核怎么配置也可以

以`clash-verge-re`为例,他的内核是基于 [mihomo](https://github.com/MetaCubeX/mihomo),但是这个内核似乎配置有点麻烦



## Hysteria2原生客户端

我们使用`Hysteria2`原生客户端 [hysteria](https://github.com/apernet/hysteria) 在`Ubuntu`上进行操作

该`Ubuntu`系统版本 : `24-LTS`

```
root@ucloud:/home/hysteria# uname -a
Linux ucloud 6.8.0-31-generic #31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

1. 创建Hysteria2用户

   ```
   useradd -m hysteria
   cd /home/hysteria
   ```

2. 下载`hysteria` 程序

   ```
   #如果访问不到github,可以下载后,再传到该服务器上
   wget https://github.com/apernet/hysteria/releases/download/app%2Fv2.6.1/hysteria-linux-amd64
   chmod +x hysteria-linux-amd64
   ```

3. 编辑配置文件

   该配置文件的信息,可以参考`class-verge-re`(其他同理),对应的配置文件

   ```
   vi config.yml
   
   #配置文件
   server: domain:443 #填入机场域名
   
   auth: 填入认证信息
   
   tls:
     insecure: true
   
   bandwidth:
     up: 20 mbps
     down: 100 mbps
   
   socks5:
     listen: 127.0.0.1:1080
   
   http:
     listen: 127.0.0.1:7890
   ```

   

4. 编辑启动脚本

   ```
   vi hysteria-start.sh
   
   nohup /home/hysteria/hysteria-linux-amd64  -c /home/hysteria/config.yml -l debug >/dev/null 2>&1 &
   
   chmod +x hysteria-start.sh
   ```

5. 启动

   ```
   ./hysteria-start.sh
   ```

   可以先用前台启动查看配置信息是否有问题,没问题再使用该命令后台启动

6. 检查启动状态

   ```
   root@ucloud:/home/hysteria# ss -tunlp | grep 7890
   tcp   LISTEN 0      4096       127.0.0.1:7890       0.0.0.0:*    users:(("hysteria-linux-",pid=99629,fd=6))
   
   
   ```

   如果能够找到,说明启动正常

7. 检查代理状态

   ```
   root@ucloud:/home/hysteria# wget -e "https_proxy=http://127.0.0.1:7890" https://www.google.com
   --2025-03-26 16:29:33--  https://www.google.com/
   Connecting to 127.0.0.1:7890... connected.
   Proxy request sent, awaiting response... 200 OK
   Length: unspecified [text/html]
   Saving to: 'index.html'
   
   index.html                                         [ <=>                                                                                               ]  17.37K  --.-KB/s    in 0.001s
   
   2025-03-26 16:29:33 (18.6 MB/s) - 'index.html' saved [17788]
   
   ```

   

8. 其他代理设置

   [设置 ubuntu 中各种应用的代理 - 阅微堂](https://zhiqiang.org/it/proxy-of-application-in-ubuntu.html)

   [Ubuntu下的代理配置 - Torch-Fan](https://www.torch-fan.site/2022/07/20/Ubuntu下的代理配置/)

   

