## CentOS7安装Rust-desk

### 1.参考《CentOS7安装Docker》和《CentOS7安装Docker-compose》文章安装docker和Docker-compose

### 2.在服务器上创建一个ruskdesk 用户,并创建docker挂载文件夹

```bash
useradd ruskdesk 
chmod -R 755 /home/rustdesk/
mkdir -p /home/rustdesk/data
```



### 3.在`rustdesk`建立`docker-compose.yml`文件，文件内容如下（注意`command`节点填写自己的服务器域名或者ip）:

```yaml

version: '3'
networks:
  rustdesk-net:
    external: false
services:
  hbbs:
    container_name: hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:latest
    
    command: hbbs -r 【your ip】:21117
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped
  hbbr:
    container_name: hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```



### 4.使用`docker compose` 启动`docker-compose.yml`配置

```bash
docker-compose up -d

```

### 5.查看docker容器是否启动正常

```bash
dokcer ps
```

### 6.把服务器的防火墙打开相应的端口（开放完后，可以使用`telnet ip port 测试是否端口可以连通`）：

```
- TCP: 21115-21119
- UDP: 21116
```



### 7.下载`rust desk`客户端，下载地址：

```
https://github.com/rustdesk/rustdesk/releases/tag/1.2.3
windows下载地址：https://github.com/rustdesk/rustdesk/releases/download/1.2.3/rustdesk-1.2.3-x86_64.exe
```



### 8.客户端配置：

```
1.查看加密连接的公钥,把里面的内容复制
cat /home/rustdesk/data/id_ed25519.pub   
2.把上一步下载下来的 rustdesk-1.2.3-x86_64.exe 文件，名字修改， 修改规则如下：
把rustdesk.exe 修改为 rustdesk-host=<host-ip-or-name>,key=<public-key-string>.exe, 例如： rustdesk-host=192.168.1.137,key=xfdsfsd32=32.exe,最终修改的效果应该为  rustdesk-host=192.168.11.222,key=ATBN5HyedBgCC+xFDzB3H4eyrCY607CahASqodztJx4=.exe
```



### 9.打开客户端软件，查看`设置-关于`，如果Key和Host都对了，那么就设置对了。



### 10.另外一台机器用同样的设置，然后就可以通过`ID`和`密码`进行访问了



