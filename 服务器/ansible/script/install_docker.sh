# 安装 Docker 的前置依赖
yum remove docker \  
 docker-client \
 docker-client-latest  \ 
 docker-common \ 
 docker-latest \ 
 docker-latest-logrotate \
 docker-logrotate \ 
 docker-selinux  \ 
 docker-engine-selinux \ 
 docker-engine \
 docker-ce \ 
 -y

yum install -y yum-utils \ 
 device-mapper-persistent-data \ 
 lvm2 --skip-broken

# 添加阿里云的 Docker 源
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 修改 Docker 源地址
sed -i 's#download.docker.com#mirrors.aliyun.com/docker-ce#' /etc/yum.repos.d/docker-ce.repo

# 更新本地包缓存
yum makecache fast

# 安装 Docker CE
yum install -y docker-ce

# 启动 Docker 服务
systemctl start docker

# 检查 Docker 版本
docker -v

# 设置 Docker 服务在系统启动时自动启动
systemctl enable docker

# 检查 Docker 服务是否已经设置为自动启动
systemctl is-enabled docker
