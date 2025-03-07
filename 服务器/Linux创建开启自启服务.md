# Linux创建开启自启服务

以执行 `/home/chfs/chfs-linux-amd64-3.1 -file  /home/chfs/chfs.ini` 程序为例

1. 切换root

   ```
   su root
   ```

2. 创建一个系统服务文件：

   ```
   sudo nano /etc/systemd/system/chfs.service
   
   #在 nano 编辑器中，保存文件的快捷键操作如下：
   保存文件：
   	按 Ctrl + O（字母 O）
   	然后按 Enter 确认文件名
   退出 nano：
   	按 Ctrl + X
   完整的操作流程：
   	编辑完内容后，按 Ctrl + O
   	底部会显示 "File Name to Write:"，按 Enter 确认
   按 Ctrl + X 退出编辑器
   
   其他常用的 nano 快捷键：
   	Ctrl + W：搜索文本
   	Ctrl + K：剪切当前行
   	Ctrl + U：粘贴文本
   	Ctrl + G：显示帮助信息
   在 nano 的底部会显示这些常用的快捷键提示，其中：
   	^O 表示 Ctrl + O
   	^X 表示 Ctrl + X
   	^W 表示 Ctrl + W
   ```

   

3. 在服务文件中添加以下内容：
   ```
   [Unit]
    Description=CHFS Service
    After=network.target
   
    [Service]
    Type=simple
    User=chfs
    Group=chfs
    WorkingDirectory=/home/chfs
    ExecStart=/home/chfs/chfs-linux-amd64-3.1 -file /home/chfs/chfs.ini
    Restart=always
    RestartSec=10  #10秒钟
   
    [Install]
    WantedBy=multi-user.target
   ```
4. 设置正确的权限：

   ```
   sudo chmod 644 /etc/systemd/system/chfs.service
   ```



4. 重新加载 systemd 配置：

   ```
   sudo systemctl daemon-reload
   ```
   
5. 启用并启动服务：

   ```
sudo systemctl enable chfs    # 设置开机自启
sudo systemctl start chfs     # 立即启动服务
   ```

6. 检查服务状态：

   ```
	sudo systemctl status chfs
   
    #一些有用的管理命令
    # 停止服务
    sudo systemctl stop chfs
   
    # 重启服务
    sudo systemctl restart chfs
   
    # 查看日志
    sudo journalctl -u chfs
   ```
