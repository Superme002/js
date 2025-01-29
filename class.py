import tkinter as tk
from tkinter import messagebox
import time

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("计数器")
        self.root.geometry("400x200")  # 设置窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小
        
        # 初始化计数器
        self.counts = {"合格": 0, "不合格": 0, "休息": 0}
        self.history = []  # 用于存储历史记录，方便撤销操作
        
        # 创建按钮和标签
        self.create_buttons()
        self.create_labels()
        
        # 定时器相关
        self.last_update_time = time.time()
    
    def create_buttons(self):
        # 创建按钮并设置样式
        button_style = {"font": ("Arial", 14), "width": 10, "height": 2}
        
        # 合格按钮
        self.qualified_button = tk.Button(self.root, text="合格", command=lambda: self.increment("合格"), **button_style)
        self.qualified_button.grid(row=0, column=0, padx=10, pady=10)
        
        # 不合格按钮
        self.unqualified_button = tk.Button(self.root, text="不合格", command=lambda: self.increment("不合格"), **button_style)
        self.unqualified_button.grid(row=0, column=1, padx=10, pady=10)
        
        # 休息按钮
        self.rest_button = tk.Button(self.root, text="休息", command=lambda: self.increment("休息"), **button_style)
        self.rest_button.grid(row=0, column=2, padx=10, pady=10)
        
        # 撤销按钮
        self.undo_button = tk.Button(self.root, text="撤销", command=self.undo, **button_style)
        self.undo_button.grid(row=1, column=1, padx=10, pady=10)
    
    def create_labels(self):
        # 创建显示标签并设置样式
        label_style = {"font": ("Arial", 14)}
        
        # 显示计数结果
        self.qualified_label = tk.Label(self.root, text="合格: 0", **label_style)
        self.qualified_label.grid(row=2, column=0)
        
        self.unqualified_label = tk.Label(self.root, text="不合格: 0", **label_style)
        self.unqualified_label.grid(row=2, column=1)
        
        self.rest_label = tk.Label(self.root, text="休息: 0", **label_style)
        self.rest_label.grid(row=2, column=2)
    
    def increment(self, option):
        # 更新计数器
        self.counts[option] += 1
        self.update_labels()
        
        # 保存历史记录
        current_time = time.time()
        self.history.append((current_time, option))
        self.last_update_time = current_time
    
    def update_labels(self):
        # 更新显示标签
        self.qualified_label.config(text=f"合格: {self.counts['合格']}")
        self.unqualified_label.config(text=f"不合格: {self.counts['不合格']}")
        self.rest_label.config(text=f"休息: {self.counts['休息']}")
    
    def undo(self):
        # 撤销操作，恢复到20秒前的状态
        current_time = time.time()
        target_time = current_time - 20  # 20秒前的时间
        
        # 找到20秒内的最后一次操作
        while self.history and self.history[-1][0] > target_time:
            _, option = self.history.pop()
            self.counts[option] -= 1
            if self.counts[option] < 0:
                self.counts[option] = 0  # 防止计数器出现负值
        
        self.update_labels()
        if not self.history:
            messagebox.showinfo("提示", "没有更多可撤销的操作！")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()