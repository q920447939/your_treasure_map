# 修复`ubuntu`系统 ssh无法启动问题

## 背景

- 系统有默认安装 ssh，但是无法使用

- 通过查看进程也没有 ssh （`sshd`）

  ```bash
  #本机连接22 拒绝连接
  root@musk-computer:/home/musk# telnet 127.0.0.1 22
  Trying 127.0.0.1...
  telnet: Unable to connect to remote host: 连接被拒绝
  
  #ssh 只有一个 ssh-agent
  root@musk-computer:/home/musk# ps -ef | grep ssh
  musk        4052    3669  0 19:36 ?        00:00:00 /usr/libexec/gcr-ssh-agent --base-dir /run/user/1000/gcr
  root       80639   59979  0 22:00 pts/2    00:00:00 grep --color=auto ssh
  
  # 防火墙已经关闭
  root@musk-computer:/home/musk# ufw status
  ```

  

- 通过`apt`安装也显示错误

  ```bash
  musk@musk-computer:~$ sudo apt install openssh-server
  正在读取软件包列表... 完成
  正在分析软件包的依赖关系树... 完成
  正在读取状态信息... 完成                 
  有一些软件包无法被安装。如果您用的是 unstable 发行版，这也许是
  因为系统无法达到您要求的状态造成的。该版本中可能会有一些您需要的软件
  包尚未被创建或是它们已被从新到(Incoming)目录移出。
  下列信息可能会对解决问题有所帮助：
  
  下列软件包有未满足的依赖关系：
   apt : 依赖: gpgv
         依赖: libapt-pkg6.0t64 (>= 2.8.3) 但是它将不会被安装
   dpkg : 预依赖: libmd0 (>= 0.0.0) 但无法安装它
          预依赖: zlib1g (>= 1:1.1.4) 但无法安装它
   e2fsprogs : 预依赖: libcom-err2 (>= 1.43.9) 但无法安装它
               预依赖: libss2 (>= 1.38) 但是它将不会被安装
   init : 预依赖: systemd-sysv
   libgssapi-krb5-2 : 依赖: libcom-err2 (>= 1.43.9) 但无法安装它
   libkrb5-3 : 依赖: libcom-err2 (>= 1.43.9) 但无法安装它
   openssh-client:i386 : 依赖: libselinux1:i386 (>= 3.1~) 但无法安装它
                         推荐: xauth:i386
   openssh-server : 依赖: libcom-err2 (>= 1.43.9) 但无法安装它
                    依赖: zlib1g (>= 1:1.1.4) 但无法安装它
                    推荐: default-logind 或
                            logind 或
                            libpam-systemd 但是它将不会被安装
                    推荐: xauth
                    推荐: ssh-import-id 但是它将不会被安装
   python3 : 预依赖: python3-minimal (= 3.12.3-0ubuntu2) 但是它将不会被安装
             依赖: python3.12 (>= 3.12.3-0~) 但是它将不会被安装
   util-linux : 预依赖: libudev1 (>= 183) 但无法安装它
                预依赖: zlib1g (>= 1:1.1.4) 但无法安装它
  E: 错误，pkgProblemResolver::Resolve 发生故障，这可能是有软件包被要求保持现状的缘故。
  
  ```

## 解决方案-卸载`ssh`再重新安装`ssh`

#### 卸载

```
# 卸载SSH服务器
sudo apt remove openssh-server
# 如果要同时删除配置文件
sudo apt purge openssh-server
# 清理依赖
sudo apt autoremove

# 卸载所有SSH相关包
sudo apt remove --purge openssh-server openssh-client ssh
# 清理配置
sudo apt autoremove
sudo apt autoclean

```



#### 修复软件源（可选）

```
sudo nano /etc/apt/sources.list

#填入如下配置：
deb http://archive.ubuntu.com/ubuntu jammy main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu jammy-security main restricted universe multiverse

```



#### 安装

```
# 更新包列表
sudo apt update

# 安装OpenSSH服务器
sudo apt install openssh-server

# 安装SSH客户端（通常会自动安装）
sudo apt install openssh-client

```



### 管理SSH服务

```
# 启动SSH服务
sudo systemctl start ssh

# 设置开机自启
sudo systemctl enable ssh

# 检查SSH服务状态
sudo systemctl status ssh

# 重启SSH服务
sudo systemctl restart ssh

# 停止SSH服务
sudo systemctl stop ssh

```

### 检查SSH是否正常工作

```
# 使用ss命令
sudo ss -tlnp | grep 22

# 测试本地连接
ssh localhost

```



## 后记

1. 如果使用的是`root`用户，查看网上的教程，默认是没有开放`root`用户的`ssh`
2. 如果有防火墙，注意防火墙是否开放了指定端口，建议先用本机`telnet`进行测试