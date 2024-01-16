## WIN10允许多用户同时远程登录

1. 判断电脑是否已经激活（如果已经激活了直接跳到第2步）
   1. 未激活先下载`KMSpico win10激活工具`
   2. 进行安装
   3. 安装完成查看是否已经激活完成

2. 修改注册表信息,参考 `https://blog.csdn.net/fallingflower/article/details/125215235`

3. 下载[RDPWrap-master.zip](https://github.com/stascorp/rdpwrap/releases/download/v1.6.2/RDPWrap-v1.6.2.zip)

4. 修改`RDPWrap-master`文件夹为`RDP Wrapper`

5. 放到`C:\Program Files\`下

6. 管理员运行`install.bat` 

6. 使用管理员运行`cmd`,执行cmd命令
	```bat
    rdpwinst -u -k
    rdpwinst -i
   ```
   
8. 打开`RDPConf.exe`,查看是否被支持

9. 使用`RDPCheck.exe`测试

