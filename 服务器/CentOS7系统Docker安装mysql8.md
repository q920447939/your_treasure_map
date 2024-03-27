## CentOS7系统Docker安装mysql8

### 1.创建挂载目录

```sh
rm -rf /opt/dockerstore/mysql
mkdir -p    /opt/dockerstore/mysql/data
mkdir -p    /opt/dockerstore/mysql/conf
mkdir -p    /opt/dockerstore/mysql/log
mkdir -p    /opt/dockerstore/mysql/mysql-files


```

### 2.编写mysql配置文件

```sh
vi /opt/dockerstore/mysql/conf/my.cnf

#内容如下


###### [mysql]配置模块 ######
[mysql]
# 设置MySQL客户端默认字符集
default-character-set=utf8mb4

###### [mysqld]配置模块 ######
[mysqld]
skip-name-resolve
# sql_mode 是 MySQL 的一个系统变量，它控制了 MySQL 在执行 SQL 语句时的行为。
# STRICT_TRANS_TABLES：启用严格模式，当插入或更新数据时，MySQL 将拒绝任何不符合数据类型的数据。
# NO_ZERO_IN_DATE：当日期或日期时间字段中的值为 "0000-00-00" 时，MySQL 将抛出警告或错误。
# NO_ZERO_DATE：当日期或日期时间字段中的值为 "0000-00-00" 或 "0000-00-00 00:00:00" 时，MySQL 将抛出警告或错误。
# ERROR_FOR_DIVISION_BY_ZERO：当除数为零时，MySQL 将抛出错误。
# NO_ENGINE_SUBSTITUTION：当请求的存储引擎不可用时，MySQL 将抛出错误，而不是自动使用另一个可用的存储引擎。
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION

# MySQL8 的密码认证插件
default_authentication_plugin=mysql_native_password

# 禁用符号链接以防止各种安全风险
symbolic-links=0

# 允许最大连接数
max_connections=1000

# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB

# 表名存储在磁盘是小写的，但是比较的时候是不区分大小写
lower_case_table_names=1
max_allowed_packet=16M

# binlog 配置
expire-logs-days = 90
max-binlog-size = 500M

# server-id 配置
server-id = 1

###### [client]配置模块 ######
[client]
default-character-set=utf8mb4

```



### 3.编写docker-compose.yml文件（请调整root用户初始密码和映射端口）

```yaml

version: '3.8'
services:
  mysql:
    # 使用 MySQL 8.0.28 镜像
    image: mysql:8.0.28
    # 容器名称为 docker_mysql
    container_name: docker_mysql
    # 容器退出时自动重启
    restart: always
    # 防止被OOM kill, -1000为最低优先级
    oom_score_adj: -1000
    environment:
      # 设置 MySQL root 用户的密码为 root
      MYSQL_ROOT_PASSWORD: "自定义密码"
    ports:
      - 3306:3306
    volumes:
      # 挂载数据目录
       - /etc/localtime:/etc/localtime
       - /opt/dockerstore/mysql/data:/var/lib/mysql
       - /opt/dockerstore/mysql/conf/my.cnf:/etc/mysql/my.cnf
       - /opt/dockerstore/mysql/log:/var/log/mysql
       - /opt/dockerstore/mysql/mysql-files:/var/lib/mysql-files
    command:
      --default-authentication-plugin=mysql_native_password
      --lower_case_table_names=1
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci

```

### 4.运行docker-compose

```sh
docker-compose up -d

#输入如下：
[root@localhost mysql]# docker-compose up
[+] Running 13/13
 ✔ mysql 12 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                                                51.5s
   ✔ 4be315f6562f Pull complete                                                                                                                                                                          6.9s
   ✔ 96e2eb237a1b Pull complete                                                                                                                                                                          4.3s                                                                                                                                                        17.1s
[+] Running 2/2
 ✔ Network mysql_default   Created                                                                                                                                                                       0.3s
 ✔ Container docker_mysql  Created                                                                                                                                                                       0.8s
Attaching to docker_mysql

```

### 5.验证

```sh
[root@localhost mysql]# docker ps | grep mysql
98d249516f57   mysql:8.0.28   "docker-entrypoint.s…"   About an hour ago   Up About an hour   33060/tcp, 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp   docker_mysql

```



