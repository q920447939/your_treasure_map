# RocketMQ双nameserver双broker-Doker部署教程

注: 如果在同一台机器上面部署多个name-server/broker ,那么需要手动调整配置的监听端口号,

这里默认是两台机器

### 1.镜像拉取

```
docker pull foxiswho/rocketmq:4.7.0
```

## 2.配置文件

创建两个`broker`配置文件`broker-a.properties， broker-b.properties`

创建配置文件路径:

```
mkdir -p /home/rocketmq/conf
cd /home/rocketmq/conf
touch broker-a.properties broker-b.properties
```



配置文件`broker-a.properties`(注意修改对外IP)

```
#集群名字
brokerClusterName=DefaultCluster

#服务分片名称
brokerName=broker-a
#集群中 0 表示 Master，>0 表示 Slave
brokerId=0

#Broker 的角色
#- ASYNC_MASTER 异步复制Master
#- SYNC_MASTER 同步双写Master
#- SLAVE
brokerRole=ASYNC_MASTER

#刷盘方式
#- ASYNC_FLUSH 异步刷盘
#- SYNC_FLUSH 同步刷盘
flushDiskType=ASYNC_FLUSH

#对外ip
brokerIP1=172.18.13.56

#在发送消息时，自动创建服务器不存在的topic，默认创建的队列数
defaultTopicQueueNums=4
#是否允许 Broker 自动创建Topic，建议线下开启，线上关闭
autoCreateTopicEnable=true
#是否允许 Broker 自动创建订阅组，建议线下开启，线上关闭
autoCreateSubscriptionGroup=true

#删除文件时间点，默认凌晨 4点
deleteWhen=04
#文件保留时间，默认 48 小时
fileReservedTime=48
#commitLog每个文件的大小默认1G
mapedFileSizeCommitLog=1073741824
#ConsumeQueue每个文件默认存30W条，根据业务情况调整
mapedFileSizeConsumeQueue=300000
#destroyMapedFileIntervalForcibly=120000
#redeleteHangedFileInterval=120000
#检测物理文件磁盘空间
diskMaxUsedSpaceRatio=88

#限制的消息大小
maxMessageSize=65536
#flushCommitLogLeastPages=4
#flushConsumeQueueLeastPages=2
#flushCommitLogThoroughInterval=10000
#flushConsumeQueueThoroughInterval=60000

#checkTransactionMessageEnable=false
#发消息线程池数量
sendMessageThreadPoolNums=128
#拉消息线程池数量
#pullMessaeThreadPoolNums=128

#发送消息是否使用可重入锁
useReentrantLockWhenPutMessage=true
waitTimeMillsInSendQueue=300  #或者更大

```

配置文件broker-b.properties，在配置文件broker-a.properties的基础上修改：(注意修改对外IP)

```
#集群名字
brokerClusterName=DefaultCluster

#服务分片名称
brokerName=broker-a
#集群中 0 表示 Master，>0 表示 Slave
brokerId=0

#Broker 的角色
#- ASYNC_MASTER 异步复制Master
#- SYNC_MASTER 同步双写Master
#- SLAVE
brokerRole=ASYNC_MASTER

#刷盘方式
#- ASYNC_FLUSH 异步刷盘
#- SYNC_FLUSH 同步刷盘
flushDiskType=ASYNC_FLUSH

#对外ip
brokerIP1=172.18.13.56

#在发送消息时，自动创建服务器不存在的topic，默认创建的队列数
defaultTopicQueueNums=4
#是否允许 Broker 自动创建Topic，建议线下开启，线上关闭
autoCreateTopicEnable=true
#是否允许 Broker 自动创建订阅组，建议线下开启，线上关闭
autoCreateSubscriptionGroup=true

#删除文件时间点，默认凌晨 4点
deleteWhen=04
#文件保留时间，默认 48 小时
fileReservedTime=48
#commitLog每个文件的大小默认1G
mapedFileSizeCommitLog=1073741824
#ConsumeQueue每个文件默认存30W条，根据业务情况调整
mapedFileSizeConsumeQueue=300000
#destroyMapedFileIntervalForcibly=120000
#redeleteHangedFileInterval=120000
#检测物理文件磁盘空间
diskMaxUsedSpaceRatio=88

#限制的消息大小
maxMessageSize=65536
#flushCommitLogLeastPages=4
#flushConsumeQueueLeastPages=2
#flushCommitLogThoroughInterval=10000
#flushConsumeQueueThoroughInterval=60000

#checkTransactionMessageEnable=false
#发消息线程池数量
sendMessageThreadPoolNums=128
#拉消息线程池数量
#pullMessaeThreadPoolNums=128

#发送消息是否使用可重入锁
useReentrantLockWhenPutMessage=true
waitTimeMillsInSendQueue=300  #或者更大
[root@server56 conf]# vi broker-b.properties
[root@server56 conf]# cat broker-b.properties
#集群名字
brokerClusterName=DefaultCluster

#服务分片名称
brokerName=broker-b
#集群中 0 表示 Master，>0 表示 Slave
brokerId=0

#Broker 的角色
#- ASYNC_MASTER 异步复制Master
#- SYNC_MASTER 同步双写Master
#- SLAVE
brokerRole=ASYNC_MASTER

#刷盘方式
#- ASYNC_FLUSH 异步刷盘
#- SYNC_FLUSH 同步刷盘
flushDiskType=ASYNC_FLUSH

#对外ip
brokerIP1=172.18.13.56

#在发送消息时，自动创建服务器不存在的topic，默认创建的队列数
defaultTopicQueueNums=4
#是否允许 Broker 自动创建Topic，建议线下开启，线上关闭
autoCreateTopicEnable=true
#是否允许 Broker 自动创建订阅组，建议线下开启，线上关闭
autoCreateSubscriptionGroup=true

#删除文件时间点，默认凌晨 4点
deleteWhen=04
#文件保留时间，默认 48 小时
fileReservedTime=48
#commitLog每个文件的大小默认1G
mapedFileSizeCommitLog=1073741824
#ConsumeQueue每个文件默认存30W条，根据业务情况调整
mapedFileSizeConsumeQueue=300000
#destroyMapedFileIntervalForcibly=120000
#redeleteHangedFileInterval=120000
#检测物理文件磁盘空间
diskMaxUsedSpaceRatio=88

#限制的消息大小
maxMessageSize=65536
#flushCommitLogLeastPages=4
#flushConsumeQueueLeastPages=2
#flushCommitLogThoroughInterval=10000
#flushConsumeQueueThoroughInterval=60000

#checkTransactionMessageEnable=false
#发消息线程池数量
sendMessageThreadPoolNums=128
#拉消息线程池数量
#pullMessaeThreadPoolNums=128

#发送消息是否使用可重入锁
useReentrantLockWhenPutMessage=true
waitTimeMillsInSendQueue=300  #或者更大

```



