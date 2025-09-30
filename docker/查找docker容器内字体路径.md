# Ubuntu  docker  容器内 使用 matplotlib字体加载中文乱码问题



### 查找docker容器内字体路径（`Dockerfile`版本可忽略）

1. 进入容器（`docker exec -it bash <contain_id> bash`）

2. 使用python查找

   ```
   python -c "import matplotlib; print(matplotlib.get_cachedir())"
   /root/.cache/matplotlib
   ```

   

### 解决方案

#### Dockerfile版本

利用`Dockerfile`重新制作镜像

1. 下载对应的字体数据（`.ttf`文件）

2. 在项目目录下创建一个`statis`文件夹，将下载下来的字体文件存放到`static`文件夹下

   ```
   x  2 root root     4096  9月 24 13:37 ./
   -rw-r--r--  1 root root 10541060  9月 24 13:37 NotoSansSC-Black.ttf
   -rw-r--r--  1 root root 10549812  9月 24 13:37 NotoSansSC-Bold.ttf
   -rw-r--r--  1 root root 10544812  9月 24 13:37 NotoSansSC-ExtraBold.ttf
   -rw-r--r--  1 root root 10563600  9月 24 13:37 NotoSansSC-ExtraLight.ttf
   -rw-r--r--  1 root root 10565100  9月 24 13:37 NotoSansSC-Light.ttf
   -rw-r--r--  1 root root 10553244  9月 24 13:37 NotoSansSC-Medium.ttf
   -rw-r--r--  1 root root 10560076  9月 24 13:37 NotoSansSC-Regular.ttf
   -rw-r--r--  1 root root 10549744  9月 24 13:37 NotoSansSC-SemiBold.ttf
   -rw-r--r--  1 root root 10558240  9月 24 13:37 NotoSansSC-Thin.ttf
   ```

   

3. 修改DockerFile脚本，在构建时把宿主机的字体加载到`image`中

   ```
   # 复制自定义字体文件到 Matplotlib 字体目录
   COPY ./static/ /usr/local/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/
   RUN chmod 644 /usr/local/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/*
   RUN fc-cache -fv
   ```

   

4. 重新构建`image`即可





#### Docker版本（未测试）

将获取到的`/root/.cache/matplotlib`路径结果，先进行备份，然后再清理

随后，手动将宿主机的字体文件放到容器内即可



