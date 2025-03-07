# CentOS7 一键安装mysql8.0

## 1.下载mysql8.0 tar gz包

## 2.MySQL脚本

注意 可根据自定义需求修改data_dir_path 

data_dir_path  是数据保存目录 ,home_data_path是mysql 安装目录 ) 。需要建立download文件夹 。以及修改mysql_package_name

PS : 正确的安装前提是拥有这些目录和文件

`/mnt/xxx/ ` 目录

`/home/xxx/download` 目录

`mysql-8.0.23-el7-x86_64.tar.gz` 需要放在`/home/xxx/download `

```shell
#! /bin/bash
data_dir_path='/mnt/xxx/'
home_data_path='/home/xxx'
download_path=''$home_data_path'/download'
mysql_base_path=''$home_data_path'/mysql8/'
mysql_data_path=''$data_dir_path'/mysql_data/'
mysql_package_name="mysql-8.0.23-el7-x86_64.tar.gz"
mysql_package_name1=${mysql_package_name%%.tar.gz}
SHELL_FOLDER=$(cd "$(dirname "$0")" || exit;pwd)

rm -rf $mysql_base_path
rm -rf mysql_data_path
mkdir mysql_data_path
rm -rf /etc/init.d/mysql
mysql_profile_line_start=`grep -n "#mysql start" /etc/profile | cut -d ":" -f 1`
if [ $mysql_profile_line_start ]; then
  mysql_profile_line_end=$((n=$mysql_profile_line_start+5))
  sed -i ''$mysql_profile_line_start','$mysql_profile_line_end'd' /etc/profile
fi
echo " 删除mysql安装目录（${mysql_base_path}）完成，删除mysql数据目录（${mysql_data_path}）完成,删除上次mysql上次安装文件完成"


if [ ! -f   $download_path/$mysql_package_name ]; then
  echo "${download_path}/${mysql_package_name} 文件不存在！"
  exit
fi
echo "开始解压mysql tar包"
tar -xf $download_path/$mysql_package_name || exit
mv ./$mysql_package_name1  $mysql_base_path
groupadd mysql
useradd -r -g mysql mysql

cd $mysql_data_path || exit
chown -R mysql:mysql ./

cd $mysql_base_path || exit
chown -R mysql:mysql ./

bin/mysqld  --initialize  --user=mysql  --basedir=$mysql_base_path  --datadir=$mysql_data_path --default-authentication-plugin=mysql_native_password
cd /etc/ || exit

if [ -f  /etc/my.cnf ] ;then
  echo '存在。。。。'
  cp /etc/my.cnf /etc/my.cnf.bak
  rm -rf /etc/my.cnf
fi

cp "$SHELL_FOLDER"/my.cnf /etc/my.cnf
chmod 755 /etc/my.cnf
chown -R mysql:mysql /var/lib/mysql

echo "#mysql start" >> /etc/profile
echo "export  MYSQL_HOME" >> /etc/profile
echo "MYSQL_HOME="$mysql_base_path"" >> /etc/profile
echo "export  PATH=$PATH:$MYSQL_HOME/lib:$MYSQL_HOME/bin " >> /etc/profile
echo "#mysql end" >> /etc/profile

source /etc/profile
cp $mysql_base_path/support-files/mysql.server   /etc/init.d/mysql
chmod +x  /etc/init.d/mysql
chkconfig  --add mysql
service mysql start
echo "mysql安装完成，服务已启动"

```



## 3.授权脚本 

先给脚本授权,最好使用root用户操作(授权命令  `chmod +x mysql脚本名字.sh`)



## 4.将下方脚本命名成 `my.cnf`

```shell
[mysqld]
socket=/var/lib/mysql/mysql.sock
skip_ssl
port=3306
basedir=需要修改成mysql的安装目录 如果没改的话是/home/xxx/mysql8
datadir=需要修改成mysql的数据目录 如果没改的话是 /mnt/xxx/mysql_data
max_connections=200
max_connect_errors=10
character-set-server=utf8mb4
default_authentication_plugin=mysql_native_password
skip-name-resolve
skip-external-locking
default-time_zone = 'system'
local-infile=1
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION

default-storage-engine=INNODB
innodb-file-per-table = 1
innodb_open_files = 50
innodb_buffer_pool_size = 1024M
innodb_log_file_size = 64M
innodb_log_buffer_size = 32M
innodb_write_io_threads = 16
innodb_read_io_threads = 16
innodb_thread_concurrency = 0
innodb_purge_threads = 1
innodb_flush_log_at_trx_commit = 2
innodb_log_files_in_group = 3
innodb_max_dirty_pages_pct = 90
innodb_lock_wait_timeout = 120
bulk_insert_buffer_size = 32M

open_files_limit = 65535
tmp_table_size = 32M
key_buffer_size = 128M
max_allowed_packet = 16M
table_open_cache = 16K
table_definition_cache = 16K
net_buffer_length = 128K
sort_buffer_size = 64M
read_buffer_size = 64M
read_rnd_buffer_size = 64M
join_buffer_size = 64M
thread_cache_size = 64
binlog_cache_size = 1M

long_query_time = 6
back_log = 1000
wait-timeout = 28800
interactive-timeout = 28800

transaction_isolation = REPEATABLE-READ

performance_schema = 0
explicit_defaults_for_timestamp

[mysql]
default-character-set=utf8mb4
[client]
port=3306
default-character-set=utf8mb4
socket=/var/lib/mysql/mysql.sock
```



## 5.运行 Mysql脚本

正常运行结果应该是会显示`mysql安装完成，服务已启动`,以及页面上会打印mysql 初始密码

## 6.登录

6.1 先查看mysql 运行状态,输入命令 `service mysql status`,如果不是running,那么需要看下配置文件没有修改安装目录和存储目录

6.2使用命令`mysql -uroot -p` ,输入密码进行登录

## 7.修改密码和允许远程登录等

7.1 前提是已经正常进入mysql 控制台操作页面;

7.2 允许远程登录

​	7.2.1 输出命令

`use mysql; `

`update user set host = '%' where user = 'root'; 
update user set authentication_string='' where  user = 'root';
flush privileges;
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123';`



