# Ubuntu 配置未匹配流量走 Mihomo 网卡教程

## 背景

### 操作系统版本

24 LTS

### 网卡信息

```
root@musk-computer:/home/musk# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:e6:a6:f5 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    inet 192.168.88.128/24 brd 192.168.88.255 scope global dynamic noprefixroute ens33
       valid_lft 1493sec preferred_lft 1493sec
    inet6 fe80::20c:29ff:fee6:a6f5/64 scope link 
       valid_lft forever preferred_lft forever
3: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none 
    inet 10.0.0.2/24 scope global wg0
       valid_lft forever preferred_lft forever
5: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 9a:72:93:dd:b3:8e brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
40: Mihomo: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 172.29.0.1/30 brd 172.29.0.3 scope global Mihomo
       valid_lft forever preferred_lft forever
    inet6 fe80::e08d:8199:c893:5f9c/64 scope link stable-privacy 
       valid_lft forever preferred_lft forever

```





## 核心目标

让未匹配特定网段（如 10.0.0.x、192.168.88.x）的流量，通过 Mihomo 网卡转发。

## 前提准备

执行 ip route 查看当前路由，确认默认路由（default 开头）当前走 ens33 网卡。

```
root@musk-computer:/home/musk# ip route
default via 192.168.88.2 dev ens33 proto dhcp src 192.168.88.128 metric 20100 
10.0.0.0/24 dev wg0 proto kernel scope link src 10.0.0.2 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
172.29.0.0/30 dev Mihomo proto kernel scope link src 172.29.0.1 
192.168.88.0/24 dev ens33 proto kernel scope link src 192.168.88.128 metric 100
```



确认 Mihomo 网关 IP（通常为 172.29.0.2，可从 Mihomo 配置文件或代理工具中获取）。

## 操作步骤（共 3 步）

1. 删除现有默认路由

   执行命令，删除原通过 ens33 的默认路由：

   ```
   ip route del default via 192.168.88.2 dev ens33
   ```

   

2. 添加 Mihomo 默认路由

   若已知 Mihomo 网关（如 172.29.0.2），执行：

   ```
   ip route add default via 172.29.0.2 dev Mihomo
   ```

   若无需网关（直连模式），简化为：

   ```
   ip route add default dev Mihomo
   ```

   

3. 验证生效

   执行命令查看默认路由是否切换为 Mihomo：

   ```
   root@musk-computer:/home/musk# ip route | grep default
   default dev Mihomo scope link 
   
   ```



## 异常恢复

若配置后无法上网，执行以下命令恢复原路由：

```
ip route del default dev Mihomo
ip route add default via 192.168.88.2 dev ens33
```

