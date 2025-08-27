# mihomo全局代理如何设置指向哪个代理

`clash`系列产品本质是用的`mihomo`,但是`mihomo`官方似乎没有找到相对明确的说明: 配置使用全局代理,那么默认是哪一个呢?

实际上都藏在配置文件中

在 Mihomo 中，当规则指定使用"全局代理"时，具体使用的是 **`GLOBAL`** 代理组。



```
# 代理服务器配置
proxies:
  - name: "🇭🇰 HK Proxy"
    type: vmess
    server: hk.example.com
    port: 443
    uuid: your-uuid
    alterId: 0
    cipher: auto
    tls: true

# 代理组配置
proxy-groups:
  # 全局代理组 - 这就是规则中指定的 GLOBAL
  - name: "GLOBAL" # 这个名称是固定的
    type: select
    proxies:
      - "🇭🇰 HK Proxy"
      - "DIRECT"

  # 其他可能的代理组
  - name: "Proxy"
    type: select
    proxies:
      - "GLOBAL"
      - "🇯🇵 JP Proxy"


```

## 关键点说明

1. **GLOBAL 是特殊名称**：Mihomo 中 `GLOBAL` 是一个特殊的关键字，代表全局代理组
2. **类型选择**：
   - `select`：手动选择代理
   - `url-test`：自动选择延迟最低的
   - `fallback`：故障转移模式



## 改动

```
mode: global #将代理模式改成 global

proxy-groups: #增加`global`代理配置部分
- name: GLOBAL
  type: select
  proxies:
  - 测试代理   #如果是这样配置的话,那么默认就是选择的全局代理,并且选用的代理是 "测试代理 "
```





