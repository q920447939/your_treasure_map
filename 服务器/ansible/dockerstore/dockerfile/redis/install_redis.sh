rm -rf /opt/dockerstore/redis
mkdir -p /opt/dockerstore/redis/datadir
mkdir -p /opt/dockerstore/redis/log
mkdir -p /opt/dockerstore/redis/conf/
mkdir -p /opt/dockerstore/redis/docker-compose


docker-compose up -d


firewall-cmd --permanent --zone=public --add-port=61379/tcp --permanent
firewall-cmd --reload