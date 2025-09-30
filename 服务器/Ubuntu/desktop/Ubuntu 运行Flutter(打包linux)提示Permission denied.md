# Ubuntu 运行Flutter(打包`linux`)提示`Permission denied.`

```
Flutter assets will be downloaded from https://storage.flutter-io.cn. Make sure you trust this source!
Launching lib/main.dart on Linux in debug mode...
CMake Error at cmake_install.cmake:66 (file):
  file INSTALL cannot copy file
  "/mnt/newdisk/work_space/musk/flutter_application_base/example/build/linux/x64/debug/intermediates_do_not_run/example"
  to "/usr/local/example": Permission denied.
2

Error: Build process failed
```



这个错误是因为Flutter构建过程试图将应用程序安装到`/usr/local/`目录，而这个目录需要root权限才能写入。

## 解决方案

1. 使用`root`用户（不推荐）

2. 修改安装目录下的Cmake文件（不推荐，每个项目都需要修改）

3. 环境变量 --》 推荐

   ```
   # 对于bash用户，编辑 ~/.bashrc
   echo 'export CMAKE_INSTALL_PREFIX="$HOME/flutter_apps"' >> ~/.bashrc
   source ~/.bashrc
   
   # 对于zsh用户，编辑 ~/.zshrc
   echo 'export CMAKE_INSTALL_PREFIX="$HOME/flutter_apps"' >> ~/.zshrc
   source ~/.zshrc
   
   ```

   