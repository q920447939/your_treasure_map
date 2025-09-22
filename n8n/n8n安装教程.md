

部署服务器(`ubuntu 24 lts`)

```
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -e N8N_SECURE_COOKIE=false  -e HTTP_PROXY=http://172.17.0.1:17893 -e HTTPS_PROXY=http://172.17.0.1:17893  -e NO_PROXY=localhost,127.0.0.1,*.internal.example.com  -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```



温馨提示: 由于n8n 的很多节点需要 代理才可以正常访问,所以我们设置 一个代理

至于宿主机增加架设代理,可以参考我的文章`ubuntu服务器安装mihomo`