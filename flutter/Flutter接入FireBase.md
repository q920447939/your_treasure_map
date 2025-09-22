## Flutter接入FireBase

请先按照步骤，参考**FireBase接入** 文章 ，使firebase登录成功

温馨提醒：采用的测试项目在git目录  [Send-It-Flutter](https://github.com/Mohamed-code-13/Send-It-Flutter)

### 注册账号

1.登录 [Firebase 控制台 (google.com)](https://console.firebase.google.com/) ，然后创建一个项目 ，我创建的项目名称是 `Send-It-Flutter`

2.下载  [Send-It-Flutter](https://github.com/Mohamed-code-13/Send-It-Flutter)项目
3.在 `Send-It-Flutter`文件夹下，打开带有 代理的`powershell`窗口，并执行命令`flutterfire configure`(这里首先他会通过npm拉取你在FireBase创建的项目列表，我们选择`Send-It-Flutter`，然后生成的系统类型 根据你的当前电脑系统选择，如果是windows 就需要把IOS和MACOS 去掉，否则会报错  ) 。
```powershell
#这是我执行成功的结果
PS > flutterfire configure
i Found 1 Firebase projects.
✔ Select a Firebase project to configure your Flutter application with · send-it-flutter (Send-It-Flutter)
✔ Which platforms should your configuration support (use arrow keys & space to select)? · android, web
i Firebase android app com.example.send_it registered.
i Firebase web app send_it (web) is not registered on Firebase project send-it-flutter.
i Registered a new Firebase web app on Firebase project send-it-flutter.

Firebase configuration file lib\firebase_options.dart generated successfully with the following Firebase apps:

Platform  Firebase App Id
web       1:424699262741:web:bde473b767056b65d1f402
android   1:424699262741:android:5324ab7db638ace8d1f411
Learn more about using this file and next steps from the documentation:
 > https://firebase.google.com/docs/flutter/setup
```

4.随后使用IDE（我使用的是**Android studio**）打开`Send-It-Flutter`项目,可以发现该项目不报错了(如果没有上面的几个步骤，那么`main.dart`会报错)

