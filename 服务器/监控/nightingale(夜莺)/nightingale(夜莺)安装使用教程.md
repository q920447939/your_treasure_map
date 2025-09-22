## nightingale(夜莺)安装使用教程

根据官网推荐，本示例采用二进制安装



### 简要介绍

​	`nightingale`类似于`grafana`、`Hertz Beat` ，简单理解就是 `nightingale` 负责数据的展示、与报警



### 官网支持的架构

​	架构1：各类时序数据库作为采集点，`nightingale`负责从这些数据源展示数据并且报警

![20240221152601](https://download.flashcat.cloud/ulric/20240221152601.png)



架构2：` Categraf (左侧猫爪)`采集数据源->推送到`nightingale`，`nightingale`负责存入到`VictoriaMetrics （时序数据）`，并且`nightingale`兼顾展示数据和报警

![20240221154910](https://download.flashcat.cloud/ulric/20240221154910.png)

总结：

​	架构1的好处是，采集与展示是分开的，不会受单点故障影响，但是这样的话就需要关注多个节点的健康；

​	架构2的缺点是耦合了一部分、优点是部署与运维相对简单一点

本次采用架构2部署



### 部署需求

本次希望监控两台机器(下面简称server56、和vm250)指标信息与报警、服务器信息如下：

| 服务器   | 架构                                                         |
| -------- | ------------------------------------------------------------ |
| server56 | Linux server56 3.10.0-1160.95.1.el7.x86_64 #1 SMP Mon Jul 24 13:59:37 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux |
| vm250    | Linux localhost.localdomain 4.19.90-52.22.v2207.ky10.x86_64 #1 SMP Tue Mar 14 12:19:10 CST 2023 x86_64 x86_64 x86_64 GNU/Linux |



服务器职责（部署软件）如下：

| 服务器   | 服务器职责                                       | 部署软件                                                     | 软件是否单节点 |
| -------- | ------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| server56 | 负责采集机器指标、数据库指标；展示数据、存储数据 | `Categraf（采集数据）`,`nightingale(展示数据)`,`VictoriaMetrics （时序数据库）` | 是             |
| vm250    | 负责采集机器指标                                 | `Categraf（采集数据）`                                       | 是             |

​	





### 部署

1. 下载
   1. 下载`Categraf`(本次采用`0.3.65`版本)
      1. [Releases · flashcatcloud/categraf (github.com)](https://github.com/flashcatcloud/categraf/releases)
   2. 下载`nightingale`(本次采用`v7.0.0-beta.3`版本)
      1. [Releases · ccfos/nightingale (github.com)](https://github.com/ccfos/nightingale/releases)
   3. 下载`VictoriaMetrics`(本次采用`v1.100.0`版本，注意不要下载企业版)
      1. [Releases · VictoriaMetrics/VictoriaMetrics (github.com)](https://github.com/VictoriaMetrics/VictoriaMetrics/releases)
   
1. 解压

   1. 创建对应文件夹

      ```sh
      mkdir -p /tmp/n9ee
      mkdir -p /tmp/categraf-v0.3.65
      mkdir -p /tmp/monitor/victoria
      ```
      
   1. 上传文件到服务器
      
   1. 解压
      
      ```sh
      tar -zxvf n9e-v7.0.0-beta.3-linux-amd64.tar.gz -C /tmp/n9ee
      tar -zxvf categraf-v0.3.65-linux-amd64.tar.gz -C /tmp/categraf-v0.3.65
      tar -zxvf nvictoria-metrics-linux-amd64-v1.100.0.tar.gz -C /tmp/monitor/victoria
      ```
      
      

1. 安装

   1. mysql

      1. 本次采用docker-compse安装([CentOS7安装Docker-compose](https://github.com/q920447939/your_treasure_map/blob/main/服务器/CentOS7安装Docker-compose.md))，docker-compse安装mysql（[CentOS7系统Docker安装mysql8](https://github.com/q920447939/your_treasure_map/blob/main/服务器/CentOS7系统Docker安装mysql8.md)）

   1. redis

      1. 本次采用docker-compse安装([CentOS7安装Docker-compose](https://github.com/q920447939/your_treasure_map/blob/main/服务器/CentOS7安装Docker-compose.md))，docker-compse安装redis（[Docker-compose安装redis](https://github.com/q920447939/your_treasure_map/blob/main/Docker-compose安装redis.md)）（注意修改里面的初始密码）

   1. 修改`nightingale`连接数据库的配置

      1. mysql

         1. 进入`nightingale`配置文件夹

            ```toml
            cd /tmp/n9ee/etc
            vi config.toml
            
            找到mysql的配置，进行调整
            下面是我调整好的配置
            [DB]
            DSN="root:123456@tcp(127.0.0.1:63306)/n9e_v6?charset=utf8mb4&parseTime=True&loc=Local&allowNativePasswords=true"
            ```

            

      1. redis

         1. 进入`nightingale`配置文件夹

            ```toml
            cd /tmp/n9ee/etc
            vi config.toml
            
            找到redis的配置，进行调整
            下面是我调整好的配置,有密码的话 记得把密码加上
            [Redis]
            Address = "127.0.0.1:61379"
            # Username = ""
            # Password = ""
            ```

            

   1. 执行初始化脚本(我采用的方式是`使用navivat`连接到数据库后，然后执行脚本)

      ```
      cd /tmp/n9ee
      这个目录下面有一个 n9e.sql ，执行该sql
      ```

      

1. 修改配置

   1. `nightingale`

      1. 编辑配置

         ```toml
         vi /tmp/n9ee/etc/config.toml
         
         
         [Ibex]
         Enable = true # 改为 true
         RPCListen = "0.0.0.0:20090"
         
         
         [[Pushgw.Writers]]
         Url = "http://127.0.0.1:8428/api/v1/write" #改为victoria单节点地址
         
         ```

   2. `categraf`

      1. 编辑配置(`server56`)

         ```toml
         #公共配置部分
         vi /tmp/categraf-v0.3.65/categraf-v0.3.65-linux-amd64/conf/config.toml 
          
         [global]
         hostname = "server56" #修改一下主机名称
         
         [ibex]
         enable = true  #改为true
         
         #mysql监控配置部分
         vi /tmp/categraf-v0.3.65/categraf-v0.3.65-linux-amd64/conf/input.mysql/mysql.toml
         [[instances]]
         address = "127.0.0.1:63306"
         username = "root"
         password = "123456"
         extra_status_metrics = true
         
         # 监控各个数据库的磁盘占用大小
         gather_schema_size = true
         
         # 监控所有的table的磁盘占用大小
         gather_table_size = true
         labels = { instance="server56:63306" }
         
   
         #redis监控配置部分
         vi /tmp/categraf-v0.3.65/categraf-v0.3.65-linux-amd64/conf/input.redis/redis.toml 
         
         [[instances]]
         address = "127.0.0.1:61379"
         #下面的内容按需填入
         # username = ""
         # password = ""
         labels = { instance="server56:61379" }
         
         ```
      
      2. 编辑配置(`vm250`)
         
         ```toml
         vi /tmp/categraf-v0.3.65/categraf-v0.3.65-linux-amd64/conf/config.toml 
         
          
         [global]
         hostname = "vm250" #修改一下主机名称
         
         
         [[writers]]
         url = "http://server56:17000/prometheus/v1/write"
         
         [heartbeat]
         enable = true
         # report os version cpu.util mem.util metadata
         url = "http://server56:17000/v1/n9e/heartbeat"
         
         [ibex]
         enable = true
         interval = "1000ms"
         ## n9e ibex server rpc address
         servers = ["server56:20090"]
         
         ```
         
   
5. 启动

   1. `nightingale`

      ```sh
      cd /tmp/n9ee
      ./n9e
      
      #后续最起码应该做成服务、开机自启
      ```

   2. `categraf`

      ```sh
      cd /tmp/categraf-v0.3.65/categraf-v0.3.65-linux-amd64
      ./categraf
      
      #后续最起码应该做成服务、开机自启
      ```

   3. `VictoriaMetrics`

      ```sh
      cd /tmp/monitor/victoria
       ./victoria-metrics-prod
      
      #后续最起码应该做成服务、开机自启
      ```
6. 验证
   
   1. `VictoriaMetrics`
   
      1. 访问`http://ip:8428`
   
         ```tex
         正常页面会显示
         
         Single-node VictoriaMetrics
         ```
   
   2. `categraf`
   
      1. 查看启动后，上报到`17000`端口是否报错
   
   3. `nightingale`
   
       1. 访问 `http:ip:17000`,默认用户是 `root`，密码是 `root.2020`
       2. 在左侧菜单选择`基础设施-机器列表`，中间选择`全部机器`，预计结果是2台服务器
       3. 在左侧菜单选择`集成中心-数据源`，中间选择`Prometheus Like`，URL添加`http://ip:8428`，点击 `测试并保存`
       4. 在左侧菜单选择`时序指标-即时查询`
          1. 中间应该会默认选择数据源类型=`Prometheus`、数据源=第3步配置的名称，
          2. 在`内置指标` 比如填入 `cpu_usage_system` 
          3. 点击查询
          4. 如果有两条就可以证明都配置成功了
       5. 在左侧菜单选择`仪表盘-内置仪表盘`
          1. 选择`Linux`
          2. 弹出来的页面在`Linux Host by Categraf v2` 右侧点击`查看`
          3. 会弹出来一个页面，如果出现了指标信息，证明成功

### 报警配置(按需)

参考文档 [快速配置告警规则体验夜莺告警功能 - 快猫星云 (flashcat.cloud)](http://flashcat.cloud/docs/content/flashcat-monitor/nightingale-v7/monitor/quick-config/)



### 开机自启

以`VictoriaMetrics`为例(参考官网示例)

```shell
# /etc/systemd/system/victoriametrics.service
[Unit]
Description="victoriametrics"
After=network.target

[Service]
Type=simple

ExecStart=/opt/victoriametrics/victoria-metrics-prod

Restart=on-failure
SuccessExitStatus=0
LimitNOFILE=65536
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=victoriametrics


[Install]
WantedBy=multi-user.target
```



### 实现自定义监控

TODO

参考链接：[API - 《夜莺（Nightingale）v6.1 使用手册》 - 书栈网 · BookStack](https://www.bookstack.cn/read/nightingale-6.1-zh/API.md)



### 参考文档

1. [夜莺项目整体介绍 - 快猫星云 (flashcat.cloud)](http://flashcat.cloud/docs/content/flashcat-monitor/nightingale-v7/introduction/)
2. [Categraf 总体介绍 - 快猫星云 (flashcat.cloud)](http://flashcat.cloud/docs/content/flashcat-monitor/categraf/1-introduction/)
3. [VictoriaMetrics/VictoriaMetrics: VictoriaMetrics: fast, cost-effective monitoring solution and time series database (github.com)](https://github.com/VictoriaMetrics/VictoriaMetrics)
4. [categraf各类指标监控说明](https://github.com/flashcatcloud/categraf/blob/main/inputs/mysql/README.md)

