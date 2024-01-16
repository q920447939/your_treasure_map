## CentOS7安装Docker

### 1.卸载Docker

```
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine \
                  docker-ce
                  

```

### 2.安装docker

```
yum install -y yum-utils \
           device-mapper-persistent-data \
           lvm2 --skip-broken
```

### 3.更新本地镜像

```
# 设置docker镜像源
yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    
sed -i 's/download.docker.com/mirrors.aliyun.com\/docker-ce/g' /etc/yum.repos.d/docker-ce.repo

yum makecache fast
```

### 4.安装docker

```
yum install -y docker-ce
```

### 5.启动Docker

```
systemctl start docker  # 启动docker服务
```

### 6.查看docker是否启动成功

```
docker -v
```

