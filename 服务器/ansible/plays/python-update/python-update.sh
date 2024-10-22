#!/bin/bash
set -e

# 指定要安装的Python版本
PYTHON_VERSION="3.10.12"

echo "=== 安装编译依赖 ==="
# 安装编译依赖
sudo yum install -y gcc gcc-c++ zlib zlib-devel readline-devel

echo "=== 下载 Python 源码包 ==="
# 下载Python源码包（从华为镜像源下载）
#wget https://mirrors.huaweicloud.com/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz

echo "=== 解压 Python 源码包 ==="
# 解压Python源码包
tar xvf Python-$PYTHON_VERSION.tar.xz

echo "=== 进入 Python 源码目录 ==="
# 进入Python源码目录
cd Python-$PYTHON_VERSION

echo "=== 配置并编译 Python ==="
# 编译并安装Python
./configure
make && sudo make install

echo "=== 更改默认 python 链接 ==="
# 更改默认python链接
sudo mv /usr/bin/python /usr/bin/python.bak
sudo ln -s /usr/local/bin/python3 /usr/bin/python

echo "=== 配置 yum 脚本和 urlgrabber-ext-down 脚本 ==="
# 配置yum脚本和urlgrabber-ext-down脚本
sudo sed -i "s|#!/usr/bin/python|#!/usr/bin/python2.7|" /usr/bin/yum
sudo sed -i "s|#!/usr/bin/python|#!/usr/bin/python2.7|" /usr/libexec/urlgrabber-ext-down

echo "=== 升级 Python 3 完成！ ==="
