import streamlit as st

st.header("一些经典案例")
tab1,tab2,tab3,tab4 = st.tabs(["计算器","音乐播放器","按钮拖放","小游戏"])

with tab1:
    st.code("""import tkinter as tk

# 定义全局变量，用于保存当前输入的数字和运算符
num1 = ''
num2 = ''
operator = ''
 
# 定义一个函数，用于将数字添加到显示屏上
def add_digit(digit):
    global num1, num2, operator
    if operator == '':
        num1 += str(digit)
        label.config(text=num1)
    else:
        num2 += str(digit)
        label.config(text=num2)
 
# 定义一个函数，用于将运算符添加到显示屏上
def add_operator(op):
    global num1, num2, operator
    if num1 != '' and num2 == '':
        operator = op
        label.config(text=num1 + operator)
 
# 定义一个函数，用于计算结果
def calculate():
    global num1, num2, operator
    if num1 != '' and num2 != '' and operator != '':
        num1 = str(eval(num1 + operator + num2))
        num2 = ''
        operator = ''
        label.config(text=num1)
 
# 创建一个名为 window 的窗口对象
window = tk.Tk()
 
# 设置窗口标题
window.title('Calculator')
#window.geometry("800x600")
 
# 创建一个标签对象，用于显示计算结果
label = tk.Label(window, text='0', font=('Arial', 20), width=12, height=2, bg='white', anchor='e')
 
# 将标签对象放置在窗口中央
label.grid(row=0, column=0, columnspan=4, padx=2, pady=2)
 
# 创建数字按钮并绑定回调函数
for i in range(1, 10):
    btn = tk.Button(window, text=str(i), font=('Arial', 20), width=2, height=1, command=lambda digit=i:add_digit(digit))
    btn.grid(row=(i-1)//3+1, column=(i-1)%3, padx=2, pady=2)
 
# 创建加、减、乘、除、等于按钮并绑定回调函数
btn_add = tk.Button(window, text='+', font=('Arial', 20), width=3, height=2, command=lambda:add_operator('+'))
btn_sub = tk.Button(window, text='-', font=('Arial', 20), width=3, height=2, command=lambda:add_operator('-'))
btn_mul = tk.Button(window, text='*', font=('Arial', 20), width=3, height=2, command=lambda:add_operator('*'))
btn_div = tk.Button(window, text='/', font=('Arial', 20), width=3, height=2, command=lambda:add_operator('/'))
btn_eq = tk.Button(window, text='=', font=('Arial', 20), width=3, height=2, command=calculate)
 
# 将按钮对象放置在窗口中间
btn_add.grid(row=1, column=3, padx=5, pady=5)
btn_sub.grid(row=2, column=3, padx=5, pady=5)
btn_mul.grid(row=3, column=3, padx=5, pady=5)
btn_div.grid(row=4, column=3, padx=5, pady=5)
btn_eq.grid(row=4, column=2, padx=5, pady=5)
 
# 创建清空按钮并绑定回调函数
btn_clear = tk.Button(window, text='C', font=('Arial', 20), width=3, height=2, command=lambda:clear())
btn_clear.grid(row=4, column=0, padx=5, pady=5)
 
# 定义一个函数，用于清空显示屏和缓存的数字和运算符
def clear():
    global num1, num2, operator
    num1 = ''
    num2 = ''
    operator = ''
    label.config(text='0')
 
# 进入主消息循环
window.mainloop()""",language='python')
with tab2:
    st.code("""import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("音乐播放器")
        self.root.geometry("480x380")
        # 初始化pygame mixer
        pygame.mixer.init()
        # 播放器和停止按钮
        self.play_button = tk.Button(root, text="播放", command=self.play_music)
        self.play_button.place(x=50,y=10)
        self.stop_button = tk.Button(root, text="停止", command=self.stop_music)
        self.stop_button.place(x=150,y=10)
        # 列表框显示音乐文件
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.place(x=50,y=40,width=300,height=240)
        # 加载音乐文件按钮
        self.load_button = tk.Button(root, text="载入音乐文件夹", command=self.load_music_folder)
        self.load_button.place(x=50,y=300)
        # 当前播放的音乐文件
        self.current_music = None
    def load_music_folder(self):
        # 弹出对话框选择文件夹
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.listbox.delete(0, tk.END)  # 清空列表
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.mp3', '.wav', '.ogg')):
                    self.listbox.insert(tk.END, os.path.join(folder_path, filename))
    def play_music(self):
        # 检查是否有选中的音乐
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.current_music = self.listbox.get(index)
            try:
                pygame.mixer.music.load(self.current_music)
                pygame.mixer.music.play()
            except pygame.error as e:
                messagebox.showerror("错误", f"无法播放音乐: {e}")
    def stop_music(self):
        pygame.mixer.music.stop()
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
    """,language="python")
with tab3:
    st.code("""import tkinter as tk
def mousedown(event):
    widget=event.widget
    widget.startx=event.x # 开始拖动时, 记录控件位置
    widget.starty=event.y
def drag(event):
    widget=event.widget
    dx=event.x-widget.startx
    dy=event.y-widget.starty
    # winfo_x(),winfo_y() 方法获取控件的坐标
    if isinstance(widget,tk.Wm):
        widget.geometry("+%d+%d"%(widget.winfo_x()+dx,
                                  widget.winfo_y()+dy))
    else:
        widget.place(x=widget.winfo_x()+dx,
                     y=widget.winfo_y()+dy)
def draggable(tkwidget):
    # tkwidget为一个控件(Widget)或一个窗口(Wm)
    tkwidget.bind("<Button-1>",mousedown,add='+')
    tkwidget.bind("<B1-Motion>",drag,add='+')

root=tk.Tk()
root.title("Test")
button=tk.Button(root,text="Drag!")
button.place(width=80,height=30)
draggable(button)
root.mainloop()
           """,language="python")
with tab4:
    st.code("""import tkinter as tk
import random

def on_enter(event):
    a = random.randint(1, 600)
    b = random.randint(1, 600)
    #当鼠标进入按钮区域时调用
    button.place(x=a, y=b)  # 移动到新的位置

def on_leave(event):
    #当鼠标离开按钮区域时调用
    button.place(x=100, y=100)  # 返回到原始位置

root = tk.Tk()
root.geometry("400x400")  # 设置窗口大小

button = tk.Button(root, text="Move Me!")
button.place(x=100, y=100)  # 初始位置

# 绑定事件
button.bind("<Enter>", on_enter)
#button.bind("<Leave>", on_leave)

root.mainloop()
           """,language="python")

st.write("我的QQ:2752978583")
