# 扫描用户输入的目录下第一层子文件夹名称 使用这个名称在那个文件夹下创建文件夹名称.txt空文件
import json
import os
import shutil

# 全局变量
target_directory = "F:\APP\Steam\steamapps\workshop\content\\431960"

# 失败的
errlist=[]
# 修改文件夹名称
def rename_folder(old_name, new_name):
    try:
        # 检查旧文件夹是否存在
        if not os.path.exists(old_name):
            print(f"错误：文件夹 '{old_name}' 不存在")
            return False
        
        # 检查新名称是否已存在
        if os.path.exists(new_name):
            print(f"错误：目标名称 '{new_name}' 已存在")
            return False
        
        # 执行重命名（支持跨磁盘）
        shutil.move(old_name, new_name)
        print(f"成功将 '{old_name}' 重命名为 '{new_name}'")
        return True
    
    except Exception as e:
        print(f"重命名失败: {str(e)}")
        errlist.append(e)
        return False


# 解析json函数
def baseAnalysis_project_json(filePath):
    # 1. 打开并解析 JSON 文件
    try:
        with open(filePath, 'r', encoding='utf-8') as file:  # 确保使用正确的编码
            data = json.load(file)  # 解析 JSON 数据到 Python 字典/列表
            return data

        # 2. 打印整个数据结构（可选）
        # print("解析成功！JSON 内容:")
        # print(json.dumps(data, indent=4, ensure_ascii=False))  # 美化输出


    except FileNotFoundError:
        print("错误: 文件 '"+filePath+"' 不存在！")
    except json.JSONDecodeError:
        print("错误: 文件内容不是有效的 JSON 格式！")
    except Exception as e:
        print(f"未知错误: {str(e)}")

def scan_first_level_subfolders(root_dir):
    first_level_folders = []
    
    if not os.path.isdir(root_dir):
        print(f"错误：'{root_dir}' 不是有效目录")
        return first_level_folders
    
    try:
        # 使用更高效的os.scandir
        with os.scandir(root_dir) as entries:
            for entry in entries:
                if entry.is_dir():
                    first_level_folders.append(os.path.abspath(entry.path))
    except PermissionError:
        print(f"警告：无权限访问目录 '{root_dir}'")
    except Exception as e:
        print(f"扫描目录时出错: {e}")
    
    return first_level_folders

# 批量解析project.json并返回
def analysis_project_json(target_directory):
    projects=[]
    originalDirectorys= scan_first_level_subfolders(target_directory)
    for i,folder in enumerate(originalDirectorys,0):
        list01=folder+"\\project.json"
        last_ten_chars = os.path.dirname(folder)

        newnaem=last_ten_chars+"\\"+baseAnalysis_project_json(list01)['title']
        rename_folder(folder,newnaem)

# 示例用法
if __name__ == "__main__":
    # 替换为你要扫描的目录路径
    # target_directory = input("请输入文件夹路径: ").strip()
    
    # 检查目录是否存在
    if not os.path.exists(target_directory):
        print(f"错误：目录 '{target_directory}' 不存在")
    elif not os.path.isdir(target_directory):
        print(f"错误：'{target_directory}' 不是目录")
    else:
        # 获取所有子文件夹
        folders = scan_first_level_subfolders(target_directory)
        last_ten_chars = [path[-10:].ljust(10) for path in folders]
        # 打印结果
        print(f"在 '{target_directory}' 中找到 {len(folders)} 个子文件夹：")
        # for i, folder in enumerate(folders, 0):
        #              # 使用这些名称在这个文件夹下创建名为文件夹名称.txt的空文件
        #     newfilename=folders[i]+"\\"+last_ten_chars[i]+".txt"
        #     with open(newfilename, "w") as file:
        #         print(newfilename)
        #         pass
        # 解析 project.json 
        # 获取里面的title参数的值 
        # 用这个值作为他的上层文件夹名称
        data= analysis_project_json(target_directory)
        print("======================================================")
        print("======================================================")
        for i,lis in errlist:
            print(lis)
    # 自动处理文件关闭，防止资源泄露

   