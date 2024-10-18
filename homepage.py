import streamlit as st

tab1,tab2,tab3 = st.tabs(["美丽开封","电脑硬件与网络技术","编程"])

with tab1:
    st.header("一头连着宋代历史，一头连着人间烟火！这儿就是开封")
    st.write('''中国十大传世名画之一的《清明上河图》，生动记录了中国十二世纪北宋都城东京（又称汴京，今河南开封）的城市面貌和当时社会各阶层人民的生活状况，是北宋时期都城东京当年繁荣的见证，也是北宋城市经济情况的写照。''')
    st.write('''作为首批国家历史文化名城的开封，迄今已有4100余年的建城史和建都史，素有“八朝古都”之称，孕育了上承汉唐、下启明清、影响深远的“宋文化”。开封是世界上唯一一座城市中轴线从未变动的都城，城摞城遗址在世界考古史和都城史上少有，宋朝都城东京城更是当时世界第一大城市。开封至今仍然有一种旧都气息，深深烙印在这个城市的血脉当中。进入开封市，首先映入眼帘就是宋代风格的建筑，这种风格贯穿整个开封市，闲逛于街头巷尾之间，仿佛穿越回“宋代”。''')
    st.image("./1.png",width=800)
    st.write('''“这里的文旅资源和景区，大多都是依托宋代文化、宋代风格建筑，也可以说，宋文化已经融入到每个景区的建设发展之中。
                开封耳熟能详的旅游景区众多，如开封清明上河园、龙亭公园、天波杨府、铁塔公园、开封府、万岁山武侠城、中国翰园碑林等，景区内十足的烟火气。
                每天500多场节目让游客真正体验到一步江湖，千幕传奇。大型实景演出、经典武侠、民俗绝活、歌舞演绎更是令广大游客应接不暇。''')
    st.write('''“美食”在开封是永远离不开的话题，“玩在河南，食在开封”也吸引众多网红到开封打卡。开封灌汤包子、鲤鱼焙面、桶子鸡、沙家牛肉、开封套四宝、炸八块、双麻火烧、炒红薯泥、花生糕、黄焖鱼、羊肉炕馍、炒凉粉、杏仁茶、四味烩菜……每个开封美食，都成为游客们津津乐道的话题。美食旅游是满足人民美好生活新需求的重要载体，也成为促进旅游产业高质量发展的新动能。一到夜晚，鼓楼夜市、西司夜市、书店街夜市、小宋城等美食街游人如织，人头攒动。第一楼、邢家锅贴等老字号饭店更是一座难求。唇齿留香的小笼包、纯正的宫廷杏仁茶、炒红薯泥、独具特色的炒凉粉、甜而不腻的花生糕等等，这些以前的“大宋皇家”美食如今纷纷呈现在游客面前。''')
    st.image("./5830.png",width=800)

