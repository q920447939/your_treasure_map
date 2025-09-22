# github使用工作流

github可以做很多事情,比如修改文件,编译等

本次的需求是运行某个`python`文件,然后更新`README.md`内容



1. 在 GitHub 上的存储库中，创建 `.github/workflows` 目录中名为 `github-actions-auto-update-readme.yml` 的工作流文件。

2. 编辑文件`github-actions-auto-update-readme.yml` 

   ```
   name: Run Python and Update Markdown
   on:
     push:
       branches: [ main ]
     schedule:
       - cron: '0 0 * * *'  # 每天运行
   
   jobs:
     update-markdown:
       runs-on: ubuntu-latest
       permissions:
         contents: write  # 关键：给予写入权限 注意,要添加这个内容,否则 工作流没有权限提交
       steps:
         - name: Checkout repository
           uses: actions/checkout@v4
   
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.9'
   
   
         - name: Run Python script
           run: |
             python markdown.py
   
   
         - name: Commit and push changes
           run: |
             git config --local user.email "action@github.com"
             git config --local user.name "GitHub Action"
             git add .
             git commit -m "Update markdown file" || exit 0
             git push
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # 使用自动生成的 token 注意,要添加这个内容,否则 工作流没有权限提交
   ```

   

3. 提交该文件到`github`

4. 在项目目录中,找到`actions`,就可以看到工作流执行的情况

