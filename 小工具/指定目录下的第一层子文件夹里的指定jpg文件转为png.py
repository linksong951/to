import os
from PIL import Image
import sys

def convert_jpg_to_png(root_dir):
    """转换第一层子文件夹中的preview.jpg为preview.png"""
    for entry in os.scandir(root_dir):
        if entry.is_dir():
            jpg_path = os.path.join(entry.path, "preview.jpg")
            png_path = os.path.join(entry.path, "preview.png")
            
            if os.path.exists(jpg_path):
                try:
                    # 打开图片并转换格式
                    with Image.open(jpg_path) as img:
                        img.save(png_path, "PNG")
                    print(f"转换成功: {jpg_path} -> {png_path}")
                except Exception as e:
                    print(f"处理 {jpg_path} 时出错: {str(e)}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    target_dir = input("请输入文件夹路径: ").strip()
    
    # 验证路径是否存在
    if not os.path.isdir(target_dir):
        print("错误: 指定的路径不存在或不是文件夹")
        sys.exit(1)
    
    convert_jpg_to_png(target_dir)
    print("所有转换操作完成！")