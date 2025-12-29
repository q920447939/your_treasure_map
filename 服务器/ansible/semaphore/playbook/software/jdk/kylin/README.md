# Kylin Linux Advanced Server (V10) 安装 OpenJDK 21

该目录为麒麟操作系统专用的 OpenJDK 21 安装 playbook，与上层目录原有 Ubuntu playbook 相互独立（不会修改原有安装逻辑）。

## 使用方式

- 修改变量文件：`kylin/openjdk_vars.yml`
- 执行安装：
  - `ansible-playbook -i kylin/openjdk_inventory.ini kylin/openjdk_install.yml`

## 架构选择

默认 `jdk_arch: auto` 会根据目标机 `uname -m/ansible_architecture` 自动选择：

- `x86_64`
- `aarch64`

也可以在 `kylin/openjdk_vars.yml` 中显式指定 `jdk_arch: x86_64` 或 `jdk_arch: aarch64`。

## 是否删除系统自带 JDK

默认不删除系统自带 JDK（例如 `/usr/bin/java` 指向的 OpenJDK 1.8）：通过 `alternatives/update-alternatives` 设置默认版本即可，风险更小。

如确需删除，请在 `kylin/openjdk_vars.yml` 中开启：

- `remove_system_jdk: true`
- `remove_system_jdk_confirm: yes`
- 推荐：显式指定 `remove_system_jdk_packages`（要删除的 RPM 包名）
- 或谨慎开启：`remove_system_jdk_auto_detect: true`（自动探测并删除 JDK 1.8 相关包）
