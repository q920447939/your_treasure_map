#mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base1.repo
mv /opt/ansible/deploy/yum/epel-7.repo ./CentOS-Base.repo
cp ./CentOS-Base.repo  /etc/yum.repos.d/

yum clean all
yum makecache
