import os
from PIL import Image
import sys

def convert_gif_to_png(root_dir):
    """转换第一层子文件夹中的preview.gif为preview.png"""
    for entry in os.scandir(root_dir):
        if entry.is_dir():
            gif_path = os.path.join(entry.path, "preview.gif")
            png_path = os.path.join(entry.path, "preview.png")
            
            if os.path.exists(gif_path):
                try:
                    # 打开GIF图片并转换格式
                    with Image.open(gif_path) as img:
                        # 如果GIF是多帧，只取第一帧
                        if img.is_animated:
                            img.seek(0)
                        
                        # 转换为RGB模式（移除透明度）
                        rgb_img = img.convert('RGB')
                        rgb_img.save(png_path, "PNG")
                    
                    print(f"转换成功: {gif_path} -> {png_path}")
                except Exception as e:
                    print(f"处理 {gif_path} 时出错: {str(e)}")
            else:
                print(f"跳过: {entry.name} 中没有找到 preview.gif")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    target_dir = input("请输入文件夹路径: ").strip()
    
    # 验证路径是否存在
    if not os.path.isdir(target_dir):
        print("错误: 指定的路径不存在或不是文件夹")
        sys.exit(1)
    
    convert_gif_to_png(target_dir)
    print("所有转换操作完成！")