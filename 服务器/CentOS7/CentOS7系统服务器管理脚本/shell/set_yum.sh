#!/bin/bash
# 检查 CentOS-Base.repo 文件是否存在
if [ -f /etc/yum.repos.d/CentOS-Base.repo ]; then
    # 备份原有的 yum 源配置文件
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
fi

# 编辑 CentOS-Base.repo 文件,替换为中国科技大学镜像源
echo '' > /etc/yum.repos.d/CentOS-Base.repo

cat << EOF > /etc/yum.repos.d/CentOS-Base.repo
[base]
name=CentOS-\$releasever - Base - USTC
baseurl=https://mirrors.ustc.edu.cn/centos/\$releasever/os/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-\$releasever - Updates - USTC
baseurl=https://mirrors.ustc.edu.cn/centos/\$releasever/updates/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-\$releasever - Extras - USTC
baseurl=https://mirrors.ustc.edu.cn/centos/\$releasever/extras/\$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF

# 生成缓存
yum makecache

# 更新软件包缓存
yum update
