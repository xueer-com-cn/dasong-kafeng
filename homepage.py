import streamlit as st

st.write("这是一个音乐播放器")
st.code('''
import tkinter as tk
from tkinter import filedialog
import pygame
import time
 
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title('Music Player')
        self.root.geometry('400x200')
 
        pygame.init()
        pygame.mixer.init()
 
        self.status = 'stopped'
        self.current_time = 0
        self.total_time = 0
 
        self.load_button = tk.Button(self.root, text='加载音乐', width=10, command=self.load_music)
        self.load_button.pack()
 
        self.play_button = tk.Button(self.root, text='播放', width=10, command=self.play_music)
        self.play_button.pack()
 
        self.pause_button = tk.Button(self.root, text='暂停/继续', width=10, command=self.toggle)
        self.pause_button.pack()
 
        self.time_label = tk.Label(self.root, text='00:00 / 00:00')
        self.time_label.pack()
 
        self.file_label = tk.Label(self.root, text='加载的音乐文件: ')
        self.file_label.pack()
 
        self.update_time()
 
    def load_music(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3; *.wav; *.ogg")])
        pygame.mixer.music.load(self.file_path)
        self.total_time = pygame.mixer.Sound(self.file_path).get_length()
        self.file_label.config(text='加载的音乐文件: ' + self.file_path)
 
    def play_music(self):
        if self.status != 'playing':
            pygame.mixer.music.play()
            self.status = 'playing'
 
    def toggle(self):
        if self.status == 'paused':
            pygame.mixer.music.unpause()
            self.status = 'playing'
        elif self.status == 'playing':
            pygame.mixer.music.pause()
            self.status = 'paused'
 
    def update_time(self):
        if self.status == 'playing':
            self.current_time = pygame.mixer.music.get_pos() // 1000
            mins, secs = divmod(self.current_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            total_mins, total_secs = divmod(int(self.total_time), 60)
            total_timeformat = '{:02d}:{:02d}'.format(total_mins, total_secs)
            self.time_label.config(text='{} / {}'.format(timeformat, total_timeformat))
        self.root.after(1000, self.update_time)
 
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
''', language='python')


st.write('这是一个计算器')
st.code('''import tkinter as tk
 
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
window.mainloop()
''',language='python')

st.write('以下代码可以实现控件移动')
st.code('''
import tkinter as tk
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
''',language='python')


 

 
