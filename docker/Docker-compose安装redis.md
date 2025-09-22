## Docker-compose安装redis

### 1.创建宿主机挂载目录和docker-compose文件

```
rm -rf /opt/dockerstore/redis
mkdir -p /opt/dockerstore/redis/datadir
mkdir -p /opt/dockerstore/redis/log
mkdir -p /opt/dockerstore/redis/conf/
mkdir -p /opt/dockerstore/redis/docker-compose
```



### 2.编辑配置文件

```
vi /opt/dockerstore/redis/conf/redis.conf
#内容如下：

bind 0.0.0.0
 
protected-mode yes
 
port 6379
 
tcp-backlog 511
 
timeout 0
 
tcp-keepalive 300
 
daemonize yes

pidfile /var/run/redis/redis.pid
 
loglevel notice
 
 
databases 16

```



### 3.编辑**docker-compose.yaml** 文件

```
version: '3'
services:
  redis:
    image: 'redis:6.0'
    restart: always
    container_name: docker_redis
    volumes:
      - /opt/dockerstore/redis/datadir:/data
      - /opt/dockerstore/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - /opt/dockerstore/redis/log:/logs
    ports:
      - '61379:6379'
    command:
      --requirepass "你的密码"
```



### 3.运行docker-compose

```bash
docker-compose up -d


 
 
 #docker ps 可以看到redis容器则证明成功
[root@localhost docker-compose]# docker ps  | grep redis
3cebbd7fd9aa   redis:6.0      "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   0.0.0.0:61379->6379/tcp, :::61379->6379/tcp     docker_redis
```

### 4.连接测试

```bash
telnet 127.0.0.1  61379

```

