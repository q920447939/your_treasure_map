# Ubuntu 安裝 Maven 並配置 MAVEN_HOME

1. 從 Maven 官方網站 下載最新版本的壓縮包，或使用以下命令直接下載：

   ```
   wget https://dlcdn.apache.org/maven/maven-3/3.9.11/binaries/apache-maven-3.9.11-bin.tar.gz
   ```

   

2. 解压

   ```
   tar -zxvf apache-maven-3.9.11-bin.tar.gz
   cd apache-maven-3.9.11
   ```

   

3. 将maven加入环境变量

   ```
   sudo nano /etc/profile
   
   #在最后一行添加
   export MAVEN_HOME=/mnt/newdisk/download/apache-maven-3.9.11
   export PATH=$MAVEN_HOME/bin:$PATH
   
   #刷新环境变量
   source /etc/profile
   ```

   

4. 修改存储位置（可选）

   ```
   cd conf/
   
   nano settings.xml
   
   #将 localRepository 注释放开，再调整想要的路径
   <localRepository>/mnt/newdisk/download/apache-maven-3.9.11/repo</localReposit>
   
   ```

   