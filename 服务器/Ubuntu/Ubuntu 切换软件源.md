# Ubuntu 切换软件源

## 版本

```
root@ucloud:/home/mihomo# uname -a
Linux ucloud 6.8.0-31-generic #31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```



## 步骤

### 备份原有源配置文件

首先备份当前的源列表，避免操作失误后无法恢复：

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

编辑源配置文件,使用文本编辑器（如nano或vim）打开源配置文件：

```
sudo nano /etc/apt/sources.list
```

删除（或注释掉，在行首加#）文件中所有原有内容，替换为国内可用的镜像源（选择其中一个即可）。

可选镜像源（Ubuntu 24.04 专用）
**清华源**

```
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-security main restricted universe multiverse
```



**阿里云源**(未测试)

```
deb http://mirrors.aliyun.com/ubuntu/ noble main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ noble-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ noble-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ noble-security main restricted universe multiverse
```


网易源(未测试)

```
deb http://mirrors.163.com/ubuntu/ noble main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ noble-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ noble-backports main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ noble-security main restricted universe multiverse
```



### 保存并更新源

按Ctrl+O保存（nano 编辑器），按Ctrl+X退出。
执行以下命令更新源列表，使新源生效：

```
sudo apt update
```

