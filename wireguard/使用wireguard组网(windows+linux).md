# 使用wireguard组网(windows+linux)



此次实验 windows 11 + ubuntu 24 desk

1.下载

windows

[WireGuard for Windows Downloads](https://download.wireguard.com/windows-client/)

ubuntu

```bash
sudo apt update && sudo apt install wireguard wireguard-tools -y
```



2.windows + Ubuntu配置

​	

1. ubuntu 成功公钥私钥

   1. ```
      wg genkey | sudo tee /etc/wireguard/client_private.key | wg pubkey | sudo tee /etc/wireguard/client_public.key
      #会打印出公钥， RHmdJgQffOYKAJYlQMWCiZi09XikRGjS6YH9zuLRdlw= 这就就是公钥
      
      ```

2. ​	打开wigregurad

3. 新建空隧道，名称 wg0,公钥（`3IyciwFJYyjlWRmhRkUbpnHQo0l3OFSdOJBqtOmHvmA=`）会自动生成

   ```
   [Interface]
   PrivateKey = 8LZB8ty92IoKntYejeRlChbLoc/8o/pY+PdwULBcG1Q=  #自动生成
   ListenPort = 51820   #保持默认
   Address = 10.0.0.1/24   #保持默认
   
   [Peer]
   PublicKey = RHmdJgQffOYKAJYlQMWCiZi09XikRGjS6YH9zuLRdlw=  #将第一步的ubuntu机器的公钥填入
   AllowedIPs = 10.0.0.2/24
   PersistentKeepalive = 25
   ```

   

4.   点击`连接`

5. ubuntu机器修改

   1. 创建客户端配置文件：

      ```
      sudo nano /etc/wireguard/wg0.conf
      ```

      

   2. 添加以下内容：

      ```
      [Interface]
      PrivateKey = [客户端私钥]  #可通过 /etc/wireguard/client_private.key  查看 
      Address = 10.0.0.2/24
      DNS = 8.8.8.8
      
      [Peer]
      PublicKey = [Windows服务器公钥]  # 3IyciwFJYyjlWRmhRkUbpnHQo0l3OFSdOJBqtOmHvmA=
      Endpoint = [Windows宿主机IP]:51820     #选择ubuntu和windows保持在同一个网段的ip即可， 192.168.88.1
      AllowedIPs = 10.0.0.0/24
      PersistentKeepalive = 25
      ```

      

   3. 启动 

      ```
      sudo wg-quick up wg0
      ```

      

   4. 从 Ubuntu VM ping Windows 服务器：

      ```
      ping 10.0.0.1
      ```

      

   5. 1

   6. 

   ```
   
   ```

