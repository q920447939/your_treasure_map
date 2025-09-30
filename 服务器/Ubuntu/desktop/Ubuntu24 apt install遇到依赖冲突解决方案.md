# Ubuntu24 `apt install`遇到依赖冲突解决方案



安装时提示如下：

```
musk@musk-computer:/mnt/newdisk/soft/fvm/cache-path/versions/3.35.4$ sudo apt install clang
正在读取软件包列表... 完成
正在分析软件包的依赖关系树... 完成
正在读取状态信息... 完成               
有一些软件包无法被安装。如果您用的是 unstable 发行版，这也许是
因为系统无法达到您要求的状态造成的。该版本中可能会有一些您需要的软件
包尚未被创建或是它们已被从新到(Incoming)目录移出。
下列信息可能会对解决问题有所帮助：

下列软件包有未满足的依赖关系：
 clang-18 : 依赖: libllvm18 (= 1:18.1.3-1) 但是 1:18.1.3-1ubuntu1 正要被安装
            依赖: libclang1-18 (= 1:18.1.3-1) 但是 1:18.1.3-1ubuntu1 正要被安装
            推荐: llvm-18-dev 但是它将不会被安装
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。
```



## 解决方案

### 更新 apt 源文件

#### 第一步：备份旧源列表

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

```

#### 第二步：替换 `/etc/apt/sources.list`

将原内容替换成适用于 Ubuntu 24.04 的官方源：

```
sudo tee /etc/apt/sources.list <<EOF
deb http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
EOF

```

#### 第三步：清理并刷新缓存

```
sudo apt clean
sudo apt update

```

