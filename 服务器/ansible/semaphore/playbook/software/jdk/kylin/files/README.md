# 手动安装包放置目录

当 `kylin/openjdk_vars.yml` 中设置 `install_method: manual` 且 `manual_install.source: local` 时：

- 请把安装包放到本目录，例如：
  - `kylin/files/openjdk-21_linux-x64_bin.tar.gz`
  - `kylin/files/openjdk-21_linux-aarch64_bin.tar.gz`

然后执行：

- `ansible-playbook -i kylin/openjdk_inventory.ini kylin/openjdk_install.yml`

