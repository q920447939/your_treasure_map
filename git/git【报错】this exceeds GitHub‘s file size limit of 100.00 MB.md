# git【报错】this exceeds GitHub‘s file size limit of 100.00 MB

1.下载并安装 Git 命令行扩展。下载并安装后，运行以下命令为您的用户帐户设置 Git LFS：

```bash
git lfs install
```


2.在您要使用 Git LFS 的每个 Git 存储库中，选择您希望 Git LFS 管理的文件类型（或直接编辑您的 .gitattributes）。您可以随时配置其他文件扩展名

```bash
git lfs migrate import --include="*.pdf"
git lfs track "*.pdf"

#*.pdf 修改成 需要的配置超过100M的后缀名称

```



3.现在确保 .gitattributes 被跟踪：

```bash
git add .gitattributes
```


​	请注意，定义 Git LFS 应该跟踪的文件类型本身不会将任何预先存在的文件转换为 Git LFS，例如其他分支上的文件或您之前的提交历史记录中的文件。为此，请使用git lfs migrate[1]命令，该命令具有一系列选项，旨在适应各种潜在用例。



4.随后正常推送即可