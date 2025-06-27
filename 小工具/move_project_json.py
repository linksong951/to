import os
import shutil

def main():
    # 获取用户输入
    base_dir = input("请输入要扫描的根目录：")
    target_file = input("请输入要查找的文件名（如'n'）：")
    new_name = input("请输入新的完整文件名：")

    # 验证目录是否存在
    if not os.path.isdir(base_dir):
        print(f"错误：目录 '{base_dir}' 不存在！")
        return

    # 遍历第一层子文件夹
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        
        # 只处理文件夹
        if not os.path.isdir(folder_path):
            continue
            
        # 检查目标文件是否存在
        src_path = os.path.join(folder_path, target_file)
        if not os.path.isfile(src_path):
            print(f"跳过 '{folder}'：未找到文件 '{target_file}'")
            continue
        
        # 获取当前目录下的第一个文件夹
        first_subfolder = None
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                first_subfolder = item
                break
                
        if not first_subfolder:
            print(f"跳过 '{folder}'：没有找到子文件夹")
            continue
            
        # 构造目标路径
        dest_folder = os.path.join(folder_path, first_subfolder)
        dest_path = os.path.join(dest_folder, new_name)
        
        # 确保目标文件夹存在
        os.makedirs(dest_folder, exist_ok=True)
        
        try:
            # 移动并重命名文件
            shutil.move(src_path, dest_path)
            print(f"成功：已将文件移动到 '{first_subfolder}/{new_name}'")
        except Exception as e:
            print(f"移动文件失败：{str(e)}")

if __name__ == "__main__":
    main()