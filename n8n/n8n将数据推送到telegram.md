# n8n 把任意数据推送到 Telegram 群组（含 Chat-ID 获取）

> 全程零代码，5 分钟跑通



## 1. 前置准备

| 项目               | 值                                                           |
| :----------------- | :----------------------------------------------------------- |
| n8n 地址           | 本地 `http://localhost:5678` 或云端实例                      |
| Telegram Bot Token | 参考教程:[3 分钟创建 Telegram 机器人](3 分钟创建 Telegram 机器人.md)<br />示例`token`: 8046486225:AAG5-uFTuWGzEz_qQpY16JwFiVKI7sAE3Zo |
| 目标群 Chat-ID     | 首次用 `-100xxx` 格式，下文教你取                            |

## 2. 获取群组 Chat-ID（一次性）

1. 把 Bot 拉进群 → **设为管理员**（至少给“读取消息”）。

2. 在群里发一条消息，浏览器访问

   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```

3. 返回 JSON 里找到
   `"chat":{"id":-1001876543210,"title":"你的群名"}`复制 `-1001876543210` 备用。

## 3. n8n 创建工作流

1. 新建 **Workflow**

2. 按业务需要选触发器，这里演示 **Schedule**（每天 9 点）。

## 4. 节点 1：读取要推送的数据（示例）

   - 类型：**code**

   - 代码：返回 1 条演示数据

   - Language: JavaScript

     ```
     return {
       "code":"hello world"
     }
     ```

## 5. 节点 2：Telegram 发送

按照下图进行配置,然后点击 `Execute step`,进行测试

**注意**:如果提示网络错误,可以参考 [使用mihomo方式启动进行代理](../clash/使用mihomo方式启动进行代理.md)

![image.png](https://s2.loli.net/2025/09/08/Qa9fTqKtEjiluNM.png)