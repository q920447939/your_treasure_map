## WIN10允许多用户同时远程登录

1. 判断电脑是否已经激活（如果已经激活了直接跳到第2步）
   1. 未激活先下载`KMSpico win10激活工具`
   2. 进行安装
   3. 安装完成查看是否已经激活完成
2. 修改注册表信息,参考 `https://blog.csdn.net/fallingflower/article/details/125215235`
3. 下载[RDPWrap-master.zip](https://github.com/stascorp/rdpwrap/releases/download/v1.6.2/RDPWrap-v1.6.2.zip)
4. 管理员运行`install.bat` 
5. 打开`RDPConf.exe`,查看是否被支持(都要是绿色才行，同时把 `Single session per user` 去掉)
   1. 如果右边显示不支持,在[10.0.19041.4474 on Windows 10 22H2 · Issue #2840 · stascorp/rdpwrap (github.com)](https://github.com/stascorp/rdpwrap/issues/2840) `issue` 输入对应的系统版本号
   2. 找到最新的`rdpwrap.ini`配置文件，将新的配置文件添加到`C:\Program Files\RDP Wrapper\rdpwrap.ini`
   3. `cmd`输入`services`，找到`remote desktop services`服务，右键点击重启
6. 使用`RDPCheck.exe`测试，如果另外一个用户能够正常登录，那么就没问题。

`RDPWrap` 竞品 [SuperRDP](https://github.com/anhkgg/SuperRDP)

## Windows隐藏已登录过的用户名

1. 新建.reg文件，填入代码

   ```cmd
   Windows Registry Editor Version 5.00
   
   [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList]
   "sysgeekdemo"=dword:00000000
   
   #sysgeekdemo 是你需要隐藏的用户名
   ```
   
2. 运行reg文件

3. 远程登录查看

   



