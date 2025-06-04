using System;
using System.IO;

class Program
{
    static void Main()
    {
        // 计算文件路径（项目根目录）
        string baseDir = AppDomain.CurrentDomain.BaseDirectory;
        string filePath = Path.Combine(baseDir, "未知男号.txt");
        
        Console.WriteLine($"生成文件到: {filePath}");
        Console.WriteLine("开始生成...");

        try
        {
            using (StreamWriter writer = new StreamWriter(filePath))
            {
                // 生成所有6位数字组合
                for (int i = 0; i <= 999999; i++)
                {
                    // 格式化为6位数字（不足前面补零）
                    writer.WriteLine($"27{i.ToString("D6")}56");
                    
                    // 每10000个数字显示一次进度
                    if (i % 100000 == 0)
                    {
                        Console.WriteLine($"已生成: {i} / 1000000");
                    }
                }
            }
            
            Console.WriteLine("生成完成！共1,000,000个组合");
            Console.WriteLine($"文件大小: {new FileInfo(filePath).Length / 1024} KB");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"出错: {ex.Message}");
        }
        
    }
}