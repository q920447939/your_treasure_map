# 3 分钟创建 Telegram 机器人

> 不需要服务器、不需要写代码，只要手机 + 浏览器即可
>  完成后你会得到：
>
> - 一个 **Bot Token**（`123456:ABC-DEF...`）
> - 一个 chat ID
> - 后面直接对接 n8n、Zapier、Make、自己脚本都行



## 1. 新建机器人

1. 打开 Telegram，搜索 **@BotFather**（官方唯一管理入口）

2. 点`START`，输入

   ```
   /newbot
   ```

3. 起名字（显示名称）：`旺财日报`

4. 起用户名（必须`_bot`结尾）,如 `wangcai_daily_bot`,成功会返回

   

   Done! Congratulations on your new bot. You will find it at [t.me/wangcai_daily_bot](http://t.me/wangcai_daily_bot). You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

   Use this token to access the HTTP API:`8146486495:AAG4-uFTuWGzEz_qQpY16JwFiVKI7MNV3Ao`,Keep your token**secure**

   and**store it safely**, it can be used by anyone to control your bot.

   For a description of the Bot API, see this page: https://core.telegram.org/bots/api

   

   看到 `Use this token to access the HTTP API:8046486295:AAG5-uFTuWGzEz_qQpY16JwFiVKI7sAE3No` ,后面就是 创建好机器人对应的`token`

   ⚠️ 复制完立刻存到密码管理器，泄露就要重新生成。

   

##     2. 立刻给机器人发第一条消息

​	在 Telegram 顶部搜索刚才的用户名 `wangcai_daily_bot` → 打开对话 → 随便发一句 `hi`（这是为了后续能用 `/getUpdates` 取到 `chat_id`）

## 总结

这样就完成了机器人的创建