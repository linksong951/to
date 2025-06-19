import os
import re

def remove_shortcut_text(directory):
    """
    删除指定目录下.lnk文件名中的" - 快捷方式"字样
    :param directory: 要处理的目录路径
    """
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查是否为.lnk文件
        if filename.lower().endswith('.lnk'):
            # 定义要删除的文本模式（支持空格变体）
            pattern = r'\s*-\s*快捷方式'
            
            # 删除匹配的文本并保留原扩展名
            new_name = re.sub(pattern, '', filename, flags=re.IGNORECASE)
            
            # 仅当文件名实际发生变化时才重命名
            if new_name != filename:
                try:
                    # 构建完整的文件路径
                    old_path = os.path.join(directory, filename)
                    new_path = os.path.join(directory, new_name)
                    
                    # 执行重命名操作
                    os.rename(old_path, new_path)
                    print(f"重命名成功: {filename} -> {new_name}")
                except Exception as e:
                    print(f"处理文件 {filename} 时出错: {str(e)}")

# 使用示例 - 替换为你的目标目录
target_directory = r"F:\Games\Go\Level 3"

# target_directory =input("请输入文件夹路径: ").strip()
remove_shortcut_text(target_directory)