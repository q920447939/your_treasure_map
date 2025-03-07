**由于网络原因，使用npm下载nodejs依赖包时，经常会出现下载失败的情况，这里就需要设置镜像和代理。**
现将具体操作总结如下：



1. 设置镜像
   1. npm设置镜像
    ```powershell
    npm config set registry=镜像地址
    //设置阿里镜像
    npm config set registry=https://registry.npm.taobao.org
    ```

   2. npm取消镜像
    ```powershell
    npm config delete registry
    ```

   3. npm查看镜像信息
    ```powershell
    npm config get registry
    ```
    
2. 设置代理
   1. 设置http和https代理

    ```powershell
    //设置http代理
    npm config set proxy = http://代理服务器地址:端口号
    //设置https代理
    npm config set https-proxy https://代理服务器地址:端口号
    ```
   2. 取消代理
    ```powershell
    npm config delete proxy
    npm config delete https-proxy
    ```

   3. 代理用户名和密码设置
    ```powershell
    如果代理需要认证的话，可以使用如下方式设置

    npm config set proxy http://username:password@server:port
    npm confit set https-proxy http://username:password@server:port
    ```

   4. 查看代理信息
    ```powershell
    npm config list
    ```