## 麒麟系统安装Docker

PS：本次系统架构为 `x86_64`，采用离线版安装方式

查看系统架构

```
# uname -p
x86_64
```



### 1.下载安装docker-ce

官网下载地址：https://download.docker.com/linux/static/stable/x86_64/docker-25.0.0.tgz

### 2.上传到服务器



### 3.配置添加 systemd

```
解压
tar -zxvf docker-20.10.7.tgz
移动解压出来的二进制文件到 /usr/bin 目录中
mv docker/* /usr/bin/
```



### 4.编辑docker的系统服务文件

```cobol
vi /usr/lib/systemd/system/docker.service

#添加下面的内容
      
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
[Service]
Type=notify
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
[Install]
WantedBy=multi-user.target
```

### 5.重新加载和重启docker

```undefined
systemctl daemon-reload
systemctl restart docker

#查看docker详细信息
docker info
```