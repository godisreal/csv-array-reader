
import os, sys

#from tkinter import ttk
#from tkinter import *

# Version Check
if sys.version_info[0] == 3: # Python 3
    from tkinter import *
    #from tkinter import ttk
    from tkinter.ttk import Notebook
    from tkinter.ttk import Treeview
    from tkinter.ttk import Button
    import tkinter.filedialog as tkf
else:
    # Python 2
    from Tkinter import *
    from ttk import Notebook
    from ttk import Treeview
    from ttk import Entry
    import tkFileDialog as tkf

root = Tk() 

left_frame = Frame(root, width=200, height=600, bg="grey")
left_frame.pack_propagate(0)
        
right_frame = Frame(root, width=400, height=600, bg="lightgrey")
right_frame.pack_propagate(0)

columns = ("agent", "iniPosX", "iniPosY")

treeview = Treeview(root, height=18, show="headings", columns=columns)  #Table

treeview.column("agent", width=100, anchor='center')
treeview.column("iniPosX", width=300, anchor='center')
treeview.column("iniPosY", width=300, anchor='center')

treeview.heading("agent", text="agent") # Show table headings
treeview.heading("iniPosX", text="iniPosX")
treeview.heading("iniPosY", text="iniPosY")

treeview.pack(side=LEFT, fill=BOTH)

name = ['agent1','agent2','new_agent']
pos = ['10.13.71.223','10.25.61.186','10.25.11.163']
vel = ['10.13.71.223','10.25.61.186','10.25.11.163']

for i in range(len(name)): #

    treeview.insert('', i, values=(name[i], pos[i], vel[i]))

def treeview_sort_column(tv, col, reverse):  # Treeview

    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # sort method
    # rearrange items in sorted positions

    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

def set_cell_value(event): # double click to edit the item

    for item in treeview.selection():

        #item = I001
        item_text = treeview.item(item, "values")
        #print(item_text[0:2])  # Output the column number selected by users

    column= treeview.identify_column(event.x)# column

    row = treeview.identify_row(event.y)  # row

    cn = int(str(column).replace('#',''))

    rn = int(str(row).replace('I',''))

    entryedit = Text(root,width=10+(cn-1)*16,height = 1)

    entryedit.place(x=16+(cn-1)*130, y=6+rn*20)

    def saveedit():

        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))

        entryedit.destroy()

        okb.destroy()

    okb = Button(root, text='OK', width=4, command=saveedit)

    okb.place(x=90+(cn-1)*242,y=2+rn*20)

def newrow():

    name.append('NoName')
    pos.append('IP')
    vel.append('Trial')

    treeview.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))

    treeview.update()

    newb.place(x=120, y=(len(name)-1)*20+45)

    newb.update()

treeview.bind('<Double-1>', set_cell_value) # Double click to edit items

newb = Button(root, text='New Agent', width=20, command=newrow)

newb.place(x=120,y=(len(name)-1)*20+45)

for col in columns:  # bind function: enable sorting in table headings

    treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))

'''

1.遍历表格

t = treeview.get_children()

for i in t:

    print(treeview.item(i,'values'))

2.绑定单击离开事件

def treeviewClick(event):  # 单击

    for item in tree.selection():

        item_text = tree.item(item, "values")

        print(item_text[0:2])  # 输出所选行的第一列的值

tree.bind('<ButtonRelease-1>', treeviewClick) 

------------------------------

鼠标左键单击按下1/Button-1/ButtonPress-1 

鼠标左键单击松开ButtonRelease-1 

鼠标右键单击3 

鼠标左键双击Double-1/Double-Button-1 

鼠标右键双击Double-3 

鼠标滚轮单击2 

鼠标滚轮双击Double-2 

鼠标移动B1-Motion 

鼠标移动到区域Enter 

鼠标离开区域Leave 

获得键盘焦点FocusIn 

失去键盘焦点FocusOut 

键盘事件Key 

回车键Return 

控件尺寸变Configure

------------------------------

'''

root.mainloop()
