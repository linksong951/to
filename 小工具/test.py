import json

# 1. 打开并解析 JSON 文件
try:
    with open('F:\\APP\\Steam\\steamapps\\workshop\\content\\431960\\3277503474\\project.json', 'r', encoding='utf-8') as file:  # 确保使用正确的编码
        data = json.load(file)  # 解析 JSON 数据到 Python 字典/列表
        a=data['title']

    # 2. 打印整个数据结构（可选）
    print("解析成功！JSON 内容:")
    print(json.dumps(data, indent=4, ensure_ascii=False))  # 美化输出


except FileNotFoundError:
    print("错误: 文件 'nnn.json' 不存在！")
except json.JSONDecodeError:
    print("错误: 文件内容不是有效的 JSON 格式！")
except Exception as e:
    print(f"未知错误: {str(e)}")