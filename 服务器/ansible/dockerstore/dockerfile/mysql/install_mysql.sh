rm -rf /opt/dockerstore/mysql
mkdir -p    /opt/dockerstore/mysql/data
mkdir -p    /opt/dockerstore/mysql/conf
mkdir -p    /opt/dockerstore/mysql/log
mkdir -p    /opt/dockerstore/mysql/mysql-files


cp -r -f ./my.cnf /opt/dockerstore/mysql/conf/my.cnf

docker-compose up -d

firewall-cmd --permanent --zone=public --add-port=63306/tcp --permanent
firewall-cmd --reload