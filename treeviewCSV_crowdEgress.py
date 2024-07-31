
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
agent2exit=None
agentgroup=None
walls=None
exits=None
doors=None
exit2door=None

openFileName = None

def file_new(event=None):
    global agents, agent2exit, agentgroup, walls, exits, doors, exit2door
    
    agents=[['agent', 'iniX', 'iniY', 'iniVx', 'iniVy', 'timelag', 'tpre', 'p', 'pMode', 'p2', 'talkRange', 'talkProb', 'inComp', 'aType']]
    agent2exit=[]
    agentgroup=[]
    walls=[]
    exits=[]
    doors=[]
    exit2door=[]
       
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA2E.delete(*treeviewA2E.get_children())
    treeviewAG.delete(*treeviewAG.get_children())
    treeviewE.delete(*treeviewE.get_children())
    treeviewD.delete(*treeviewD.get_children())
    treeviewW.delete(*treeviewW.get_children())
    treeviewE2D.delete(*treeviewE2D.get_children())
    
    for i in range(15): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA.heading(columns[i], text=agents[0][i])
    for i in range(1, len(agents)): #
        try:
            treeviewA.insert('', i, values=(agents[i][0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8], agents[i][9], agents[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(exits)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA2E.heading(columns[i], text=agent2exit[0][i])
    for i in range(1, len(agent2exit)): #
        try:
            treeviewA2E.insert('', i, values=(agent2exit[i][0], agent2exit[i][1], agent2exit[i][2], agent2exit[i][3], agent2exit[i][4], agent2exit[i][5],  agent2exit[i][6], agent2exit[i][7], agent2exit[i][8], agent2exit[i][9], agent2exit[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agents)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewAG.heading(columns[i], text=agentgroup[0][i])
    for i in range(1, len(agentgroup)): #
        try:
            treeviewAG.insert('', i, values=(agentgroup[i][0], agentgroup[i][1], agentgroup[i][2], agentgroup[i][3], agentgroup[i][4], agentgroup[i][5],  agentgroup[i][6], agentgroup[i][7], agentgroup[i][8], agentgroup[i][9], agentgroup[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(13): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewW.heading(columns[i], text=walls[0][i])
    for i in range(1, len(walls)): #
        try:
            treeviewW.insert('', i, values=(walls[i][0], walls[i][1], walls[i][2], walls[i][3], walls[i][4], walls[i][5],  walls[i][6], walls[i][7], walls[i][8]))
        except:
            treeviewW.insert('', i, values=(i))
            
    for i in range(9): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE.heading(columns[i], text=exits[0][i])
    for i in range(1, len(exits)): #
        try: 
            treeviewE.insert('', i, values=(exits[i][0], exits[i][1], exits[i][2], exits[i][3], exits[i][4], exits[i][5],  exits[i][6], exits[i][7], exits[i][8]))
        except:
            treeviewE.insert('', i, values=(i))
            
    for i in range(9): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewD.heading(columns[i], text=doors[0][i])
    for i in range(1, len(doors)): #
        try: 
            treeviewD.insert('', i, values=(doors[i][0], doors[i][1], doors[i][2], doors[i][3], doors[i][4], doors[i][5],  doors[i][6], doors[i][7], doors[i][8]))
        except:
            treeviewD.insert('', i, values=(i))

    for i in range(len(doors)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE2D.heading(columns[i], text=exit2door[0][i])
    for i in range(1, len(exit2door)): #
        try: 
            treeviewE2D.insert('', i, values=(exit2door[i][0], exit2door[i][1], exit2door[i][2], exit2door[i][3], exit2door[i][4], exit2door[i][5],  exit2door[i][6], exit2door[i][7], exit2door[i][8]))
        except:
            treeviewE2D.insert('', i, values=(i))
    

def file_open(event=None):
    
    global agents, agent2exit, agentgroup, walls, exits, doors, exit2door
    
    fnameCSV = tkf.askopenfilename(filetypes=(("csv files", "*.csv"),("All files", "*.*"))) #,initialdir=self.currentdir)
        #temp=self.fname_EVAC.split('/') 
    temp=os.path.basename(fnameCSV)
    currentdir = os.path.dirname(fnameCSV)
    #lb_csv.config(text = "The input csv file selected: "+str(fnameCSV)+"\n")
    #self.textInformation.insert(END, 'fname_EVAC:   '+self.fname_EVAC)
    print('fname', fnameCSV)
    #setStatusStr("Simulation not yet started!")
    #textInformation.insert(END, '\n'+'EVAC Input File Selected:   '+self.fname_EVAC+'\n')
    
    agents, agent2exit, agentgroup, walls, exits, doors, exit2door = readCrowdEgressCSV(fnameCSV, debug=True, marginTitle=1)
    
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA2E.delete(*treeviewA2E.get_children())
    treeviewAG.delete(*treeviewAG.get_children())
    treeviewE.delete(*treeviewE.get_children())
    treeviewD.delete(*treeviewD.get_children())
    treeviewW.delete(*treeviewW.get_children())
    treeviewE2D.delete(*treeviewE2D.get_children())
    
    for i in range(15): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA.heading(columns[i], text=agents[0][i])
    for i in range(1, len(agents)): #
        try:
            treeviewA.insert('', i, values=(agents[i][0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8], agents[i][9], agents[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(exits)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA2E.heading(columns[i], text=agent2exit[0][i])
    for i in range(1, len(agent2exit)): #
        try:
            treeviewA2E.insert('', i, values=(agent2exit[i][0], agent2exit[i][1], agent2exit[i][2], agent2exit[i][3], agent2exit[i][4], agent2exit[i][5],  agent2exit[i][6], agent2exit[i][7], agent2exit[i][8], agent2exit[i][9], agent2exit[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agents)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewAG.heading(columns[i], text=agentgroup[0][i])
    for i in range(1, len(agentgroup)): #
        try:
            treeviewAG.insert('', i, values=(agentgroup[i][0], agentgroup[i][1], agentgroup[i][2], agentgroup[i][3], agentgroup[i][4], agentgroup[i][5],  agentgroup[i][6], agentgroup[i][7], agentgroup[i][8], agentgroup[i][9], agentgroup[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(13): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewW.heading(columns[i], text=walls[0][i])
    for i in range(1, len(walls)): #
        try:
            treeviewW.insert('', i, values=(walls[i][0], walls[i][1], walls[i][2], walls[i][3], walls[i][4], walls[i][5],  walls[i][6], walls[i][7], walls[i][8]))
        except:
            treeviewW.insert('', i, values=(i))
            
    for i in range(9): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE.heading(columns[i], text=exits[0][i])
    for i in range(1, len(exits)): #
        try: 
            treeviewE.insert('', i, values=(exits[i][0], exits[i][1], exits[i][2], exits[i][3], exits[i][4], exits[i][5],  exits[i][6], exits[i][7], exits[i][8]))
        except:
            treeviewE.insert('', i, values=(i))
            
    for i in range(9): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewD.heading(columns[i], text=doors[0][i])
    for i in range(1, len(doors)): #
        try: 
            treeviewD.insert('', i, values=(doors[i][0], doors[i][1], doors[i][2], doors[i][3], doors[i][4], doors[i][5],  doors[i][6], doors[i][7], doors[i][8]))
        except:
            treeviewD.insert('', i, values=(i))

    for i in range(len(doors)): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE2D.heading(columns[i], text=exit2door[0][i])
    for i in range(1, len(exit2door)): #
        try: 
            treeviewE2D.insert('', i, values=(exit2door[i][0], exit2door[i][1], exit2door[i][2], exit2door[i][3], exit2door[i][4], exit2door[i][5],  exit2door[i][6], exit2door[i][7], exit2door[i][8]))
        except:
            treeviewE2D.insert('', i, values=(i))

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
frameAgent2Exit = Frame(root)
frameAgentGroup = Frame(root)
frameWall = Frame(root)
frameExit = Frame(root)
frameDoor = Frame(root)
frameExit2Door = Frame(root)

notebook.add(frameAgent,text="  <AgentFeatures>  ")
notebook.add(frameWall,text="  <Wall/Obstruction>  ")
notebook.add(frameExit,text="  <Exit/SinkPoint>  ")
notebook.add(frameAgent2Exit,text="  <AgentExitProb>  ")
notebook.add(frameDoor,text="  <Door/Passage/WayPoint>  ")
notebook.add(frameAgentGroup,text="  <AgentGroup>  ")
notebook.add(frameExit2Door,text="  <Exit2DoorArray>  ")

#left_frame = Frame(root, width=200, height=600, bg="grey")
#left_frame.pack_propagate(0)
        
#right_frame = Frame(root, width=400, height=600, bg="lightgrey")
#right_frame.pack_propagate(0)

#columns = ("agent", "iniPosX", "iniPosY", "iniVx", "iniVy", "timelag", "tpre", "p", "pMode", "p2", "talkRange", "aType", "inComp", "tpreMode")

columns = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q")

scrollbarAy = Scrollbar(frameAgent, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAy.pack(side=RIGHT, fill=Y)

scrollbarAx = Scrollbar(frameAgent, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAx.pack(side=BOTTOM, fill=X)

treeviewA = Treeview(frameAgent, height=18, show="headings", columns=columns)  #Table
scrollbarAy.config(command=treeviewA.yview)
scrollbarAx.config(command=treeviewA.xview)

#treeviewA.column("/", width=30, anchor='center')
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


treeviewA.pack(side=LEFT, fill=BOTH)

#scrollbar = Scrollbar(treeviewA, orient="vertical", command=treeviewA.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
#scrollbar.config(command=treeviewA.yview)

scrollbarA2Ey = Scrollbar(frameAgent2Exit, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarA2Ey.pack(side=RIGHT, fill=Y)

scrollbarA2Ex = Scrollbar(frameAgent2Exit, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarA2Ex.pack(side=BOTTOM, fill=X)

treeviewA2E = Treeview(frameAgent2Exit, height=18, show="headings", columns=columns)  #Table
scrollbarA2Ey.config(command=treeviewA2E.yview)
scrollbarA2Ex.config(command=treeviewA2E.xview)

#treeviewA2E.column("/", width=30, anchor='center')
treeviewA2E.column("A", width=70, anchor='center')
treeviewA2E.column("B", width=70, anchor='center')
treeviewA2E.column("C", width=70, anchor='center')
treeviewA2E.column("D", width=70, anchor='center')
treeviewA2E.column("E", width=70, anchor='center')
treeviewA2E.column("F", width=70, anchor='center')
treeviewA2E.column("G", width=70, anchor='center')
treeviewA2E.column("H", width=70, anchor='center')
treeviewA2E.column("I", width=70, anchor='center')
treeviewA2E.column("J", width=70, anchor='center')
treeviewA2E.column("K", width=70, anchor='center')
treeviewA2E.column("L", width=70, anchor='center')
treeviewA2E.column("M", width=70, anchor='center')
treeviewA2E.column("N", width=70, anchor='center')
treeviewA2E.column("O", width=70, anchor='center')
treeviewA2E.column("P", width=70, anchor='center')
treeviewA2E.column("Q", width=70, anchor='center')

treeviewA2E.pack(side=LEFT, fill=BOTH)


scrollbarAGy = Scrollbar(frameAgentGroup, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAGy.pack(side=RIGHT, fill=Y)

scrollbarAGx = Scrollbar(frameAgentGroup, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAGx.pack(side=BOTTOM, fill=X)

treeviewAG = Treeview(frameAgentGroup, height=18, show="headings", columns=columns)  #Table
scrollbarAGy.config(command=treeviewAG.yview)
scrollbarAGx.config(command=treeviewAG.xview)

#treeviewAG.column("/", width=30, anchor='center')
treeviewAG.column("A", width=70, anchor='center')
treeviewAG.column("B", width=70, anchor='center')
treeviewAG.column("C", width=70, anchor='center')
treeviewAG.column("D", width=70, anchor='center')
treeviewAG.column("E", width=70, anchor='center')
treeviewAG.column("F", width=70, anchor='center')
treeviewAG.column("G", width=70, anchor='center')
treeviewAG.column("H", width=70, anchor='center')
treeviewAG.column("I", width=70, anchor='center')
treeviewAG.column("J", width=70, anchor='center')
treeviewAG.column("K", width=70, anchor='center')
treeviewAG.column("L", width=70, anchor='center')
treeviewAG.column("M", width=70, anchor='center')
treeviewAG.column("N", width=70, anchor='center')
treeviewAG.column("O", width=70, anchor='center')
treeviewAG.column("P", width=70, anchor='center')
treeviewAG.column("Q", width=70, anchor='center')

treeviewAG.pack(side=LEFT, fill=BOTH)


scrollbarWy = Scrollbar(frameWall, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarWy.pack(side=RIGHT, fill=Y)

scrollbarWx = Scrollbar(frameWall, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarWx.pack(side=BOTTOM, fill=X)

treeviewW = Treeview(frameWall, height=18, show="headings", columns=columns)  #Table
scrollbarWy.config(command=treeviewW.yview)
scrollbarWx.config(command=treeviewW.xview)

#treeviewW.column("/", width=30, anchor='center')
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

#treeviewE.column("/", width=30, anchor='center')
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


### Frame of Exit
scrollbarDy = Scrollbar(frameDoor, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarDy.pack(side=RIGHT, fill=Y)

scrollbarDx = Scrollbar(frameDoor, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarDx.pack(side=BOTTOM, fill=X)

treeviewD = Treeview(frameDoor, height=18, show="headings", columns=columns)  #Table
scrollbarDy.config(command=treeviewD.yview)
scrollbarDx.config(command=treeviewD.xview)

#treeviewE.column("/", width=30, anchor='center')
treeviewD.column("A", width=100, anchor='center')
treeviewD.column("B", width=70, anchor='center')
treeviewD.column("C", width=70, anchor='center')
treeviewD.column("D", width=70, anchor='center')
treeviewD.column("E", width=70, anchor='center')
treeviewD.column("F", width=70, anchor='center')
treeviewD.column("G", width=70, anchor='center')
treeviewD.column("H", width=70, anchor='center')
treeviewD.column("I", width=70, anchor='center')
treeviewD.column("J", width=70, anchor='center')
treeviewD.column("K", width=70, anchor='center')
treeviewD.column("L", width=70, anchor='center')
treeviewD.column("M", width=70, anchor='center')
treeviewD.column("N", width=70, anchor='center')
treeviewD.column("O", width=70, anchor='center')
treeviewD.column("P", width=70, anchor='center')
treeviewD.column("Q", width=70, anchor='center')
treeviewD.pack(side=LEFT, fill=BOTH)


### Frame of Exit
scrollbarE2Dy = Scrollbar(frameExit2Door, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarE2Dy.pack(side=RIGHT, fill=Y)

scrollbarE2Dx = Scrollbar(frameExit2Door, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarE2Dx.pack(side=BOTTOM, fill=X)

treeviewE2D = Treeview(frameExit2Door, height=18, show="headings", columns=columns)  #Table
scrollbarE2Dy.config(command=treeviewE2D.yview)
scrollbarE2Dx.config(command=treeviewE2D.xview)

#treeviewE.column("/", width=30, anchor='center')
treeviewE2D.column("A", width=100, anchor='center')
treeviewE2D.column("B", width=70, anchor='center')
treeviewE2D.column("C", width=70, anchor='center')
treeviewD.column("D", width=70, anchor='center')
treeviewD.column("E", width=70, anchor='center')
treeviewD.column("F", width=70, anchor='center')
treeviewD.column("G", width=70, anchor='center')
treeviewD.column("H", width=70, anchor='center')
treeviewD.column("I", width=70, anchor='center')
treeviewD.column("J", width=70, anchor='center')
treeviewD.column("K", width=70, anchor='center')
treeviewD.column("L", width=70, anchor='center')
treeviewD.column("M", width=70, anchor='center')
treeviewD.column("N", width=70, anchor='center')
treeviewD.column("O", width=70, anchor='center')
treeviewD.column("P", width=70, anchor='center')
treeviewD.column("Q", width=70, anchor='center')
treeviewD.pack(side=LEFT, fill=BOTH)

def treeview_sort_column(tv, col, reverse):  # Treeview

    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # sort method
    # rearrange items in sorted positions

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 

def set_cell_value_A(event): # double click to edit the item
    
    global agents
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
    entryedit = Text(root, width=56, height = 2)
    #entryedit = Entry(root,width=10)
    entryedit.insert(END, agents[rn][0]+'|'+agents[0][cn-1]+' = '+str(item_text[cn-1]))
    #entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    entryedit.pack()
    #lb= Label(root, text = str(rn)+columns[cn-1])
    #lb.pack()

    def saveedit():

        global agents
        try:
            temp=entryedit.get(0.0, 'end').split('=')
            treeviewA.set(item, column=column, value=temp[1].strip())
            agents[rn][cn-1]=temp[1].strip()
            print(agents) #[rn, cn])
        except:
            treeviewA.set(item, column=column, value=entryedit.get(0.0, 'end').strip())
            agents[rn][cn-1]=entryedit.get(0.0, 'end').strip()
            print(agents) #[rn, cn])
            
        #treeviewA.set(item, column=column, value=entryedit.get(0.0, "end"))
        #agents[rn-1][cn-2]=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    okb = Button(root, text=agents[rn][0]+'|'+agents[0][cn-1]+': <Save Changes>', width=56, command=saveedit)
    okb.pack() #place(x=90+(cn-1)*242,y=2+rn*20)

def newrow_A():
    
    global agents
    for item in treeviewA.selection():
        #item = I001
        item_text = treeviewA.item(item, "values")
        print(item_text)
        print(item)
        #print(item_text[0:2])  # Output the column number selected by users
    #column= treeviewA.identify_column(event.x)# column
    #row = treeviewA.identify_row(item)  # row

    #cn = int(str(column).replace('#',''))
    #rn = int(str(item).replace('I',''), base=16)
    try:
        treeviewA.insert('', len(agents), values=(item_text[0], item_text[1], item_text[2],item_text[3], item_text[4], item_text[5],item_text[6], item_text[7], item_text[8], item_text[9], item_text[10])) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
        agents.append([item_text[0], item_text[1], item_text[2],item_text[3], item_text[4], item_text[5],item_text[6], item_text[7], item_text[8], item_text[9], item_text[10]])
        #npzVE = np.concatenate((npzVE, tempVE), axis=0)
    except:
        treeviewA.insert('', len(agents), values=('agent'+str(len(agents)-1),0,0,0,0,0,0,0,0,0,0,0))
        agents.append(['agent'+str(len(agents)-1), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    #treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    print("len(agents)")
    treeviewA.update()
    
    #name.append('NoName')
    #pos.append('IP')
    #vel.append('Trial')
    #treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    #treeviewA.update()

    #newb.place(x=120, y=20) #y=(len(name)-1)*20+45)
    #newb.update()

def deleterow_A():
    
    global agents
    for item in treeviewA.selection():
        #item = I001
        item_text = treeviewA.item(item, "values")
        print(item_text)
        print(item)

    #cn = int(str(column).replace('#',''))
    rn = int(str(item).replace('I',''), base=16)
    try:
        treeviewA.delete(item) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
    except:
        treeviewA.delete(item)
    #treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    treeviewA.update()

def set_cell_value_W(event):
    global walls
    pass

treeviewA.bind('<Double-1>', set_cell_value_A) # Double click to edit items
root.bind("<Control-o>", file_open)
root.bind("<Control-s>", file_save)
root.bind("<Control-n>", file_new)


for col in columns:  # bind function: enable sorting in table headings
    treeviewA.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeviewA, _col, False))

#######################
# Configure the menubar

menubar = Menu(root, bg="lightgrey", fg="black")
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
file_menu.add_command(label="New", command=file_new, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=file_open, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=file_save, accelerator="Ctrl+S")
menubar.add_cascade(label="File", menu=file_menu)

add_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
add_menu.add_command(label="Add Item", command=newrow_A, accelerator="Ctrl+A")
menubar.add_cascade(label="Add", menu=add_menu)

delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Item", command=deleterow_A, accelerator="Ctrl+D")
menubar.add_cascade(label="Delete", menu=delete_menu)

newb = Button(frameAgent, text='New Agent', width=20, command=newrow_A)
newb.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

newb = Button(frameAgent, text='Delete Agent', width=20, command=deleterow_A)
newb.pack() #place(x=120,y=20 )

newb = Button(frameAgent2Exit, text='New Agent2Exit', width=20, command=newrow_A)
newb.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

newb = Button(frameAgent2Exit, text='Delete Agent2Exit', width=20, command=deleterow_A)
newb.pack() #place(x=120,y=20 )

newb = Button(frameAgentGroup, text='New AgentGroup', width=20, command=newrow_A)
newb.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

newb = Button(frameAgentGroup, text='Delete AgentGroup', width=20, command=deleterow_A)
newb.pack() #place(x=120,y=20 )

root.mainloop()
