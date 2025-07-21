## python项目使用uv管理包-并在服务器上进行部署



### 创建

使用`uv init  xxx` 创建项目,`xxx`是项目名称

### 开发

`uv`会将依赖放到`pyproject.toml` 文件中

### 部署

部署机器版本

```
root@a:~# uname -v
#31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024

```

1.下载安装`uv`

```
#下载 安装
root@ucloud:/home/n8n_back_api# curl -LsSf https://astral.sh/uv/install.sh | sh
downloading uv 0.7.19 x86_64-unknown-linux-gnu
no checksums to verify
installing to /root/.local/bin   #提示安装到了 /root/.local/bin, 写入系统变量可以全局使用
  uv
  uvx
everything's installed!  

```

2.设置环境变量

```
root@ucloud:/home/n8n_back_api# echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc
root@ucloud:/home/n8n_back_api# source  ~/.bashrc
```

3.检查安装

```
root@ucloud:/home/n8n_back_api# uv
```

4.将项目文件上传到服务器中

5.`uv`设置国内镜像源

```
#UV_DEFAULT_INDEX 只能设置一个索引源，用于替换默认的 PyPI 源。
#建议使用时,先检查目标镜像源是否可用

root@ucloud:/home/n8n_back_api# uv add fastapi --default-index https://mirrors.aliyun.com/pypi/simple/
Resolved 24 packages in 1.18s
Prepared 22 packages in 742ms
Installed 22 packages in 12ms
 + annotated-types==0.7.0
 + anyio==4.9.0
 + beautifulsoup4==4.13.4
 + click==8.2.1
 + fastapi==0.115.14
 + h11==0.16.0
 + httptools==0.6.4
 + idna==3.10
 + pydantic==2.11.7
....

#如果出现下载包,那就说明uv下载依赖成功了

```





5.启动

```
 uv run python main.py
```

