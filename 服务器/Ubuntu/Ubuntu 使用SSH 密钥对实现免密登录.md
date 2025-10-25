# Ubuntu 使用SSH 密钥对实现免密登录

## 注

假设我们需要连接的服务器`IP`为`192.168.1.240`

### 教程

1. 在本地生成密钥对（如果没有）

```
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_server240
# 一路回车（无需设置密码，否则仍需输密钥密码）
```



2. 将公钥上传到目标服务器（替换为实际用户名和 IP）：

```
# 格式：ssh-copy-id -i 本地公钥路径 用户名@服务器IP/域名 -p 端口（可选）
ssh-copy-id -i ~/.ssh/id_rsa_server240.pub 用户名@服务器IP
```

3. 执行这一步时，会要求输入 服务器上 ubuntu 用户的密码（仅这一次需要，用于授权将公钥写入 `~/.ssh/authorized_keys`）。



4. 配置 `~/.ssh/config`（提前固化参数，后续免输）：
为了后续用 `ssh server240` 直接免密登录，需要在配置文件中写明服务器参数（和公钥路径）：

```
Host server240
    HostName 192.168.1.240  # 服务器IP/域名
    User ubuntu             # 登录用户名（必须和上传公钥时的用户一致）
    IdentityFile ~/.ssh/id_rsa_server240  # 本地私钥路径
    # Port 22  # 非默认端口时添加
```



后续免密登录：通过 `~/.ssh/config `配置好上述参数后，直接用 `ssh server240` 即可，无需再输用户名、IP、密码。



## 传输数据（其他）

### 从本地上传文件到服务器

在 本地终端（不是服务器终端）执行

```
# 格式：scp 本地文件路径 服务器快捷名:目标路径
scp /path/to/local/file server240:/path/to/server/dir
```

### 从服务器下载文件到本地

```
scp server240:/path/to/server/file /path/to/local/dir
```

