# ubuntu系统修复gnome桌面没有设置



报错如下：

```
samba-libs : 依赖: libldb2 (= 2:2.8.0+samba4.19.5+dfsg-4ubuntu9) 但是 2:2.8.0+samba4.19.5+dfsg-4ubuntu9.2 正要被安装
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。
```



```
sudo apt update --fix-missing
sudo dpkg --configure -a
sudo apt install -f
sudo apt --fix-broken install
sudo apt install libldb2=2:2.8.0+samba4.19.5+dfsg-4ubuntu9 samba-libs=2:4.19.5+dfsg-4ubuntu9 --allow-downgrades

#重新安装控制中心
sudo apt install --reinstall gnome-control-center

#打开控制中心
gnome-control-center


```

