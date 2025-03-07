import os

# 指定要读取的文件夹路径
folder_path = "."

def generate_markdown_toc(folder_path):

    def traverse_folder(path, level=0):
        toc = []
        folder_name = os.path.basename(path)
        has_md_files = False

        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
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
                relative_path = "./" + relative_path.replace("\\", "/")
                file_name = os.path.splitext(item)[0]
                toc.append(f"{indent}- [{file_name}]({relative_path})")

        if level == 0 and not has_md_files:
            return []
        elif has_md_files:
            return toc
        else:
            return []

    return "\n".join(traverse_folder(folder_path))

# 调用函数并打印生成的目录
markdown_toc = generate_markdown_toc(folder_path)
print(markdown_toc)