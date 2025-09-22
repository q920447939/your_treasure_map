## CentOS7 grafana监控主机信息(多节点)

先按照之前的教程安装`Prometheus` 和`grafana` 

### 1.主机监控node-exporter

- docker 安装

  ```shell
  docker run -d -p 9100:9100 -v /proc:/host/proc -v /sys:/host/sys -v /:/rootfs prom/node-exporter --path.procfs /host/proc --path.sysfs /host/sys --collector.filesystem.ignored-mount-points "^/(sys|proc|dev|host|etc)($|/)"
  
  #验证
  访问 http://127.0.0.1:9100/metrics 查看是否能够正常访问
  ```
- 配置prometheus监控   注意文件里面的 `static_configs`节点下面的IP 调整
  ```shell
     # 修改配置文件
    cd /data/prometheus
    vim prometheus.yml
    
  ```
  
  ```yaml
  global:
    scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  
  alerting:
    alertmanagers:
      - static_configs:
          - targets:
  
    
  
  scrape_configs:
    - job_name: "prometheus"
  
      static_configs:
        - targets: ["localhost:9090"]
  
  
    #这个随便填，这里到时候会在web 监控面板展示名称
    - job_name: 'server1'
      static_configs:
       #填写你的ip ，targets 只能保留一个
        - targets: ["ip:9100"] #单节点
        - targets: ["主机IP:8080","主机IP:9100"]  #多节点
  ```

### 2.docker 重启`prometheus `

```sh
docker restart prometheus
#听说有热加载，但是我没试过，所以就直接重启docker中的prometheus容器
```



### 3.下载模板文件

[Node Exporter Dashboard 220417 通用Job分组版 | Grafana Labs](https://grafana.com/grafana/dashboards/16098-1-node-exporter-for-prometheus-dashboard-cn-0417-job/) （ID：`16098`）



### 4.登录`http://ip:3000`

### 5.点击左侧菜单`+`，然后点击impport,选择 刚刚下载的模板文件

### 6.可以查看刚刚的模板文件渲染的统计信息



