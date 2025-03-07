## Docker-compose安装mongodb

### 1.创建宿主机挂载目录和docker-compose文件

```
#mongo数据目录
mkdir -p /opt/dockerstore/mongo/data
#mongo日志目录
mkdir -p /opt/dockerstore/mongo/logs
#mongo docker-compose文件目录
mkdir -p /opt/docker-compose/mongodb
```



### 2.新建docker-compose.yml

```
version: '3.1'
services:
  mongodb:
    container_name: mongodb
    image: mongo:latest
    ports:
      - "67017:27017"
    restart: always
    command: --wiredTigerCacheSizeGB 4 --auth # 限制内存大小, 需要认证
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: "75b597fdeb43d8c8a1626"
    volumes:
      - "/opt/dockerstore/mongo/data:/data/db"
      - "/opt/dockerstore/mongo/logs:/var/log/mongodb"
      - "/usr/share/zoneinfo/Asia/Shanghai:/etc/localtime"

```



### 3.运行docker-compose

```bash
docker-compose up -d



提示如下：
[+] Running 10/10
 ✔ mongodb 9 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                                                 398.1s 
   ✔ 57c139bbda7e Pull complete                                                                                                                                                                         38.2s 
   ✔ 5ded68502327 Pull complete                                                                                                                                                                         10.6s 
   ✔ 25b2700cb3f2 Pull complete                                                                                                                                                                         30.6s 
   ✔ 40c78628995a Pull complete                                                                                                                                                                         19.2s 
   ✔ 81f3a3fe93a2 Pull complete                                                                                                                                                                        373.6s 
   ✔ 4fbdadf2860f Pull complete                                                                                                                                                                         42.2s 
   ✔ 8050fbbed2fd Pull complete                                                                                                                                                                         44.1s 
   ✔ 6d012f43eccc Pull complete                                                                                                                                                                        261.1s 
   ✔ 80634cd52614 Pull complete                                                                                                                                                                         51.1s 
[+] Running 2/2
 ✔ Network mongodb_default  Created                                                                                                                                                                      0.2s 
 ✔ Container mongodb        Started                                                                                                                                                                      1.4s 
 
 
 #docker ps 可以看到mongodb镜像则证明成功
 [root@localhost mongodb]# docker ps 
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS          PORTS                                           NAMES
53aa4f21d16a   mongo:latest   "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes    0.0.0.0:67017->27017/tcp, :::67017->27017/tcp   mongodb
```

### 4.连接和认证

```bash
docker exec -it mongodb /bin/bash
mongosh

test> use admin
switched to db admin
admin> db.auth("admin","75b597fdeb43d8c8a1626")
{ ok: 1 }

#提示 { ok: 1 }  则证明认证成功，后续可以使用navicat 和Robo 3T 工具 进行可视化查看

```

