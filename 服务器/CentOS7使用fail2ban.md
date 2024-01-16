## CentOS7使用fail2ban

**注意：需要python开发环境，并且版本大于2.4**

```sh
[root@ localhost ~]# python -V      #查看当前系统中python的版本。
Python 2.6.6
```



### SSH

1.修改ssh默认端口为`60022`

```sh
[root@centos ~]# vi /etc/ssh/sshd_config
找到#Port 22，默认是注释掉的，先把前面的#号去掉，再插入一行设置成你想要的端口号，注意不要跟现有端口号重复

......

# If you want to change the port on a SELinux system, you have to tell
# SELinux about this change.
# semanage port -a -t ssh_port_t -p tcp #PORTNUMBER
Port 60022
.....

```

2.防火墙开放端口`60022`

```sh
firewall-cmd --zone=public --add-port=60022/tcp --permanent
firewall-cmd --reload
```

3.重启SSH服务

```sh
systemctl restart sshd  
shutdown -r now   #按需重启系统
```



### 设置DNS（可选）

1.编辑配置`vi /etc/resolv.conf` 

```sh
vi /etc/resolv.conf

在后面添加内容:

nameserver 8.8.8.8
search localdomain

```





### fail2ban（ssh）

1.安装`fail2ban`

```
[root@ localhost ~]# yum -y install epel-release
[root@ localhost ~]# yum -y install fail2ban

```

2.复制配置

```
cd /etc/fail2ban 
sudo cp fail2ban.conf fail2ban.local
sudo cp jail.conf jail.local
```

3.修改配置

```
vi /etc/fail2ban/jail.conf

#找到sshd那一块，把下面的进行替换
[sshd]
enabled  = true
#修改刚刚的端口号
port    = 60022
filter   = sshd
logpath = /var/log/secure
backend = %(sshd_backend)s
#最大重试次数
maxretry = 2
#封禁时间，单位s。-1为永久封禁
bantime  = 120


```



4.修改拒绝策略

Fail2ban 的默认 iptables 封禁策略为 REJECT –reject-with icmp-port-unreachable，需要变更 iptables 封禁策略为 DROP。

```sh
cp /etc/fail2ban/action.d/iptables-multiport.conf /etc/fail2ban/action.d/iptables-multiport.local
vi /etc/fail2ban/action.d/iptables-multiport.local

修改内容如下：

[Init]

blocktype = DROP
```





5.重启fail2ban

```sh
systemctl restart fail2ban
```



6.查看fail2ban状态

```sh
[root@server ~]# fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed:	1
|  |- Total failed:	4
|  `- Journal matches:	_SYSTEMD_UNIT=sshd.service + _COMM=sshd
`- Actions
   |- Currently banned:	1
   |- Total banned:	1
   `- Banned IP list:	82.116.189.56  #此处可以看到有一台ip被封禁了
```

​	如果需要解封ip。那么用命令`fail2ban-client set [监狱名称] unbanip [封禁IP]` ,例如：`fail2ban-client set sshd unbanip 82.116.189.56`

7.查看`fail2ban`日志

```sh
 cat  /var/log/fail2ban.log
```

### HTTP访问频率限制

