# Linux新增普通用户

新建 `chfs` 用户为例

1. 先删除用户

   ```
ps -u | grep pkill -9 -u chfs
   ```

2. 创建用户

   ```
   sudo useradd -m chfs    # -m 参数会创建用户主目录
   sudo passwd chfs        # 设置用户密码
   ```

   

3. 修改用户的默认 shell 为 bash：

   ```
sudo chsh -s /bin/bash chfs
   ```



4. 确保用户主目录下有基本的 bash 配置文件。可以从 /etc/skel 复制默认配置：

   ```
sudo cp /etc/skel/.bashrc /home/chfs/
sudo cp /etc/skel/.profile /home/chfs/
sudo chown chfs:chfs /home/chfs/.bashrc
sudo chown chfs:chfs /home/chfs/.profile
   ```

