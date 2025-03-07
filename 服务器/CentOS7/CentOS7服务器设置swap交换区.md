## CentOS7服务器设置swap交换区

### 1.查看当前的交换分区

```
# cat /proc/swaps 
# free -m
# swapon -s
```

### 2.增加交换分区

```
 dd if=/dev/zero of=/swap_file bs=1M count=4096
 # 注：此文件的大小是count的大小乘以bs大小，上面命令的大小是4GB
```

### 3.通过mkswap命令将上面新建出的文件做成swap分区

```
mkswap /swap_file
```

### 4.启用交换分区，并使用命令查看内存占用情况

```
# swapon /swap_file

# free -m
```

### 5.设置开机自动启动

```
# vim /etc/fstab
/swap_file swap swap defaults 0 0

或直接输入：
# echo "/data/swap swap swap defaults    0  0" >> /etc/fstab
```

### 6.查看内核参数vm.swappiness中的数值是否为0(非必须)

```
# cat /proc/sys/vm/swappiness   
# sysctl -a | grep swappiness    
# sysctl -w vm.swappiness=50


#这里需要简单说明下,在Linux系统中,可以通过查看/proc/sys/vm/swappiness内容的值来确定系统对SWAP分区的使用原则。当swappiness内容的值为0时,表示最大限度地使用物理内存,物理内存使用完毕后,才会使用SWAP分区。当swappiness内容的值为100时,表示积极地使用SWAP分区,并且把内存中的数据及时地置换到SWAP分区。注：若想永久修改，则编辑/etc/sysctl.conf文件
我们这里设置的50,就表示当物理内存少于50%时便使用交换分区。
```





### 关闭swap分区

```
# swapoff /data/swap   
# swapoff -a >/dev/null
```
