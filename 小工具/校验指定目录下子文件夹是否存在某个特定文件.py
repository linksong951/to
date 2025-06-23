import os
target_directory = "F:\Games\FS"

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

# 校验文件是否存在


if __name__ == "__main__":
    lists=scan_first_level_subfolders(target_directory)
    for i,lis in enumerate(lists,0):
        list01=lis+"\\解压码：FS"
        if(os.path.exists(list01)):
            # print(list01+"文件存在") 
            pass
        else:
            print(list01+"文件不存在") 

