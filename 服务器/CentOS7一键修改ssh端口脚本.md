

1. 新增脚本并授权

   ```bash
   touch modify_ssh_port.sh && chmod +x ./modify_ssh_port.sh
   ```

2. 修改脚本内容

    ```bash
    #!/bin/bash
    
    # 检查是否为root用户运行
    if [ "$(id -u)" -ne 0 ]; then
        echo "请以 root 用户身份运行此脚本。"
        exit 1
    fi
    
    # 获取新端口号
    read -p "请输入新的SSH端口号（例如：2222）: " NEW_PORT
    
    # 检查端口号是否有效
    if ! [[ "$NEW_PORT" =~ ^[0-9]+$ ]] || [ "$NEW_PORT" -le 0 ] || [ "$NEW_PORT" -gt 65535 ]; then
        echo "无效的端口号，请输入1到65535之间的数字。"
        exit 1
    fi
    
    # 备份原始配置文件
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
    
    # 添加或修改端口设置
    sed -i "/^#Port 22/a Port $NEW_PORT" /etc/ssh/sshd_config
    
    # 检查是否已经存在Port指令
    if grep -q "^Port $NEW_PORT" /etc/ssh/sshd_config; then
        echo "已成功添加新的端口号：$NEW_PORT 到 SSH 配置文件。"
    else
        echo "添加新的端口号失败，请手动检查配置文件。"
        exit 1
    fi
    
    # 重启SSH服务
    systemctl restart sshd
    
    # 检查服务状态
    if systemctl is-active --quiet sshd; then
        echo "SSH 服务已成功重启。现在您可以通过新的端口 $NEW_PORT 访问服务器。"
    else
        echo "重启 SSH 服务失败，请检查日志并解决问题。"
        exit 1
    fi
    
    # 提醒用户关闭旧端口
    echo "请尝试使用新的端口登录，确认无误后再关闭旧的端口22。"
    ```

3. 如果是云服务器,记得在云服务器开放防火墙端口
