## Cento7使用rinetd端口转发

1. 将`rinetd-0.62-9.el7.nux.x86_64.rpm`传到服务器

2. 安装

   ```
   rpm -ivh rinetd-0.62-9.el7.nux.x86_64.rpm
   ```

3. 编辑配置文件

   ```
   vi /etc/rinetd.conf 
   #填入转发规则
   ```
4. 启动转发

    ```
    rinetd -c /etc/rinetd.conf
    ```

5. 停止

    ```
    pkill rinetd
    ```