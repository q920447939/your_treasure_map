麒麟操作系统安装Wireguard(作为客户端)



系统版本

```
[root@localhost wireguard]# cat /etc/os-release
NAME="Kylin Linux Advanced Server"
VERSION="V10 (Lance)"
ID="kylin"
VERSION_ID="V10"
PRETTY_NAME="Kylin Linux Advanced Server V10 (Lance)"
ANSI_COLOR="0;31"


```

1. 下载rpm包

   ```
   wget  https://archive.kylinos.cn/yum/v10/kcnos/stable/x86_64/toplink/packages/wireguard-tools/1.0.20200102/1.ky10/x86_64/
   ```

   

2. 安装

   ```
   rpm -ivh ./wireguard-tools-1.0.20200102-1.ky10.x86_64.rpm
   ```

   

3. 创建目录和配置文件

   ```
   mkdir -p /etc/wireguard/
   touch  wg0.conf
   ```

   

4. 生成公钥和私钥

   ```
   	# 生成私钥和公钥
   	wg genkey | tee clientprivatekey | wg pubkey > clientpublickey
   ```

   

5. 编辑`wg0`配置

   ```ini
   	# vim wg0.conf
   	
   	填入如下内容
   	[Interface]
   	PrivateKey = <此处粘贴上一步生成的客户端私钥内容>
   	Address = 10.0.0.2/24  # 客户端在VPN隧道内的IP地址，由服务端分配
   	[Peer]
   	PublicKey = <此处粘贴WireGuard服务器的公钥>
   	Endpoint = <服务器的公网IP或域名>:<服务器监听的端口>  # 例如：123.45.67.89:51820
   	AllowedIPs = 0.0.0.0/0  # 表示所有流量都通过隧道转发，也可按需设置，如192.168.1.0/24
   	PersistentKeepalive = 25  # 保持NAT连接，可选但推荐
   ```

   

6. 启动

   ```
   wg-quick up wg0
   ```

   

7. 查看握手和传输统计

   ```
   方式1：wg
   	[root@localhost wireguard]# wg
       interface: wg0
         public key: ***
         private key: (hidden)
         listening port: 33044
   
       peer: ***
         endpoint: ***:51820
         allowed ips: 10.0.0.0/24
         latest handshake: 1 minute, 58 seconds ago
         transfer: 70.14 KiB received, 75.29 KiB sent
         persistent keepalive: every 25 seconds
   
   方式2：直接ping 10.0.0.x 网段ip即可
   ```

   

8. 开机启动

   ```
   systemctl enable wg-quick@wg0.service
   ```

   

9.  其他命令

   ```
   重启WireGuard接口：wg-quick down wg0 && wg-quick up wg0
   重启WireGuard服务：systemctl restart wg-quick@wg0.service
   ```



如系统升级了 `python`版本导致 `yum`异常，可以替换命令 ` sudo  /usr/bin/python3.7 /usr/bin/yum`

