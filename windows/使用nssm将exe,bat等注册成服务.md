## 使用`nssm`将`exe,bat`等注册成服务

使用自带的`sc`命令, 因为启动路径是从`C:\Windows\System32`运行,那么可能会导致启动参数异常，同时 `bat`脚本中，无法使用`sc`命令（因为`bat`脚本没有类似于实现`windows服务`接口回调，`windows服务`会认为启动服务失败）

使用`nssm`可以避免类似问题

`nssm`不可以直接打开

### 安装

1.先使用`cmd`命令到`nssm`目录下

2.使用`nssm.exe install MyServer` 安装服务（`MyServer`调整成对应的服务名称）

3.`nssm`会弹出配置页面，选择对应的程序（`exe`,`bat`等），也可以配置启动参数

4.`启动服务`



### 删除服务

1.`nssm remove <服务名>`

2.通过 Windows 命令行使用 sc 删除服务（**慎用**）

- 这种方式只是从系统中删除服务项；
- 不会自动清理 NSSM 创建的配置文件或日志；



