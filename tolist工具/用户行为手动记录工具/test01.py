import tkinter as tk
from tkinter import messagebox
import datetime
import os
# from PIL import Image, ImageTk

class BehaviorTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("行为手动记录器")
        self.root.geometry("250x200+100+100")
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.overrideredirect(True)  # 无边框窗口
        self.root.config(bg="#2c3e50")
        
        # 设置窗口透明度
        self.root.attributes("-alpha", 0.65)
        
        # 记录拖动初始位置
        self.x = 0
        self.y = 0
        
        # 初始化状态
        self.tracking = False
        self.start_time = None
        self.behavior_name = ""
        
        # 创建界面
        self.create_widgets()
        
        # 绑定拖动事件
        self.header.bind("<ButtonPress-1>", self.start_move)
        self.header.bind("<B1-Motion>", self.do_move)
        
        # 创建数据库文件（如果不存在）
        self.db_file = "behavior_records.txt"
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                f.write("行为名称,开始时间,结束时间,持续时间\n")
    
    def create_widgets(self):
        # 自定义标题栏
        self.header = tk.Frame(self.root, bg="#3498db", height=30)
        self.header.pack(fill=tk.X)
        
        # 标题
        title_label = tk.Label(self.header, text="行为时间记录器", bg="#3498db", fg="white", 
                             font=("Arial", 10, "bold"))
        title_label.pack(side=tk.LEFT, padx=10)
        
        # 关闭按钮
        close_btn = tk.Label(self.header, text="×", bg="#3498db", fg="white", 
                           font=("Arial", 14), cursor="hand2")
        close_btn.pack(side=tk.RIGHT, padx=10)
        close_btn.bind("<Button-1>", lambda e: self.root.destroy())
        
        # 主体内容
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 行为名称输入框
        tk.Label(main_frame, text="行为名称:", bg="#2c3e50", fg="white", 
                font=("Arial", 9)).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.entry = tk.Entry(main_frame, width=20, font=("Arial", 10))
        self.entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        self.entry.focus()
        
        # 开始/结束按钮
        self.action_btn = tk.Button(main_frame, text="开始记录", command=self.toggle_tracking,
                                   bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                                   width=10, relief="flat")
        self.action_btn.grid(row=2, column=0, pady=5)
        
        # 查看记录按钮
        tk.Button(main_frame, text="查看记录", command=self.show_records,
                 bg="#27ae60", fg="white", font=("Arial", 10), width=10, relief="flat"
                 ).grid(row=2, column=1, padx=(10, 0), pady=5)
        
        # 状态标签
        self.status = tk.Label(main_frame, text="状态: 等待开始", bg="#2c3e50", fg="#ecf0f1",
                              font=("Arial", 9))
        self.status.grid(row=3, column=0, columnspan=2, pady=(15, 0))
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
    
    def toggle_tracking(self):
        if not self.tracking:
            # 开始记录
            self.behavior_name = self.entry.get().strip()
            if not self.behavior_name:
                messagebox.showwarning("输入错误", "请输入行为名称！")
                return
                
            self.start_time = datetime.datetime.now()
            self.tracking = True
            self.action_btn.config(text="结束记录", bg="#e74c3c")
            self.status.config(text=f"状态: 正在记录 [{self.behavior_name}]")
            self.entry.config(state="disabled")
            
            # 显示开始时间
            start_str = self.start_time.strftime("%H:%M:%S")
            messagebox.showinfo("开始记录", f"已开始记录: {self.behavior_name}\n开始时间: {start_str}")
        else:
            # 结束记录
            end_time = datetime.datetime.now()
            self.tracking = False
            self.action_btn.config(text="开始记录", bg="#3498db")
            self.status.config(text="状态: 记录完成")
            self.entry.config(state="normal")
            self.entry.delete(0, tk.END)
            
            # 计算持续时间
            duration = end_time - self.start_time
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            
            # 保存到数据库
            self.save_to_db(end_time, duration_str)
            
            # 显示结束信息
            end_str = end_time.strftime("%H:%M:%S")
            messagebox.showinfo("记录完成", 
                               f"行为: {self.behavior_name}\n"
                               f"开始时间: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                               f"结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                               f"持续时间: {duration_str}")
    
    def save_to_db(self, end_time, duration_str):
        with open(self.db_file, "a") as f:
            f.write(f"{self.behavior_name},"
                    f"{self.start_time.strftime('%Y-%m-%d %H:%M:%S')},"
                    f"{end_time.strftime('%Y-%m-%d %H:%M:%S')},"
                    f"{duration_str}\n")
    
    def show_records(self):
        try:
            with open(self.db_file, "r") as f:
                records = f.readlines()
            
            if len(records) <= 1:  # 只有标题行
                messagebox.showinfo("行为记录", "还没有任何记录！")
                return
                
            # 创建记录窗口
            records_window = tk.Toplevel(self.root)
            records_window.title("行为记录")
            records_window.geometry("600x400+200+200")
            records_window.attributes('-topmost', True)
            
            # 添加滚动条
            scrollbar = tk.Scrollbar(records_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # 添加文本框显示记录
            text = tk.Text(records_window, wrap=tk.WORD, yscrollcommand=scrollbar.set,
                          font=("Consolas", 10))
            text.pack(fill=tk.BOTH, expand=True)
            scrollbar.config(command=text.yview)
            
            # 设置列宽
            text.tag_configure("header", foreground="blue", font=("Arial", 10, "bold"))
            text.tag_configure("row", font=("Arial", 10))
            
            # 添加标题
            text.insert(tk.END, records[0], "header")
            
            # 添加记录（从最新到最旧）
            for record in reversed(records[1:]):
                text.insert(tk.END, record, "row")
                
            text.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror("错误", f"无法读取记录文件: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BehaviorTrackerApp(root)
    root.mainloop()