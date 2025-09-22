## FireBase接入教程

系统：Windows11
**前提：梯子一枚**

1. ### 下载[Node.js (nodejs.org)](https://nodejs.org/en)

2. 安装NodeJS并验证NodeJS和npm

```powershell
C:\Users\leegoo>node -v
v20.10.0

C:\Users\leegoo>npm -v
10.2.3
```

这样就OK了

3. 打开新的powershell窗口；执行 `npm install -g firebase-tools`和 `dart pub global activate flutterfire_cli`
```powershell
PS F:\data\leegoo\work_space\flutter\Send-It-Flutter> npm install -g firebase-tools

added 574 packages in 2m

53 packages are looking for funding
  run `npm fund` for details
npm notice
npm notice New patch version of npm available! 10.2.3 -> 10.2.5
npm notice Changelog: https://github.com/npm/cli/releases/tag/v10.2.5
npm notice Run npm install -g npm@10.2.5 to update!
npm notice
PS F:\data\leegoo\work_space\flutter\Send-It-Flutter> dart pub global activate flutterfire_cli
+ ansi_styles 0.3.2+1s... (2.3s)
+ args 2.4.2
+ async 2.11.0
+ boolean_selector 2.1.1
+ characters 1.3.0
+ ci 0.1.0
+ cli_util 0.3.5 (0.4.1 available)
+ clock 1.1.1
+ collection 1.18.0
+ dart_console 1.2.0
+ deep_pick 0.10.0 (1.0.0 available)
+ ffi 2.1.0
+ file 6.1.4 (7.0.0 available)
+ flutterfire_cli 0.2.7
+ http 0.13.6 (1.1.2 available)
+ http_parser 4.0.2
+ interact 2.2.0
+ intl 0.18.1 (0.19.0 available)
+ json_annotation 4.8.1
+ matcher 0.12.16+1
+ meta 1.11.0
+ path 1.9.0
+ petitparser 6.0.1 (6.0.2 available)
+ platform 3.1.3
+ process 4.2.4 (5.0.1 available)
+ pub_semver 2.1.4
+ pub_updater 0.2.4 (0.4.0 available)
+ pubspec 2.3.0
+ quiver 3.2.1
+ source_span 1.10.0
+ stack_trace 1.11.1
+ stream_channel 2.1.2
+ string_scanner 1.2.0
+ term_glyph 1.2.1
+ test_api 0.7.0
+ tint 2.0.1
+ typed_data 1.3.2
+ uri 1.0.0
+ win32 5.1.1
+ xml 6.4.2 (6.5.0 available)
+ yaml 3.1.2
Building package executables... (5.8s)
Built flutterfire_cli:flutterfire.
Installed executable flutterfire.
Warning: Pub installs executables into C:\Users\leegoo\AppData\Local\Pub\Cache\bin, which is not on your path.
You can fix that by adding that directory to your system's "Path" environment variable.
A web search for "configure windows path" will show you how.
Activated flutterfire_cli 0.2.7.

```

4. 	在powershell中执行` flutterfire configure` ,此时可能会报错（未报错看下一步）
```powershell
PS F:\data\leegoo\work_space\flutter\Send-It-Flutter> flutterfire configure
flutterfire : 无法将“flutterfire”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，
请确保路径正确，然后再试一次。
所在位置 行:1 字符: 1
+ flutterfire configure
+ ~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (flutterfire:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```
```powershell
如果报这个错，说明未配置`flutterfire`的环境变量，在环境变量 `Path`中加入`C:\Users\leegoo\AppData\Local\Pub\Cache\bin` ;注意：leegoo是用户名，具体请看第3步生成的路径在哪里(关注这一句`Warning: Pub installs executables into xxx...`)
```

5. 	使用管理员打开新的powershell窗口，执行`Set-ExecutionPolicy RemoteSigned`,然后输入 'Y'
6. 	在powershell窗口中，设置代理和登录，例如：
```powershell
 #1.设置代理
 PS > $Env:http_proxy="http://127.0.0.1:1111";$Env:https_proxy="http://127.0.0.1:1111"
 #2.登录
 PS > firebase login --no-localhost
 #随后按照提示，一般先需要在浏览器里面登录一次google账号，然后在powershell中在点击一个验证链接，把验证码复制需要填入的窗口即可
```