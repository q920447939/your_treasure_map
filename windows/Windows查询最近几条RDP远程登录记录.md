# Windows查询最近几条RDP远程登录记录

使用工具 `powelshell`

执行命令:

```
wevtutil qe "Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational" /q:"*[System[(EventID=1149)]]" /c:3 /rd:true /f:RenderedXml
```

