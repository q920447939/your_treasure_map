# 将python打包为exe程序

1. 安装 PyInstaller

   ```
   pip install pyinstaller
   ```

2. 创建虚拟环境（一般都会自动创建虚拟环境)

   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

3. 生成 .spec 配置文件(类似于配置文件)

   ```
   #确保当前目录下有 main.py 文件
   pyinstaller --name=MyApp main.py
   
   完成后会生成 MyApp.spec 配置文件
   ```

4. 打包

   ```
   pyinstaller    MyApp.spec
   ```

5. 查看exe结果

   一般在当前目录下的`dist`文件夹下