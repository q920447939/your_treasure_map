# git已提交到暂存区的文件如何移除

以` .idea`文件夹为例

1. 先从暂存区移除 .idea

   ```
   git rm -r --cached .idea
   
   #-r 参数用于递归删除整个目录
   ```

2. 在 .gitignore 文件中添加:

   ```
   .idea/
   ```

3. 提交这个更改:

   ```
   git add .gitignore
   git commit -m "ignore .idea folder"
   ```

   

