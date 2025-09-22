# Git Pre-commit Hook 配置说明

Git pre-commit hook 是在执行 `git commit` 命令时自动触发的脚本，可以用来执行代码检查、自动格式化等任务。

## Windows 环境配置

### 1. 创建 pre-commit.bat

在 `.git/hooks/` 目录下创建 `pre-commit.bat` 文件：

```batch
@echo off
python markdown.py
git add README.md
```

### 2. 文件说明

- `@echo off`: 关闭命令回显
- `python markdown.py`: 运行 Python 脚本
- `git add README.md`: 将更新后的文件添加到暂存区

## Linux/Mac 环境配置

### 1. 创建 pre-commit

在 `.git/hooks/` 目录下创建 `pre-commit` 文件：

```bash
#!/bin/sh
python markdown.py
git add README.md
```

### 2. 添加执行权限

```bash
chmod +x .git/hooks/pre-commit
```

## 工作流程

1. 当执行 `git commit` 时
2. Git 自动检查 `.git/hooks` 目录
3. 找到并执行 pre-commit 脚本
4. 脚本执行成功后继续提交
5. 脚本执行失败则终止提交

## 常见问题

1. Windows 环境注意事项：
   - 确保 Python 已添加到系统环境变量
   - ~~使用相对路径 `../../` 访问项目根目录~~(目前已移除相对路径,不加也可以)
   - 文件扩展名必须是 `.bat`

2. Linux/Mac 环境注意事项：
   - 必须添加执行权限
   - 必须包含 shebang (`#!/bin/sh`)
   - 使用 Unix 换行符 (LF)

## 禁用 Hook

如果临时不需要执行 hook：

```bash
git commit -m "message" --no-verify
```

## 调试技巧

1. 手动执行脚本测试：
   ```bash
   # Windows
   .git/hooks/pre-commit.bat
   
   # Linux/Mac
   .git/hooks/pre-commit
   ```

2. 添加调试输出：
   ```batch
   @echo off
   echo Starting pre-commit hook...
   python markdown.py
   echo Updating README.md...
   git add README.md
   echo Pre-commit hook completed.
   ```

## 最佳实践

1. 保持脚本简单，执行时间短
2. 添加适当的错误处理
3. 提供清晰的输出信息
4. 使用相对路径确保跨平台兼容
5. 将 hook 脚本纳入版本控制 