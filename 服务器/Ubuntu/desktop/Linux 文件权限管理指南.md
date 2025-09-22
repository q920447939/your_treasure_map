# Linux 文件权限管理指南

## 问题背景

在 Linux 系统中，当普通用户尝试编辑或保存位于需要 root 权限目录中的文件时，会遇到"无权限"错误。例如在 `/mnt` 目录下创建的文件，默认属于 root 用户。

## 解决方案

### 方案一：修改文件/目录所有者

#### 适用场景

- 需要完全控制特定目录及其子目录

- 个人工作目录权限管理

#### 操作命令

- 创建一个专用组来管理

  ```bash
  # 创建新组
  sudo groupadd mntusers
  
  # 将 musk 用户添加到组
  sudo usermod -a -G mntusers musk
  
  # 设置目录权限
  sudo chown -R root:mntusers /mnt
  sudo chmod -R 775 /mnt
  ```

  

- 授权

```bash


# 递归更改目录及所有子文件的所有者
sudo chown -R 用户名:用户名 /路径/到/目录

# 示例：将 /mnt 目录完全交给 musk 用户
sudo chown -R musk:musk /mnt

# 示例：将工作目录交给 musk 用户
sudo chown -R musk:musk /mnt/newdisk/work_space/musk
```

