
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


agents=None
walls=None
exits=None
doors=None

def file_open(event=None):
    
    global agents, walls, exits, doors
    
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
    
    for i in range(15): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA.heading(columns[i+1], text=agents[0][i])
    for i in range(1, len(agents)): #
        try:
            treeviewA.insert('', i, values=(i, agents[i][0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8], agents[i][9], agents[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(13): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewW.heading(columns[i+1], text=walls[0][i])
    for i in range(1, len(walls)): #
        try:
            treeviewW.insert('', i, values=(i, walls[i][0], walls[i][1], walls[i][2], walls[i][3], walls[i][4], walls[i][5],  walls[i][6], walls[i][7], walls[i][8]))
        except:
            treeviewW.insert('', i, values=(i))
            
    for i in range(13): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE.heading(columns[i+1], text=exits[0][i])
    for i in range(1, len(exits)): #
        try: 
            treeviewE.insert('', i, values=(i, exits[i][0], exits[i][1], exits[i][2], exits[i][3], exits[i][4], exits[i][5],  exits[i][6], exits[i][7], exits[i][8]))
        except:
            treeviewE.insert('', i, values=(i))

def file_save(event=None):
    pass
    
root = Tk() 

file_name_var = StringVar()
file_name_label = Label(root, textvar=openFileName, fg="black", bg="white", font=(None, 12))
file_name_label.pack(side=TOP, expand=1, fill=X)

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
frameExit = Frame(root)
frameDoor = Frame(root)

notebook.add(frameAgent,text="Agent")
notebook.add(frameWall,text="Wall")
notebook.add(frameExit,text="Exit")
notebook.add(frameDoor,text="Door")

#left_frame = Frame(root, width=200, height=600, bg="grey")
#left_frame.pack_propagate(0)
        
#right_frame = Frame(root, width=400, height=600, bg="lightgrey")
#right_frame.pack_propagate(0)

#columns = ("agent", "iniPosX", "iniPosY", "iniVx", "iniVy", "timelag", "tpre", "p", "pMode", "p2", "talkRange", "aType", "inComp", "tpreMode")

columns = ("/", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q")

scrollbarAy = Scrollbar(frameAgent, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAy.pack(side=RIGHT, fill=Y)

scrollbarAx = Scrollbar(frameAgent, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAx.pack(side=BOTTOM, fill=X)

treeviewA = Treeview(frameAgent, height=18, show="headings", columns=columns)  #Table
scrollbarAy.config(command=treeviewA.yview)
scrollbarAx.config(command=treeviewA.xview)

treeviewA.column("/", width=30, anchor='center')
treeviewA.column("A", width=70, anchor='center')
treeviewA.column("B", width=70, anchor='center')
treeviewA.column("C", width=70, anchor='center')
treeviewA.column("D", width=70, anchor='center')
treeviewA.column("E", width=70, anchor='center')
treeviewA.column("F", width=70, anchor='center')
treeviewA.column("G", width=70, anchor='center')
treeviewA.column("H", width=70, anchor='center')
treeviewA.column("I", width=70, anchor='center')
treeviewA.column("J", width=70, anchor='center')
treeviewA.column("K", width=70, anchor='center')
treeviewA.column("L", width=70, anchor='center')
treeviewA.column("M", width=70, anchor='center')
treeviewA.column("N", width=70, anchor='center')
treeviewA.column("O", width=70, anchor='center')
treeviewA.column("P", width=70, anchor='center')
treeviewA.column("Q", width=70, anchor='center')

'''
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
'''
treeviewA.pack(side=LEFT, fill=BOTH)

#scrollbar = Scrollbar(treeviewA, orient="vertical", command=treeviewA.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
#scrollbar.config(command=treeviewA.yview)

scrollbarWy = Scrollbar(frameWall, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarWy.pack(side=RIGHT, fill=Y)

scrollbarWx = Scrollbar(frameWall, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarWx.pack(side=BOTTOM, fill=X)

treeviewW = Treeview(frameWall, height=18, show="headings", columns=columns)  #Table
scrollbarWy.config(command=treeviewW.yview)
scrollbarWx.config(command=treeviewW.xview)

treeviewW.column("/", width=30, anchor='center')
treeviewW.column("A", width=100, anchor='center')
treeviewW.column("B", width=70, anchor='center')
treeviewW.column("C", width=70, anchor='center')
treeviewW.column("D", width=70, anchor='center')
treeviewW.column("E", width=70, anchor='center')
treeviewW.column("F", width=70, anchor='center')
treeviewW.column("G", width=70, anchor='center')
treeviewW.column("H", width=70, anchor='center')
treeviewW.column("I", width=70, anchor='center')
treeviewW.column("J", width=70, anchor='center')
treeviewW.column("K", width=70, anchor='center')
treeviewW.column("L", width=70, anchor='center')
treeviewW.column("M", width=70, anchor='center')
treeviewW.column("N", width=70, anchor='center')
treeviewW.column("O", width=70, anchor='center')
treeviewW.column("P", width=70, anchor='center')
treeviewW.column("Q", width=70, anchor='center')
treeviewW.pack(side=LEFT, fill=BOTH)

### Frame of Exit
scrollbarEy = Scrollbar(frameExit, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarEy.pack(side=RIGHT, fill=Y)

scrollbarEx = Scrollbar(frameExit, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarEx.pack(side=BOTTOM, fill=X)

treeviewE = Treeview(frameExit, height=18, show="headings", columns=columns)  #Table
scrollbarEy.config(command=treeviewE.yview)
scrollbarEx.config(command=treeviewE.xview)

treeviewE.column("/", width=30, anchor='center')
treeviewE.column("A", width=100, anchor='center')
treeviewE.column("B", width=70, anchor='center')
treeviewE.column("C", width=70, anchor='center')
treeviewE.column("D", width=70, anchor='center')
treeviewE.column("E", width=70, anchor='center')
treeviewE.column("F", width=70, anchor='center')
treeviewE.column("G", width=70, anchor='center')
treeviewE.column("H", width=70, anchor='center')
treeviewE.column("I", width=70, anchor='center')
treeviewE.column("J", width=70, anchor='center')
treeviewE.column("K", width=70, anchor='center')
treeviewE.column("L", width=70, anchor='center')
treeviewE.column("M", width=70, anchor='center')
treeviewE.column("N", width=70, anchor='center')
treeviewE.column("O", width=70, anchor='center')
treeviewE.column("P", width=70, anchor='center')
treeviewE.column("Q", width=70, anchor='center')
treeviewE.pack(side=LEFT, fill=BOTH)

def treeview_sort_column(tv, col, reverse):  # Treeview

    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # sort method
    # rearrange items in sorted positions

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 

def set_cell_value_A(event): # double click to edit the item

    for item in treeviewA.selection():

        #item = I001
        item_text = treeviewA.item(item, "values")
        #print(item_text[0:2])  # Output the column number selected by users

    column= treeviewA.identify_column(event.x)# column
    row = treeviewA.identify_row(event.y)  # row

    cn = int(str(column).replace('#',''))
    rn = int(str(row).replace('I',''), base=16)
    
    print("cn:", column)
    print("rn:", row)

    #entryedit = Text(root,width=10+(cn-1)*16,height = 1)
    entryedit = Text(root, width=26, height = 2)
    #entryedit = Entry(root,width=10)
    entryedit.insert(END, 'agent'+str(rn)+'|'+agents[0][cn-2]+' = '+str(item_text[cn-1]))
    #entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    entryedit.pack()
    #lb= Label(root, text = str(rn)+columns[cn-1])
    #lb.pack()

    def saveedit():

        treeviewA.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    okb = Button(root, text='agent'+str(rn)+'|'+agents[0][cn-2]+': <OK>', width=26, command=saveedit)

    okb.pack() #place(x=90+(cn-1)*242,y=2+rn*20)
    

def newrow():
    name.append('NoName')
    pos.append('IP')
    vel.append('Trial')
    treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    treeviewA.update()

    #newb.place(x=120, y=20) #y=(len(name)-1)*20+45)
    #newb.update()

treeviewA.bind('<Double-1>', set_cell_value_A) # Double click to edit items
root.bind("<Control-o>", file_open)
root.bind("<Control-s>", file_save)

#newb = Button(frameAgent, text='New Agent', width=20, command=newrow)
#newb.place(x=120,y=20 ) #(len(name)-1)*20+45)
for col in columns:  # bind function: enable sorting in table headings
    treeviewA.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeviewA, _col, False))

#######################
# Configure the menubar

menubar = Menu(root, bg="lightgrey", fg="black")
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

root.mainloop()
