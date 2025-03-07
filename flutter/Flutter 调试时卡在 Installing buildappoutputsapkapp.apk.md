**Flutter 调试时卡在 Installing build\app\outputs\apk\app.apk**



```
在终端

1. adb kill-server

2. taskkill /f /im adb.exe

3. adb uninstall com.gxuwz.beethoven  #后面替换你的APP包名
```

