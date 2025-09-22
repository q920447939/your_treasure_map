# Ubuntu机器把脚本放到桌面上



#### **创建 `.desktop` 文件**

```
nano ~/.local/share/applications/pycharm.desktop
```

#### 粘贴以下内容，并根据需要修改路径：

```
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm
Icon=/home/musk/Applications/pycharm-2025.2.1.1/bin/pycharm.png
Exec="/home/musk/Applications/pycharm-2025.2.1.1/bin/pycharm.sh" %f
Comment=The intelligent Python IDE
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-pycharm

```



#### **添加执行权限**

```
chmod +x ~/.local/share/applications/pycharm.desktop
```



#### **复制到桌面（如果文件夹存在）**

```
cp ~/.local/share/applications/pycharm.desktop ~/Desktop/


#~/Desktop/ 如果系统选的中文，可能中文
```