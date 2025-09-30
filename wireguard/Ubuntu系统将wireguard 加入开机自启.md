# Ubuntu系统将wireguard 加入开机自启

## 简介

WireGuard 是一个现代、高性能的 VPN 解决方案。默认情况下，每次系统重启后都需要手动执行

```bash
wg-quick up wg0
```

来启动 WireGuard。本教程将指导您如何配置 WireGuard 开机自动启动。

## 前提条件

已正确安装 WireGuard
已配置好 WireGuard 配置文件（通常位于`/etc/wireguard/wg0.conf`) 具有 sudo 权限



## 方法一：使用 systemd 模板服务（推荐）

1. 启用开机自启动

   ```
   sudo systemctl enable wg-quick@wg0
   ```

   命令原理：

   创建符号链接到系统启动目标
   系统启动时自动激活服务`@wg0`,表示使用 wg0 接口配置

2. 立即启动服务

   ```
   sudo systemctl start wg-quick@wg0
   ```

   