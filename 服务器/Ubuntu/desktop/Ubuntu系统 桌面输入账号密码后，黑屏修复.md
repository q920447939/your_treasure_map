# Ubuntu系统 桌面输入账号密码后，黑屏修复

## 操作步骤

1. 按`ctrl+alt+f3`，进入黑色终端交互模式

2. 重建`gnome`

   ```
   # 备份当前配置
   mv ~/.config ~/.config.backup
   mv ~/.local/share ~/.local/share.backup
   sudo systemctl restart gdm3
   ```

   

3. 按道理应该是可以经常进入系统了