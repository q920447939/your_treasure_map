# 禁用搜狗输入法Linux版的简繁切换快捷键

## 前言

最近将工作环境切换到了Linux下，在使用搜狗输入法时，发现其占用了快捷键**Ctrl+Shift+F**,而且设置中没有提供选项进行修改，造成了Android Studio中全局搜索不可用的情况（当然你也可以改AS的快捷键），网上找了一圈，发现没有提供有效的解决方法，遂提供一下我的解决方案。

## 解决方案

1.首先打开搜狗拼音的配置文件

```
gedit ~/.config/sogoupinyin/conf/env.ini
```

**ps:** gedit只是gnome下面自带的文本编辑工具，你也可以用vim vi等

然后找到下面这行，将后面的值改为0，保存文件

```
ShortCutFanJian=1
```

完成这一步还没结束，还需要修改fcitx的配置文件

2.打开fcitx的相关配置文件

```
gedit ~/.config/fcitx/conf/fcitx-chttrans.config
```

然后找到下面这行

```
#Hotkey=CTRL_SHIFT_F
```

将前面的注释取消，随便修改一个不常用的快捷键，比如

```
Hotkey=CTRL_SHIFT_]
```



3.重启

```
fcitx -r -d
```



