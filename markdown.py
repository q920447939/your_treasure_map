import os

# 指定要读取的文件夹路径
folder_path = "."

def generate_markdown_content():
    header = """# your_treasure_map
This is a collection of all kinds of software engineering records, you will always find what you need

"""
    return header + "\n\n\n\n"

def generate_markdown_toc(folder_path):
    def traverse_folder(path, level=0):
        toc = []
        folder_name = os.path.basename(path)
        has_md_files = False

        # 获取目录下所有文件和文件夹，并按名称排序
        items = sorted(os.listdir(path))
        
        for item in items:
            item_path = os.path.join(path, item)
            # 忽略 .git 目录和 README.md
            if ".git" in item_path or item == "README.md":
                continue
                
            if os.path.isdir(item_path):
                subtree = traverse_folder(item_path, level + 1)
                if subtree:
                    has_md_files = True
                    indent = "  " * level
                    toc.append(f"{indent}- {item}")
                    toc.extend(subtree)
            elif item.endswith(".md"):
                has_md_files = True
                indent = "  " * level
                relative_path = os.path.relpath(item_path, folder_path)
                relative_path = "./" + relative_path.replace("\\", "/").replace(" ", "%20")
                file_name = os.path.splitext(item)[0]
                toc.append(f"{indent}- [{file_name}]({relative_path})")

        if level == 0 and not has_md_files:
            return []
        elif has_md_files:
            return toc
        else:
            return []

    return "\n".join(traverse_folder(folder_path))

# 生成内容并写入 README.md
content = generate_markdown_content() + generate_markdown_toc(folder_path)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
