# docker 操作记录

## 打包镜像与迁移镜像

```shell
docker commit ede8d3f83fef auto_report_test:1.0  # 创建带自定义标签的持久化镜像

#查看镜像,非必须
docker images | grep auto_report_test:1.0

#保存容器到指定目录
docker save auto_report_test:1.0 > migration_package.tar
```



```shell
#加载镜像
docker load -i /tmp/nb_auto_report/migration_package.tar
```



## docker运行命令

### -V 挂载

```

docker run -d -v /host/app:/app <镜像名称>  # 单路径映射

    参数说明：
    /host/app：宿主机目录路径。
    /app：容器内目标路径。
    -d：以后台模式运行容器（可选）。
    
    
```



### cp 复制

```
docker cp <容器ID>:/app /host/app_backup  # 从容器内拷贝文件到宿主机
```



运行参数

```
--network host  #已宿主机网络启动

 -w /app  指定运行目录
 
```

