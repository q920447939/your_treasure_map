# Windows10使用powershell自动连接WIFI



将下方的`ssid`和`key`改成 对应的`WIFI`名称和`密码`,当前使用的是`WPA2`加密

```powershell
# 设置WiFi参数
$ssid = "IPhone"
$key = "12345679"
$profileName = $ssid

# 创建WiFi配置文件
$profileXml = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>$profileName</name>
    <SSIDConfig>
        <SSID>
            <name>$ssid</name>
        </SSID>
        <nonBroadcast>true</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <autoSwitch>false</autoSwitch>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>$key</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"@

# 保存配置文件
$tempPath = "$env:TEMP\wifi_profile.xml"
$profileXml | Out-File -FilePath $tempPath -Encoding UTF8

# 添加WiFi配置文件
netsh wlan add profile filename="$tempPath"

# 连接WiFi
netsh wlan connect name="$ssid"

# 设置为自动连接
netsh wlan set profileparameter name="$ssid" connectionmode=auto

# 清理临时文件
Remove-Item $tempPath -Force

Write-Host "WiFi连接配置完成！"
```

