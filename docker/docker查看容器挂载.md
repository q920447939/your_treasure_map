# 查看 Docker 容器的挂载情况

## 更易读的格式

```bash
docker inspect -f '{{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}' container_name_or_id
```

## 查看完整挂载详情（包括类型、读写权限等）

```
docker inspect container_name_or_id | grep -A 20 "Mounts"
```

