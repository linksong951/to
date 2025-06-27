import os
import sys
import tempfile
from PIL import Image
import subprocess

def convert_jpg_to_win_ico(jpg_path, ico_path):
    """创建完全兼容Windows的ICO文件"""
    try:
        with Image.open(jpg_path) as img:
            # 创建正方形画布
            width, height = img.size
            size = min(width, height)
            left = (width - size) // 2
            top = (height - size) // 2
            right = left + size
            bottom = top + size
            cropped = img.crop((left, top, right, bottom))
            
            # 生成PNG格式的临时文件
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_png:
                png_temp_path = temp_png.name
                cropped.save(png_temp_path, "PNG")
                
            # 使用ImageMagick转换（最佳兼容性）
            if convert_with_imagemagick(png_temp_path, ico_path):
                os.unlink(png_temp_path)  # 删除临时PNG
                print(f"转换成功: {jpg_path} -> {ico_path}")
                return True
            
            # 回退方法：使用Pillow生成256×256
            resized_img = cropped.resize((256, 256), Image.LANCZOS)
            resized_img.save(ico_path, format="ICO")
            print(f"使用兼容模式生成256×256 ICO: {ico_path}")
            return True
            
    except Exception as e:
        print(f"转换失败: {jpg_path} - 错误: {str(e)}")
        return False

def convert_with_imagemagick(png_path, ico_path):
    """使用ImageMagick转换（确保兼容性）"""
    try:
        # 检查ImageMagick是否安装
        result = subprocess.run(["convert", "--version"], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
        if result.returncode != 0:
            return False
            
        # 转换命令
        cmd = [
            "convert",
            png_path,
            "-resize", "512x512",
            "-define", "icon:auto-resize=256,128,96,64,48,32,16",
            ico_path
        ]
        
        # 执行转换
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True
            
        print(f"ImageMagick转换错误: {result.stderr}")
        return False
    except Exception as e:
        print(f"ImageMagick调用失败: {str(e)}")
        return False

def process_directory(root_dir):
    """处理目录及其所有子目录"""
    not_found = []
    
    for foldername, subfolders, filenames in os.walk(root_dir):
        jpg_path = os.path.join(foldername, "preview.jpg")
        
        if os.path.isfile(jpg_path):
            ico_path = os.path.join(foldername, "preview.ico")
            convert_jpg_to_win_ico(jpg_path, ico_path)
        else:
            # 检查子目录是否有preview.jpg
            found_in_sub = False
            for sub in subfolders:
                sub_jpg = os.path.join(foldername, sub, "preview.jpg")
                if os.path.isfile(sub_jpg):
                    found_in_sub = True
                    ico_path = os.path.join(foldername, sub, "preview.ico")
                    convert_jpg_to_win_ico(sub_jpg, ico_path)
            
            if not found_in_sub:
                not_found.append(foldername)
    
    # 输出未找到preview.jpg的目录
    if not_found:
        print("\n以下目录未找到 preview.jpg:")
        for path in not_found:
            print(f"  - {path}")

def install_imagemagick():
    """提示用户安装ImageMagick"""
    print("\n建议安装ImageMagick以获得最佳兼容性：")
    print("1. 访问 https://imagemagick.org/script/download.php")
    print("2. 下载Windows版本安装程序")
    print("3. 安装时勾选'Add application directory to your system path'")
    print("4. 安装完成后重新运行此脚本")

if __name__ == "__main__":
    # 检查Pillow库
    try:
        from PIL import Image
    except ImportError:
        print("错误: 需要安装Pillow库")
        print("请运行: pip install Pillow")
        sys.exit(1)
    
    # 获取用户输入
    target_dir = input("请输入文件夹路径: ").strip()
    
    # 验证路径
    if not os.path.isdir(target_dir):
        print(f"错误: 路径不存在或不是目录 - {target_dir}")
        sys.exit(1)
    
    # 提示安装ImageMagick
    if not convert_with_imagemagick:  # 总是提示
        install_imagemagick()
    
    # 开始处理
    process_directory(target_dir)
    print("\n处理完成!")