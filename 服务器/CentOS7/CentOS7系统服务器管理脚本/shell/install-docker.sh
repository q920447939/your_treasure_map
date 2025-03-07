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

yum install -y yum-utils \           device-mapper-persistent-data \           lvm2 --skip-broken


yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    
sed -i 's/download.docker.com/mirrors.aliyun.com\/docker-ce/g' /etc/yum.repos.d/docker-ce.repo

yum makecache fast

yum install -y docker-ce

systemctl start docker 


echo "==========【docker版本号】============"
docker -v


systemctl enable docker
echo "==========【docker启动成功】============"

systemctl is-enabled docker
echo "==========【docker加入开机自启完成】============"

echo "==========【docker安装完成】============"