## CentOS7系设置系统代理

### 1. 编辑`/etc/profile`

```sh
vi /etc/profile


```

### 2.填写内容

```sh
http_proxy=http://yourproxy:8080/
https_proxy=http://yourproxy:8080/
 
export http_proxy
export https_proxy
```



### 3.刷新配置文件

```sh
source /etc/profile
```