with tab2:
    st.header("组本地局域网")
    st.text('''
方法一：使用网线直接连接
1、准备一根网线，长度不宜过长（建议不要超过80米，否则信号会衰减），确保两台电脑相邻或距离较近。
2、将网线的一头插入一台电脑的网口，另一头插入另一台电脑的网口。
3、打开电脑，进入网络设置。在Windows系统中，可以点击桌面下方的网络图标，选择“网络设置”。
4、在网络设置中，找到“以太网（本地连接）”选项，并选择“网络和共享中心”。
5、在“网络和共享中心”中，找到“以太网链接”并点击，打开状态窗口。
6、点击“属性”，找到并双击“Internet 协议版本4（TCP/IPv4）”。
7、在属性窗口中，选择“使用下面的IP地址”，然后为两台电脑分别设置相同的IP地址段（确保最后一位数字不同），以及相同的子网掩码。例如，一台电脑可以设置IP地址为192.168.1.100，另一台为192.168.1.101，子网掩码都为255.255.255.0。
8、点击确定，完成设置。此时，两台电脑已经建立了局域网，可以进行文件共享、设备共享等操作。
方法二：使用交换机连接
1、准备一个带有8口的交换机（带宽最好在100兆或以上）。
2、按照电脑的摆放位置，制作若干条标准网线（推荐选择568B规格）。
3、将网线的一头连接电脑，另一头连接交换机。
4、重复上述步骤，将其他电脑也连接到交换机上。
5、打开电脑，进入网络设置。同样地，在Windows系统中，可以点击桌面下方的网络图标，选择“网络设置”。
7、确保所有电脑的IP地址都在同一网段内，并且子网掩码相同。
8、完成设置后，所有连接到交换机的电脑就已经建立了局域网。
            ''')
    st.header("文件共享")
    st.text('''
一、使用局域网共享
如果两台电脑都连接到同一个局域网（例如家庭或办公室的无线网络），那么您可以使用局域网共享的功能，将一台电脑上的文件夹或驱动器共享给另一台电脑，从而实现文件传输。具体操作步骤如下：
1、打开网络和共享中心，选择‘高级共享设置’，启用‘网络发现’和‘文件和打印机共享’。
WIN+X打开计算机管理，在‘本地用户和组’-‘用户’可以新建用户。如果‘网络’中无法看到自己，查看服务‘FDResPub’是否启动。
2、在要共享文件的电脑上，打开文件资源管理器，找到要共享的文件夹或驱动器，右键单击，选择“属性”。
3、在弹出的窗口中，切换到“共享”选项卡，点击“高级共享”按钮。
4、在“高级共享”窗口中，勾选“共享此文件夹”选项，可以修改共享名称，也可以设置共享权限，例如只读或完全控制。点击“确定”按钮，完成共享设置。
5、在要接收文件的电脑上，打开文件资源管理器，点击“网络”，找到共享文件的电脑的名称，双击打开，就可以看到共享的文件夹或驱动器，可以直接复制或移动文件。
6、在文件传输完成后，建议您取消共享，以防止他人访问您的文件。取消共享的方法是在共享文件的电脑上，重复步骤1和2，然后取消勾选“共享此文件夹”选项，点击“确定”按钮。
二、使用远程桌面连接
如果两台电脑不在同一个局域网，但都能连接到互联网，那么您可以使用远程桌面连接的功能，将一台电脑的桌面显示在另一台电脑上，从而实现文件传输。具体操作步骤如下：
1、在要共享文件的电脑上，打开“控制面板”，选择“系统和安全”，然后选择“允许远程访问”。
2、在弹出的窗口中，切换到“远程”选项卡，勾选“允许运行任意版本的远程桌面的计算机连接”选项，点击“选择用户”按钮，添加允许访问的用户账户，点击“确定”按钮，完成远程设置。
3、在要接收文件的电脑上，打开“开始”菜单，搜索“远程桌面连接”，打开该程序。
4、在“远程桌面连接”窗口中，输入共享文件的电脑的IP地址或计算机名称，点击“连接”按钮，输入用户名和密码，建立远程连接。
5、在远程桌面上，打开文件资源管理器，找到要传输的文件，右键单击，选择“复制”。
6、在本地桌面上，打开文件资源管理器，找到要保存的位置，右键单击，选择“粘贴”，就可以将文件从远程桌面复制到本地桌面。
7、在文件传输完成后，建议您断开远程连接，以防止他人访问您的电脑。断开远程连接的方法是在远程桌面上，点击“开始”菜单，选择“断开连接”。

            ''')

