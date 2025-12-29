# mihomo 离线包目录（Kylin）

本目录用于存放 `setup_mihomo_tun.yml` 所需的离线文件。

至少需要提供 **一个** mihomo 二进制（按架构自动选择）：

- x86_64：
  - `mihomo-linux-amd64`（推荐）
  - 或 `mihomo-amd64`
  - 或 `mihomo`（兼容旧命名）
- aarch64：
  - `mihomo-linux-arm64`（推荐）
  - 或 `mihomo-arm64`
  - 或 `mihomo`（不推荐，容易放错架构）

可选文件（存在则会复制到安装目录）：

- `Country.mmdb`
- `geoip.dat`
- `geosite.dat`
- `cache.db`

如需使用 `mihomo_config_mode=bundle`，还需要提供：

- `config.yaml`