## 3.启动容器

启动rocket需要启动两个服务：**namesrv和broker**，启动顺序要先namesrv后broker

### 1）启动namesrv

在两台机器都启动，执行脚本：（把–name rmqnamesrv-1 改成不一样就行）

```
	docker run -d \
	--network net \
	-v /usr/local/docker/rocketmq/mqbroker1/logs:/home/rocketmq/logs \
	--name rmqnamesrv-1 \
	-e "JAVA_OPT_EXT=-Xms512M -Xmx512M -Xmn128m" \
	-p 9876:9876 \
	foxiswho/rocketmq:4.7.0 sh mqnamesrv


	docker run -d \
	--network net \
	-v /usr/local/docker/rocketmq/mqbroker1/logs:/home/rocketmq/logs \
	--name rmqnamesrv-2 \
	-e "JAVA_OPT_EXT=-Xms512M -Xmx512M -Xmn128m" \
	-p 9876:9876 \
	foxiswho/rocketmq:4.7.0 sh mqnamesrv

```



### 2）启动broker

```
docker run -d \
-v /home/rocketmq/conf/:/home/rocketmq/conf \
--name rmqbroker-a-master \
-e "NAMESRV_ADDR=172.18.13.56:9876;172.18.13.56:9877" \
-e "JAVA_OPT_EXT=-Xms512M -Xmx512M -Xmn128m -XX:-AssumeMP" \
-p 10911:10911 -p 10912:10912 -p 10909:10909 \
foxiswho/rocketmq:4.7.0 \
sh mqbroker -c /home/rocketmq/conf/broker-a.properties


docker run -d \
-v /home/rocketmq/conf/:/home/rocketmq/conf \
--name rmqbroker-b-master \
-e "NAMESRV_ADDR=172.18.13.56:9876;172.18.13.56:9877" \
-e "JAVA_OPT_EXT=-Xms512M -Xmx512M -Xmn128m -XX:-AssumeMP" \
-p 10911:10911 -p 10912:10912 -p 10909:10909 \
foxiswho/rocketmq:4.7.0 \
sh mqbroker -c /home/rocketmq/conf/broker-b.properties

注：如果要把数据挂载出来可以加上(未测试)
-v /usr/local/docker/rocketmq/mqbroker/logs:/home/rocketmq/logs
-v /usr/local/docker/rocketmq/mqbroker/store:/home/rocketmq/store \
```

## 4.安装rocketmq-console控制台可视化界面

### 1）镜像

```
docker pull styletang/rocketmq-console-ng:1.0.0
```

### 2）启动容器

```
#把 -Drocketmq.namesrv.addr=192.168.56.121:9876;192.168.56.122:9876 修改实际的nameserver
docker run -d \
--name rmqconsole \
-e "JAVA_OPTS=-Drocketmq.namesrv.addr=192.168.56.121:9876;192.168.56.122:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false" \
-p 8180:8080 -t styletang/rocketmq-console-ng:1.0.0
```

### 3）访问界面

> #修改成实际的IP
>
> http://192.168.56.123:8180





参考文章:[一佳互联-docker部署rocketmq双主双从模式](https://www.yjlink.cc/?id=3297)