with tab3:
    st.header("python的GUI库tkinter常用知识点")
    st.text('''
标准模块tkinter
1.label
from tkinter import *
root=Tk()
from PIL import ImageTk,Image
var = StringVar()
text_label = Label(root,textvariable=var,justify=LEFT)
im = Image.open(filename).resize((width, height))
im = ImageTk.PhotoImage(im)
img_label = Label(root, text='欢迎检测', image=im)
img_label.place(x=2, y=2, width=100, height=40)

2.button
from tkinter import *
main_win = Tk()
main_win.geometry(f'{800}x{800}')
png = PhotoImage(file='button.png')
text = '渔道的按钮'
fg='blue'
Button(main_win, compound='bottom', image=png, text=text, fg=fg).pack()
Button(main_win, compound='top', image=png, text=text, fg=fg).pack()
Button(main_win, compound='center', image=png, text=text, fg=fg).pack()
Button(main_win, compound='left', image=png, text=text, fg=fg).pack()
Button(main_win, compound='right', image=png, text=text, fg=fg).pack()
3.notebook
from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('300x180')
notebook=ttk.Notebook(root)
frameone=Frame(root)
frametwo=Frame(root)
notebook.add(frameone,text='选项卡1')
label=Label(frameone,text='我是选项卡1的便签')
label.pack()
notebook.add(frametwo,text='选项卡2')
label2=Label(frametwo,text='我是选项卡2的便签')
label2.pack(side=BOTTOM)
notebook.place(x=0,y=0,width=300,height=180)
root.mainloop()

4.treeview
from tkinter import ttk
from tkinter import *
root = Tk()
tree = ttk.Treeview(root,show='headings',columns=('col1','col2','col3'))
tree.column('col1', width=100, anchor='center')
tree.column('col2', width=100, anchor='center')
tree.column('col3', width=100, anchor='center')
tree.heading('col1', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')
def onDBClick(event):
    item = tree.selection()[0]
    print("you clicked on ", tree.item(item, "values"))
for i in range(10):
    tree.insert('',i,values=('a'+str(i),'b'+str(i),'c'+str(i)))
tree.bind("<Double-1>", onDBClick)
tree.pack()
root.mainloop()

5.组合框
from tkinter import *
from tkinter import ttk
root=Tk()
root.title('lianxi')
root.geometry('600x500')
def showya():
    print(var.get())
def showdd(event):
    lable['text']=var.get()
def showaa(event):
    print(var.get())    
var=StringVar()
combobox=ttk.Combobox(root,textvariable=var)
combobox['value']=('aa','bb','cc','dd','gg','ff','hh')
combobox.current(0)
combobox.bind('<<ComboboxSelected>>',showdd)
combobox.pack()

lable=Label(root,text='lable')
lable.bind('<Button-1>',showaa)
lable.pack()
button=Button(root,text='button',command=showya)
button.pack()
root.mainloop()

6进度条
模拟下载
def show():
    # 设置进度条的目前值
    progressbar['value'] = 0
    # 设置进度条的最大值
    progressbar['maximum'] = maxbyte
    # 调用loading方法
    loading()
def loading():
    # 改变变量属性
    global byte
    # 每次运行500B
    byte += 500
    # 设置指针
    progressbar['value'] = byte
    if byte < maxbyte:
        # 经过100ms后再次调用loading方法
        progressbar.after(100, loading)
root = tkinter.Tk()
root.geometry('150x120')
# 设置下载初值
byte = 0
# 设置下载最大值
maxbyte = 10000
progressbar = tkinter.ttk.Progressbar(root)
progressbar.pack(pady=20)
button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)
root.mainloop()

7.listbox
from tkinter import *
def printList(event):
    print(lb.get(lb.curselection())) #输出当前选中项的值
root = Tk()
lb = Listbox(root)
lb.bind('<Double-Button-1>', printList)
for i in range(10):
    lb.insert(END, str(i * 100))
lb.pack()
root.mainloop()

8.scrollbar
from tkinter import *
root=Tk()
root.geometry('400x300')
f=Frame(root)
sb=Scrollbar(f)
sb.pack(side=RIGHT,fill=Y)
lb=Listbox(f,yscrollcommand=sb.set)
lb.pack(side=LEFT)
sb.config(command=lb.yview)

9.text
from tkinter import *
root = Tk()
text1 = Text(root, width=50, height=40)
text1.pack()
text1.insert(INSERT, 'starting writing\n')
 
photo = PhotoImage(file='g.gif')
def show():
    text1.insert(END, '\nshow a new photo')
    # 插入图片在文本框
    text1.image_create(END, image=photo) 
button = Button(text1, text='Click Me!', command=show)
# 插入按钮在文本框
text1.window_create(INSERT, window=button)
root.mainloop()
插入字符串 获取信息 删除信息
from tkinter import *
text.insert('end', 'A') # 插入到末尾
text.insert('insert', 'B') # 插入到光标处
# 插入指定位置(x.y)，行x从1开始，列y从0开始
# 如果x.y之前没内容，则添加到前面
text.insert(1.2, 'C')
# 获取信息
msg = text.get(1.0, 1.6) # 获取1行1列至1行7列
msg = text.get(1.0, '1.end') # 获取1行1列至1行末尾
msg = text.get(1.4, '2.end') # 获取1行5列至2行末尾
msg = text.get(1.2, 'end') # 获取1行3列至内容结尾
#删除信息
text.delete(1.0, 1.6) # 删除1行1列至1行7列
text.delete(1.0, '1.end') # 删除1行1列至1行末尾
text.delete(1.4, '2.end') # 删除1行5列至2行末尾
text.delete(1.2, 'end') # 删除1行3列至内容结尾

10.单选框
import tkinter as tk
def select():
    dict = {1:'C语言中文网',2:'菜鸟教程',3:'W3SCHOOL',4:'微学苑'}
    strings = '您选择了' + dict.get(v.get()) + '，祝您学习愉快'
    lable.config(text = strings)
window = tk.Tk()
window.geometry('400x180')
lable = tk.Label(window,font=('微软雅黑', '15','bold'),fg='#43CD80')
lable.pack(side ='bottom')
site = [('C语言中文网',1),
        ('菜鸟教程',2),
        ('W3SCHOOL',3),
        ('微学苑',4)]
v = tk.IntVar()
for name, num in site:
    radio_button = tk.Radiobutton(window,text = name,
                 variable = v,value =num,command =
                 select,indicatoron = False)
    radio_button.pack(anchor ='w')
window.mainloop()

11.复选框
import tkinter
top = tkinter.Tk()
CheckVar1 = tkinter.IntVar(master=top)
CheckVar2 = tkinter.IntVar(master=top)
cb1 = tkinter.Checkbutton(top, text = "A", variable=CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
cb2 = tkinter.Checkbutton(top, text = "B", variable=CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
cb1.pack()
cb2.pack()
 
def print_data():
    print("%d  %d"%(CheckVar1.get(),CheckVar2.get()))

b1 = tkinter.Button(top,text = "test",command=print_data,height=5, width = 20)
b1.pack()
top.mainloop()

12.entry
import tkinter as tk
import time
root = tk.Tk()
root.geometry('450x150')
def gettime():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    # 每隔 1s 调用一次 gettime()函数来获取时间
    root.after(1000, gettime)

dstr = tk.StringVar()
lb = tk.Label(root,textvariable=dstr,font=("楷书",45))
lb.pack()
gettime()
root.mainloop()

13.scale
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('600x400')
l = tk.Label(window, bg='yellow', width=100, text='empty')
l.pack()
def print_selection(v):
    # 这里的Scale会传过来一个value,用v接收
    l.config(text='you have selected ' + v)
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=False, tickinterval=3, resolution=0.01,
             command=print_selection)
# from_=5,to=10 -> 从5到10, orient=tk.HORIZONTAL -> 横向, showvalue -> 条上是否显示数字,
# tickinterval 数字间隔, resolution 数字精度
s.pack()
window.mainloop() 

14.messagebox
import tkinter.messagebox
tkinter.messagebox.askokcancel("FishC Demo",'确定or取消？')
tkinter.messagebox.askquestion("FishC Demo","你确定吗？")
tkinter.messagebox.askretrycancel("FishC Demo","启动失败，重试？")
tkinter.messagebox.askyesno("FishC Demo","是否继续?")
tkinter.messagebox.showerror("FishC Demo","出错啦！")
tkinter.messagebox.showinfo("FishC Demo","2019元旦快乐")
tkinter.messagebox.showwarning("FishC Demo","请注意！")
参数icon 指定对话框显示的图标
可以指定的值有: ERROR、INFO、QUESTION或WARNING.
            ''')
