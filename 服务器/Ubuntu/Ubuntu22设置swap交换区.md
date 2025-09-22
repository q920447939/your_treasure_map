## Ubuntu22设置swap交换区

### 1. 查看当前的交换分区

```
# 以下三个命令都可以查看swap状态
free -h
swapon --show
cat /proc/swaps
```



### 2. 创建swap文件

```
# 创建4GB的swap文件
sudo fallocate -l 4G /swapfile

# 如果fallocate命令不可用，可以使用dd命令替代
sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
```

### 3. 设置正确的权限

```
# 设置安全权限
sudo chmod 600 /swapfile
```

### 4. 将文件格式化为swap格式

```
sudo mkswap /swapfile
```

### 5. 启用swap文件

```
# 启用swap
sudo swapon /swapfile

# 验证swap是否启用
free -h
```

### 6. 设置开机自动启用swap

```
# 备份fstab文件
sudo cp /etc/fstab /etc/fstab.backup

# 添加swap配置到fstab
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 7. 调整Swappiness值（可选）

```
# 查看当前swappiness值
cat /proc/sys/vm/swappiness

# 临时修改swappiness值为50
sudo sysctl vm.swappiness=50

# 永久修改swappiness值，编辑sysctl.conf
echo 'vm.swappiness=50' | sudo tee -a /etc/sysctl.conf
```



### 8. 关闭swap（如需要）

```
# 临时关闭所有swap
sudo swapoff -a

# 关闭指定的swap文件
sudo swapoff /swapfile

# 如果要永久关闭，还需要从/etc/fstab中删除相关配置
sudo sed -i '/swapfile/d' /etc/fstab
```



### 9. 一键设置swap=4G脚本

   ```
   # 创建4GB的swap文件
   sudo fallocate -l 4G /swapfile
   
   # 如果fallocate命令不可用，可以使用dd命令替代
   sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
   
   # 设置安全权限
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   # 启用swap
   sudo swapon /swapfile
   
   # 验证swap是否启用
   free -h
   # 备份fstab文件
   sudo cp /etc/fstab /etc/fstab.backup
   
   # 添加swap配置到fstab
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   
   ```

