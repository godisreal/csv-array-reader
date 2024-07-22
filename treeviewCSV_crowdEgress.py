
import os, sys
from data_func import *
import numpy as np

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


def file_open(event=None):
    fnameCSV = tkf.askopenfilename(filetypes=(("csv files", "*.csv"),("All files", "*.*"))) #,initialdir=self.currentdir)
        #temp=self.fname_EVAC.split('/') 
    temp=os.path.basename(fnameCSV)
    currentdir = os.path.dirname(fnameCSV)
    #lb_csv.config(text = "The input csv file selected: "+str(fnameCSV)+"\n")
    #self.textInformation.insert(END, 'fname_EVAC:   '+self.fname_EVAC)
    print('fname', fnameCSV)
    #setStatusStr("Simulation not yet started!")
    #textInformation.insert(END, '\n'+'EVAC Input File Selected:   '+self.fname_EVAC+'\n')
    
    agents, walls, exits, doors = readCrowdEgressCSV(fnameCSV, debug=True, marginTitle=1)
    
    
    #for i in range(np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
    #    treeviewA.heading(columns[i], text=agents[0][i])
    for i in range(1, len(agents)): #
        treeviewA.insert('', i, values=(agents[i][0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8]))

def file_save(event=None):
    pass
    
root = Tk() 

menubar = Menu(root, bg="lightgrey", fg="black")

'''
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
file_menu.add_command(label="Open", command=file_open, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=file_save, accelerator="Ctrl+S")
menubar.add_cascade(label="File", menu=file_menu)

add_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
add_menu.add_command(label="Add Item", command=newrow, accelerator="Ctrl+O")
menubar.add_cascade(label="Add", menu=add_menu)

delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Item", command=file_open, accelerator="Ctrl+O")
menubar.add_cascade(label="Delete", menu=delete_menu)
'''

notebook = Notebook(root)      
notebook.pack(side=TOP, padx=2, pady=2)
        
frameAgent = Frame(root)
frameWall = Frame(root)
frameDoor = Frame(root)
frameExit = Frame(root)

notebook.add(frameAgent,text="Agent")
notebook.add(frameWall,text="Wall")
notebook.add(frameDoor,text="Exit")
notebook.add(frameExit,text="Door")

#left_frame = Frame(root, width=200, height=600, bg="grey")
#left_frame.pack_propagate(0)
        
#right_frame = Frame(root, width=400, height=600, bg="lightgrey")
#right_frame.pack_propagate(0)

columns = ("agent", "iniPosX", "iniPosY", "iniVx", "iniVy", "timelag", "tpre", "p", "pMode", "p2", "talkRange", "aType", "inComp", "tpreMode")

scrollbarAy = Scrollbar(frameAgent, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAy.pack(side=RIGHT, fill=Y)

scrollbarAx = Scrollbar(frameAgent, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAx.pack(side=BOTTOM, fill=X)

treeviewA = Treeview(frameAgent, height=18, show="headings", columns=columns)  #Table
scrollbarAy.config(command=treeviewA.yview)
scrollbarAx.config(command=treeviewA.xview)

treeviewA.column("agent", width=100, anchor='center')
treeviewA.column("iniPosX", width=70, anchor='center')
treeviewA.column("iniPosY", width=70, anchor='center')
treeviewA.column("iniVx", width=70, anchor='center')
treeviewA.column("iniVy", width=70, anchor='center')
treeviewA.column("timelag", width=70, anchor='center')
treeviewA.column("tpre", width=70, anchor='center')
treeviewA.column("p", width=70, anchor='center')
treeviewA.column("pMode", width=70, anchor='center')
treeviewA.column("p2", width=70, anchor='center')
treeviewA.column("talkRange", width=70, anchor='center')
treeviewA.column("aType", width=70, anchor='center')
treeviewA.column("inComp", width=70, anchor='center')
treeviewA.column("tpreMode", width=70, anchor='center')


#treeviewA.heading("agent", text="agent") # Show table headings
#treeviewA.heading("iniPosX", text="iniPosX")
#treeviewA.heading("iniPosY", text="iniPosY")
#treeviewA.heading("iniVx", text='iniVx')
#treeviewA.heading("iniVy", text='iniVy')
#treeviewA.heading("timelag", text='timelag')
#treeviewA.heading("tpre", text='tpre')
#treeviewA.heading("p", text='p')
#treeviewA.heading("pMode", text='pMode')
#treeviewA.heading("p2", text='p2')
#treeviewA.heading("talkRange", text='talkRange')
#treeviewA.heading("aType", text='aType')
#treeviewA.heading("inComp", text='inComp')
#treeviewA.heading("tpreMode", text='tpreMode')

treeviewA.pack(side=LEFT, fill=BOTH)

#scrollbar = Scrollbar(treeviewA, orient="vertical", command=treeviewA.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
#scrollbar.config(command=treeviewA.yview)

name = ['agent1','agent2','new_agent']
pos = ['10.13.71.223','10.25.61.186','10.25.11.163']
vel = ['10.13.71.223','10.25.61.186','10.25.11.163']


def treeview_sort_column(tv, col, reverse):  # Treeview

    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # sort method
    # rearrange items in sorted positions

    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

def set_cell_value(event): # double click to edit the item

    for item in treeviewA.selection():

        #item = I001
        item_text = treeviewA.item(item, "values")
        #print(item_text[0:2])  # Output the column number selected by users

    column= treeviewA.identify_column(event.x)# column

    row = treeviewA.identify_row(event.y)  # row

    cn = int(str(column).replace('#',''))

    rn = int(str(row).replace('I',''))

    entryedit = Text(frameAgent,width=10+(cn-1)*16,height = 1)

    entryedit.place(x=16+(cn-1)*130, y=6+rn*20)

    def saveedit():

        treeviewA.set(item, column=column, value=entryedit.get(0.0, "end"))

        entryedit.destroy()

        okb.destroy()

    okb = Button(frameAgent, text='OK', width=4, command=saveedit)

    okb.place(x=90+(cn-1)*242,y=2+rn*20)
    

def newrow():

    name.append('NoName')
    pos.append('IP')
    vel.append('Trial')

    treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    treeviewA.update()

    #newb.place(x=120, y=20) #y=(len(name)-1)*20+45)
    #newb.update()

treeviewA.bind('<Double-1>', set_cell_value) # Double click to edit items

#newb = Button(frameAgent, text='New Agent', width=20, command=newrow)
#newb.place(x=120,y=20 ) #(len(name)-1)*20+45)

for col in columns:  # bind function: enable sorting in table headings

    treeviewA.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeviewA, _col, False))

# Configure the menubar
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
file_menu.add_command(label="Open", command=file_open, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=file_save, accelerator="Ctrl+S")
menubar.add_cascade(label="File", menu=file_menu)

add_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
add_menu.add_command(label="Add Item", command=newrow, accelerator="Ctrl+A")
menubar.add_cascade(label="Add", menu=add_menu)

delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Item", command=file_open, accelerator="Ctrl+D")
menubar.add_cascade(label="Delete", menu=delete_menu)

'''

1.遍历表格

t = treeviewA.get_children()

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
