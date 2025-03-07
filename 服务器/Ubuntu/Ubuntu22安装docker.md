## Ubuntu 22.04安装Docker

### 1.卸载旧版本

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```



### 2.更新apt包索引并安装必要的依赖包

```bash
sudo apt-get update

sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```



### 3.添加Docker的官方GPG密钥

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```



### 4.设置Docker仓库

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```



### 5.更新apt包索引

```bash
sudo apt-get update
```



### 6.安装Docker Enginesudo

```bash
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```



### 7.启动Docker服务

```bash
sudo systemctl start docker
```



### 8.验证Docker安装是否成功

```bash
docker -v
```



### 9.设置开机自启动

```bash
sudo systemctl enable docker

# 查看是否设置开机自启动
sudo systemctl is-enabled docker
```



### 10.一键脚本

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update

sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl start docker
docker -v
sudo systemctl enable docker

# 查看是否设置开机自启动
sudo systemctl is-enabled docker
```

