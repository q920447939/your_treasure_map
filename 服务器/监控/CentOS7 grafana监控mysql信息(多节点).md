## CentOS7 grafana监控mysql信息(多节点)

前提，已经安装好mysql，并且已配置好对应的用户，建议新生成账号专门用来监控

```
## 监控专用账户权限配置：
CREATE USER '<监控专用用户名>'@'%' IDENTIFIED BY '<监控专用密码>' WITH MAX_USER_CONNECTIONS 10;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO '<监控专用用户名>'@'%';

```



## docker安装mysqld-exporter

```
#配置1 注意调整映射端口、用户名、密码、ip、端口、和 容器名称字段
docker run -d --restart=always -p 9104:9104 -e DATA_SOURCE_NAME="username:password@(127.0.0.1:3306)/" --name mysqld_exporter_3306 prom/mysqld-exporter:latest

#配置2
docker run -d --restart=always -p 9105:9104 -e DATA_SOURCE_NAME="username:password@(127.0.0.1:3307)/" --name mysqld_exporter_3307 prom/mysqld-exporter:latest


```

### 2.编辑prometheus配置信息

```
  #这里只展示配置job部分，一定要注意空格
  - job_name: 'mysql-status'
    static_configs:
    	#节点1
    	#这里填写主机ip，防止在docker容器里面不可预期的问题 ,192.168.0.123 代表的是我主机ip
      - targets: ['192.168.0.123:9104']
        labels:
          instance: '123_3306'
      - targets: ['192.168.0.123:9105']
        labels:
          instance: '123_3307'

```





### 3.查看`http://ip:9092/classic/targets` 检查 `mysql-status`节点下面是否有两个ip

1. 可以分别访问`http://192.168.0.123:9104/metrics`、`http://192.168.0.123:9105/metrics` 查看结果，正常的结果应该是输出内容比较多的，如果内容比较少，那么就是`mysqld-exporter`配置有问题，可以使用`docker logs 容器id`查看



### 4.grafana添加对应的模板

```
我使用的模板是：https://grafana.com/grafana/dashboards/17320-1-mysqld-exporter-dashboard/
ID: 17320
```

