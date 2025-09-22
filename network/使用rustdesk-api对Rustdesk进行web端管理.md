# 使用rustdesk-api对Rustdesk进行web端管理



开源版的rustdesk 目前仅通过ID 和密码进行连接

没有一个可视化的后台页面对各类ID、设备进行管理

使用不太方便

可以使用rustdesk-api 对rustdesk连接设备、ID等进行管理



1. ## 编辑docker-compose.yml

   后续更新可以查看wiki [Use Docker With My S6 · lejianwen/rustdesk-api Wiki](https://github.com/lejianwen/rustdesk-api/wiki/Use-Docker-With-My-S6)

   ```
    networks:
      rustdesk-net:
        external: false
    services:
      rustdesk:
        ports:
          - 21114:21114
          - 21115:21115
          - 21116:21116
          - 21116:21116/udp
          - 21117:21117
          - 21118:21118
          - 21119:21119
        image: lejianwen/rustdesk-server-s6:latest
        environment:
          - RELAY=ip:21117>
          - ENCRYPTED_ONLY=1
          - MUST_LOGIN=Y #是否必须登录
          - TZ=Asia/Shanghai
          - RUSTDESK_API_RUSTDESK_ID_SERVER=ip:21116 #21116
          - RUSTDESK_API_RUSTDESK_RELAY_SERVER=ip:21117 #21117
          - RUSTDESK_API_RUSTDESK_API_SERVER=http://ip:21114 #21114
          - RUSTDESK_API_KEY_FILE=/data/id_ed25519.pub
          - RUSTDESK_API_JWT_KEY=xxxxxx # jwt key
        volumes:
          - /data/rustdesk/server:/data  #将server的key挂载出来
          - /data/rustdesk/api:/app/data #将数据库挂载
        networks:
          - rustdesk-net
        restart: unless-stopped
   
   ```

   

2. 开放防火墙指定端口 TCP:21114~21119 UDP: 21116

3. 在控制台会输出连接密码

   ![image-20250312165108330](https://github.com/lejianwen/rustdesk-api/raw/master/docs/init_admin_pwd.png)

   同时还会产生连接密钥,也需要记下来

4. http://ip:21114

5.  输入账号: `admin` ,密码是第3步的密码

6. 客户端更换认证信息

   ID服务器 ,填写你的IP

   API服务器填写 http://ip:21114

   Key 填写第三步的连接密钥

7. 账号密码进行登录即可

8. 可以在网页看到设备上线



目前已知问题:

客户端使用代理时,那么无法正常登录,但是远程功能还是可以正常使用
