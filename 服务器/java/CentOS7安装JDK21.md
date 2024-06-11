## CentOS7安装JDK21

```
yum install wget
wget https://objects.githubusercontent.com/github-production-release-asset-2e65be/602574963/0d2d3aa8-7467-4d65-b73b-41824aac48e9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T032751Z&X-Amz-Expires=300&X-Amz-Signature=8efa9d93e574b458add98f5de88cf906f572f4d49886b00a3e11bd42b236d070&X-Amz-SignedHeaders=host&actor_id=15419380&key_id=0&repo_id=602574963&response-content-disposition=attachment%3B%20filename%3DOpenJDK21U-jdk_x64_linux_hotspot_21.0.3_9.tar.gz&response-content-type=application%2Foctet-stream

tar -zxvf OpenJDK21U-jdk_x64_linux_hotspot_21.0.3_9.tar.gz 

mv jdk-21.0.3+9/ /usr/local


vi /etc/profile

把旧的jdk环境变量使用#注释掉，在旧的下面复制下面代码


export JAVA_HOME=/usr/local/jdk-21.0.3+9
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

source /etc/profile

#验证java配置
java -version 


```

