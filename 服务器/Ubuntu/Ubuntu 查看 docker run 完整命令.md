# Ubuntu 查看 docker run 完整命令



## 版本

```
root@ucloud:/home/mihomo# uname -a
Linux ucloud 6.8.0-31-generic #31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

## 切换软件源（可选）

参考[Ubuntu 切换软件源](./Ubuntu 切换软件源.md)



## 使用pipx（适合安装命令行工具）

pipx专门用于安装 Python 应用，会自动创建独立虚拟环境并将工具添加到系统 PATH：

```
# 1. 先安装pipx（系统级工具，用apt）
sudo apt update && sudo apt install pipx

# 2. 确保pipx路径被添加到环境变量（可能需要重启终端）
pipx ensurepath

# 3. 用pipx安装runlike
pipx install runlike
```

## 运行命令

```
runlike -p <container_name>  # 后面可以是容器名和容器id，-p参数是显示自动换行
```

