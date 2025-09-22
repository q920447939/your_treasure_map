# semaphore迁移

1.创建服务器的用户

```
useradd -m useradd -m semaphore
```

2.将原服务器的`/home/semaphore`文件数据全部复制到新服务器`/home/semaphore`目录下

3.使用原服务器的启动方式启动`semaphore` docker服务

4.将原服务器的 `/etc/semaphore/config.json` 覆盖新服务器的 `/etc/semaphore/config.json`配置信息

5.重启`semaphore docker`服务

6.访问`HTTP//IP:33000`端口