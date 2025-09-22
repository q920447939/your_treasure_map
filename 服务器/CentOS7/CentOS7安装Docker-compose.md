## CentOS7安装Docker-compose

### 1.从github下载docker-compose文件，下载地址

```
https://github.com/docker/compose/releases/download/v2.24.0/docker-compose-linux-x86_64
```



### 2.上传到服务器



### 3.改名并放到`/usr/local/bin/`路径下

```bash
mv docker-compose-linux-x86_64 docker-compose
mv docker-compose /usr/local/bin/
cd /usr/local/bin/
chmod +x /usr/local/bin/docker-compose

```

### 4.验证版本

```bash
docker-compose --version
```

