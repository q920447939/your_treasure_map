#!/bin/bash

# 设置swap函数
setup_swap() {
    # 检查当前swap大小
    swap_before=$(free -m | awk '/Swap:/ { print $2 }')

    # 如果有swap则禁用并删除
    if [ $swap_before -gt 0 ]; then
        swapoff -a
        rm -f /swapfile
    fi

    # 获取总内存大小
    mem_total=$(free -m | awk '/Mem:/ { print $2 }')

    # 计算新的swap大小 (1.5倍于总内存)
    swap_size=$((mem_total * 3 / 2))

    # 创建新的swap文件
    fallocate -l ${swap_size}M /swapfile

    # 设置权限
    chmod 600 /swapfile

    # 格式化为swap
    mkswap /swapfile

    # 启用swap
    swapon /swapfile

    # 验证新的swap大小
    swap_after=$(free -m | awk '/Swap:/ { print $2 }')
    echo "Swap before: $swap_before MB, Swap after: $swap_after MB"

    # 添加到fstab使其永久生效
    echo "/swapfile swap swap defaults 0 0" >> /etc/fstab
}

setup_swap