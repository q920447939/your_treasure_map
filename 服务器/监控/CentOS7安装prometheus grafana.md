## CentOS7安装prometheus grafana

## 安装Prometheus

### 1.创建配置目录与下载

```
#清理之前的数据
rm -rf /data/prometheus/prometheus-data

# 创建目录
mkdir -p /data/prometheus/prometheus-data
cd /data/prometheus/

# 拉取prometheus镜像
docker pull prom/prometheus

# 初次启动cp配置文件
docker run -d --name prometheus prom/prometheus

# 拷贝配置文件到 /data/prometheus/目录
docker cp prometheus:/etc/prometheus/prometheus.yml .

# 配置权限
chmod -R 775 /data/prometheus

#删除刚刚的那一个
docker stop prom/prometheus && docker rm prom/prometheus

# 启动服务
docker run  --user root --name prometheus1 -p 9092:9090 -v /data/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml -v /data/prometheus/prometheus-data:/prometheus -d prom/prometheus

```

### 2.配置prometheus监控

```
# 修改配置文件
cd /data/prometheus
vim prometheus.yml

```

```yml
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

#下面可以先忽略(未测试)

```



### 3.查看`http://ip:9092/classic/targets` 是否打开 (注意 开放`9092`端口)



## 安装Grafana

### 1.安装

```
# 拉取镜像
docker pull grafana/grafana

# 启动grafana
docker run --name grafana -d -p 3000:3000 grafana/grafana
```

### 2.开放防火墙端口`3000`

### 3.访问web端口

```
访问地址：主机IP地址加3000端口

默认用户名密码：admin/admin

能够访问就代表可以用
```



### 4.关联到prometheus

1. 点击左边的 一个`设置按钮`(我的版本是左侧倒数第二个)，然后选择 `Add data source`
2. 选择 `Prometheus`
3. 填入URL ，目前设置的端口是`9092`,所以填写的端口是 http://ip:9092
4. 点击最下面的`Save & test`
5. 提示绿色则代表成功 