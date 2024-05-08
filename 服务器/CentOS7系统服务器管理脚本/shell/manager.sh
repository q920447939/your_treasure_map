#!/bin/bash

# 脚本所在目录
script_dir=$(dirname "$0")

# 为所有脚本添加执行权限
chmod +x "$script_dir"/*.sh

# 引入setup_swap函数
source "$script_dir/setup_swap.sh"


# 显示一级菜单
show_main_menu() {
    clear
    echo "======================"
    echo " 管理脚本"
    echo "======================"
    echo "1. SWAP管理"
    echo "2. 设置Yum国内镜像源"
    echo "99. 退出"
    echo ""
    read -p "请选择操作 [1-99]: " choice
}

# 显示swap二级菜单
show_swap_menu() {
    clear
    echo "======================"
    echo " SWAP 管理"
    echo "======================"
    echo "1. 设置swap (1.5倍总内存)"
    echo "2. 删除swap"
    echo "3. 显示当前swap"
    echo "4. 返回上一级菜单"
    echo ""
    read -p "请选择操作 [1-4]: " choice
}

while true; do
    show_main_menu
    case $choice in
        1)
            while true; do
                show_swap_menu
                case $choice in
                    1) setup_swap ;;
                    2) swapoff -a; rm -f /swapfile ;;
                    3) free -m ;;
                    4) break ;;
                    *) echo "无效选项,请重试" ;;
                esac
                read -p "按回车键继续..."
            done
            ;;
        2)
            /bin/bash  $script_dir/set_yum.sh
            read -p "按回车键继续..."
            ;;
        99) exit 0 ;;
        *) echo "无效选项,请重试" ;;
    esac
    read -p "按回车键继续..."
done
