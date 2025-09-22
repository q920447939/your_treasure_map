在 idea 或者其他 Jetbrains IDE 中，如果你使用的版本是 2023.x 或以前，在 idea 中运行 dockerfile 时，在配置正确的远程 docker 服务器后，可以正常运行构建，但是在更新到 2024 版本后，idea 无法正常构建 dockerfile，提示 docker.exe 找不到

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7b9090bbe6c2ed5eda37e86b5877a380.png)



### 解决办法

#### 下载docker.exe

在链接中选择最新的 docker，解压到任意目录

[Index of win/static/stable/x86_64/](https://download.docker.com/win/static/stable/x86_64/)

这里下载的是`docker-26.1.0.zip`



解压后，在idea - 设置 - 构建、执行、部署 - Docker中找到工具，选择docker.exe解压的位置，点击确定

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/855c9c52723988c7f11d2c1c90364dab.png)



#### 解决buildx工具找不到的问题

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3bdff4fe32ab6477fcf4d4c58fc924ad.png)



在上述流程后，仍有可能出现buildx工具无法找到的情况，此时，在你的用户文件夹下（或在文件管理地址栏输入 `%USERPROFILE%` 定位），新建` .docker` 文件夹（注意有个“.”），下面再新建一个`cli-plugins`文件夹，访问如下 [链接](https://github.com/docker/buildx/releases/download/v0.13.1/buildx-v0.13.1.windows-amd64.exe) ，下载下来，然后重命名为 `docker-buildx.exe`，然后放入该文件夹中





参考

[【IDEA】解决idea2024无法使用远程构建dockerfile的问题_idea找不到docker.exe-CSDN博客](https://blog.csdn.net/Equent/article/details/137779505)