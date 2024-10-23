
import os, sys, csv
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
    import tkinter.messagebox as msg
else:
    # Python 2
    from Tkinter import *
    from ttk import Notebook
    from ttk import Treeview
    from ttk import Entry
    import tkFileDialog as tkf
    import tkMessageBox as msg


agents=None
agent2exit=None
agentgroup=None
walls=None
exits=None
doors=None
exit2door=None

'''
RNA=0
RNA2E=0
RNAG=0
RNW=0
RNE=0
RNR=0
RNE2D=0
'''

openFileName = None


def readCSV_base(fileName):
    
    # read .csv file
    csvFile = open(fileName, "r")
    reader = csv.reader(csvFile)
    print(reader)
    strData = []
    for item in reader:
        #print(item)
        strData.append(item)

    #print(strData)
    #print('np.shape(strData)=', np.shape(strData))
    #print('\n')

    print('\n')
    print('#=======================#')
    print(fileName)
    dataNP = np.array(strData)
    #print (dataNP)
    #print ('np.shape(dataNP)', np.shape(dataNP))
    #print ('\n')

    #print(strData[1:,1:])
    csvFile.close()
    return dataNP


def getData(fileName, strNote):
    dataFeatures = readCSV_base(fileName)

    Num_Data = len(dataFeatures)
    
    IPedStart=0
    Find = False
    #print(dataFeatures)
    for i in range(Num_Data):
        if len(dataFeatures[i]):
            if dataFeatures[i][0]==strNote:
                IPedStart=i
                Find = True
    
    if Find is False:
        return [], 0, 0
        #IPedStart = None
        #IPedEnd = None
        #dataOK = None
        #return dataOK, IPedStart, IPedEnd
        #return [], 0, 0
    else:
        IPedEnd=IPedStart
        for j in range(IPedStart, Num_Data):
            if len(dataFeatures[j]):
                if dataFeatures[j][0]=='' or dataFeatures[j][0]==' ':
                    IPedEnd=j
                    break
            else: #len(dataFeatures[j])==0: Namely dataFeatures[j]==[]
                IPedEnd=j
                break
            if j==Num_Data-1:
                IPedEnd=Num_Data

        dataOK = list(dataFeatures[IPedStart : IPedEnd])
        return dataOK, IPedStart, IPedEnd

    #data_result = np.array(dataOK)
    #return data_result[1:, 1:]
    

def readCrowdEgressCSV(FileName, debug=True, marginTitle=1):

    #dataFeatures = readCSV_base(FileName)
    #[Num_Data, Num_Features] = np.shape(dataFeatures)   

    agentFeatures, lowerIndex, upperIndex = getData(FileName, '&Ped')
    Num_Agents=len(agentFeatures)-marginTitle
    if Num_Agents <= 0:
        agentFeatures, lowerIndex, upperIndex = getData(FileName, '&agent')
        Num_Agents=len(agentFeatures)-marginTitle
    if Num_Agents <= 0:
        agentFeatures, lowerIndex, upperIndex = getData(FileName, '&Agent')
        Num_Agents=len(agentFeatures)-marginTitle

    if debug: 
        print ('Number of Agents:', Num_Agents, '\n')
        print ("Features of Agents\n", agentFeatures, "\n")

    agent2exitFeatures, lowerIndex, upperIndex = getData(FileName, '&agent2exit')
    Num_Agent2Exit=len(agent2exitFeatures)-marginTitle
    if Num_Agent2Exit <= 0:
        agent2exitFeatures, lowerIndex, upperIndex = getData(FileName, '&ped2exit')
        Num_Agent2Exit=len(agent2exitFeatures)-marginTitle
    if Num_Agent2Exit <= 0:
        agent2exitFeatures, lowerIndex, upperIndex = getData(FileName, '&Ped2Exit')
        Num_Agent2Exit=len(agent2exitFeatures)-marginTitle
    if debug:
        print ('Number of Agent2Exit:', Num_Agent2Exit, '\n')
        print ('Features of Agent2Exit\n', agent2exitFeatures, "\n")

    agentgroupFeatures, lowerIndex, upperIndex = getData(FileName, '&groupC')
    Num_AgentGroup=len(agentgroupFeatures)-marginTitle
    if Num_AgentGroup <= 0:
        agentgroupFeatures, lowerIndex, upperIndex = getData(FileName, '&groupCABD')
        Num_AgentGroup=len(agent2exitFeatures)-marginTitle
    if Num_AgentGroup <= 0:
        agentgroupFeatures, lowerIndex, upperIndex = getData(FileName, '&groupABD')
        Num_AgentGroup=len(agent2exitFeatures)-marginTitle
    if debug:
        print ('Number of AgentGroup:', Num_AgentGroup, '\n')
        print ('Features of AgentGroup\n', agentgroupFeatures, "\n")

    obstFeatures, lowerIndex, upperIndex = getData(FileName, '&Wall')
    Num_Obsts=len(obstFeatures)-marginTitle
    if Num_Obsts <= 0:
        obstFeatures, lowerIndex, upperIndex = getData(FileName, '&wall')
        Num_Obsts=len(obstFeatures)-marginTitle

    if debug:
        print ('Number of Walls:', Num_Obsts, '\n')
        print ("Features of Walls\n", obstFeatures, "\n")

    exitFeatures, lowerIndex, upperIndex = getData(FileName, '&Exit')
    Num_Exits=len(exitFeatures)-marginTitle
    if Num_Exits <= 0:
        exitFeatures, lowerIndex, upperIndex = getData(FileName, '&exit')
        Num_Exits=len(exitFeatures)-marginTitle
        
    if debug: 
        print ('Number of Exits:', Num_Exits, '\n')
        print ("Features of Exits\n", exitFeatures, "\n")

    doorFeatures, lowerIndex, upperIndex = getData(FileName, '&Door')
    Num_Doors=len(doorFeatures)-marginTitle
    if Num_Doors <= 0:
        doorFeatures, lowerIndex, upperIndex = getData(FileName, '&door')
        Num_Doors=len(doorFeatures)-marginTitle
        
    if debug:
        print ('Number of Doors:', Num_Doors, '\n')
        print ('Features of Doors\n', doorFeatures, "\n")
        
    exit2doorFeatures, lowerIndex, upperIndex = getData(FileName, '&Exit2Door')
    Num_Exit2Door=len(exit2doorFeatures)-marginTitle
    if Num_Exit2Door <= 0:
        exit2doorFeatures, lowerIndex, upperIndex = getData(FileName, '&exit2door')
        Num_Exit2Door=len(doorFeatures)-marginTitle

    if debug:
        print ('Number of Exit2Door:', Num_Exit2Door, '\n')
        print ('Features of Exit2Door\n', exit2doorFeatures, "\n")

    return agentFeatures, agent2exitFeatures, agentgroupFeatures, obstFeatures, exitFeatures, doorFeatures, exit2doorFeatures



def file_new(event=None):
    global agents, agent2exit, agentgroup, walls, exits, doors, exit2door
    global openFileName
    
    agents=[['agent', 'iniX', 'iniY', 'iniVx', 'iniVy', 'timelag', 'tpre', 'p', 'pMode', 'p2', 'talkRange', 'talkProb', 'inComp', 'aType']]
    agent2exit=[['agent2exit', 'exit0', 'exit1', 'exit2', 'exit3', 'exit4', 'exit5', 'exit6']]
    agentgroup=[['agent2group', 'agent0', 'agent1', 'agent2','agent3', 'agent4', 'agent5', 'agent6']]
    walls=[['walls', 'startX', 'startY', 'endX', 'endY', 'arrow', 'shape', 'inComp']]
    exits=[['exits', 'startX', 'startY', 'endX', 'endY', 'arrow', 'shape', 'inComp']]
    doors=[['doors', 'startX', 'startY', 'endX', 'endY', 'arrow', 'shape', 'inComp']]
    exit2door=[['exit2door', 'door0', 'door1', 'door2']]
       
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA2E.delete(*treeviewA2E.get_children())
    treeviewAG.delete(*treeviewAG.get_children())
    treeviewE.delete(*treeviewE.get_children())
    treeviewD.delete(*treeviewD.get_children())
    treeviewW.delete(*treeviewW.get_children())
    treeviewE2D.delete(*treeviewE2D.get_children())
    treeviewA.update()    
    treeviewA2E.update()    
    treeviewAG.update()
    treeviewE.update()    
    treeviewD.update()    
    treeviewW.update()
    treeviewE2D.update()
    
    for i in range(len(agents[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA.heading(columns[i], text=agents[0][i])
    for i in range(1, len(agents)): #
        try:
            treeviewA.insert('', i, values=tuple(agents[i])) #[0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8], agents[i][9], agents[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agent2exit[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA2E.heading(columns[i], text=agent2exit[0][i])
    for i in range(1, len(agent2exit)): #
        try:
            treeviewA2E.insert('', i, values=tuple(agent2exit[i])) #[0], agent2exit[i][1], agent2exit[i][2], agent2exit[i][3], agent2exit[i][4], agent2exit[i][5],  agent2exit[i][6], agent2exit[i][7], agent2exit[i][8], agent2exit[i][9], agent2exit[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agentgroup[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewAG.heading(columns[i], text=agentgroup[0][i])
    for i in range(1, len(agentgroup)): #
        try:
            treeviewAG.insert('', i, values=tuple(agentgroup[i])) #[0], agentgroup[i][1], agentgroup[i][2], agentgroup[i][3], agentgroup[i][4], agentgroup[i][5],  agentgroup[i][6], agentgroup[i][7], agentgroup[i][8], agentgroup[i][9], agentgroup[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(walls[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewW.heading(columns[i], text=walls[0][i])
    for i in range(1, len(walls)): #
        try:
            treeviewW.insert('', i, values=tuple(walls[i])) #[0], walls[i][1], walls[i][2], walls[i][3], walls[i][4], walls[i][5],  walls[i][6], walls[i][7], walls[i][8]))
        except:
            treeviewW.insert('', i, values=(i))
            
    for i in range(len(exits[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE.heading(columns[i], text=exits[0][i])
    for i in range(1, len(exits)): #
        try: 
            treeviewE.insert('', i, values=tuple(exits[i])) #[0], exits[i][1], exits[i][2], exits[i][3], exits[i][4], exits[i][5],  exits[i][6], exits[i][7], exits[i][8]))
        except:
            treeviewE.insert('', i, values=(i))
            
    for i in range(len(doors[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewD.heading(columns[i], text=doors[0][i])
    for i in range(1, len(doors)): #
        try: 
            treeviewD.insert('', i, values=tuple(doors[i])) #[0], doors[i][1], doors[i][2], doors[i][3], doors[i][4], doors[i][5],  doors[i][6], doors[i][7], doors[i][8]))
        except:
            treeviewD.insert('', i, values=(i))

    for i in range(len(exit2door[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE2D.heading(columns[i], text=exit2door[0][i])
    for i in range(1, len(exit2door)): #
        try: 
            treeviewE2D.insert('', i, values=tuple(exit2door[i])) #[0], exit2door[i][1], exit2door[i][2], exit2door[i][3], exit2door[i][4], exit2door[i][5],  exit2door[i][6], exit2door[i][7], exit2door[i][8]))
        except:
            treeviewE2D.insert('', i, values=(i))
    

def file_open(event=None):
    
    global agents, agent2exit, agentgroup, walls, exits, doors, exit2door
    global openFileName
    
    fnameCSV = tkf.askopenfilename(filetypes=(("csv files", "*.csv"),("All files", "*.*"))) #,initialdir=self.currentdir)
        #temp=self.fname_EVAC.split('/') 
    temp=os.path.basename(fnameCSV)
    currentdir = os.path.dirname(fnameCSV)
    #lb_csv.config(text = "The input csv file selected: "+str(fnameCSV)+"\n")
    #self.textInformation.insert(END, 'fname_EVAC:   '+self.fname_EVAC)
    print('fname', fnameCSV)
    #setStatusStr("Simulation not yet started!")
    #textInformation.insert(END, '\n'+'EVAC Input File Selected:   '+self.fname_EVAC+'\n')
    if fnameCSV:
        openFileName = fnameCSV
    
    file_name_label.config(text=fnameCSV, fg="black", bg="lightgrey", font=(None, 10))
    agents, agent2exit, agentgroup, walls, exits, doors, exit2door = readCrowdEgressCSV(fnameCSV, debug=True, marginTitle=1)
    
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA2E.delete(*treeviewA2E.get_children())
    treeviewAG.delete(*treeviewAG.get_children())
    treeviewE.delete(*treeviewE.get_children())
    treeviewD.delete(*treeviewD.get_children())
    treeviewW.delete(*treeviewW.get_children())
    treeviewE2D.delete(*treeviewE2D.get_children())
    treeviewA.update()    
    treeviewA2E.update()    
    treeviewAG.update()
    treeviewE.update()    
    treeviewD.update()    
    treeviewW.update()
    treeviewE2D.update()

    treeviewA.column(chr(65), width=130, anchor='center')
    treeviewA2E.column(chr(65), width=130, anchor='center')
    treeviewAG.column(chr(65), width=130, anchor='center')
    
    for i in range(len(agents[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA.heading(columns[i], text=agents[0][i])
    for i in range(1, len(agents)): #
        agents[i][0]=str(i)+"# "+agents[i][0]
        try:
            treeviewA.insert('', i, values=tuple(agents[i])) #[0], agents[i][1], agents[i][2], agents[i][3], agents[i][4], agents[i][5],  agents[i][6], agents[i][7], agents[i][8], agents[i][9], agents[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agent2exit[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewA2E.heading(columns[i], text=agent2exit[0][i])
    for i in range(1, len(agent2exit)): #
        agent2exit[i][0]=str(i)+"# "+agent2exit[i][0]
        try:
            treeviewA2E.insert('', i, values=tuple(agent2exit[i])) #[0], agent2exit[i][1], agent2exit[i][2], agent2exit[i][3], agent2exit[i][4], agent2exit[i][5],  agent2exit[i][6], agent2exit[i][7], agent2exit[i][8], agent2exit[i][9], agent2exit[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(agentgroup[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewAG.heading(columns[i], text=agentgroup[0][i])
    for i in range(1, len(agentgroup)): #
        agentgroup[i][0]=str(i)+"# "+agentgroup[i][0]
        try:
            treeviewAG.insert('', i, values=tuple(agentgroup[i])) #[0], agentgroup[i][1], agentgroup[i][2], agentgroup[i][3], agentgroup[i][4], agentgroup[i][5],  agentgroup[i][6], agentgroup[i][7], agentgroup[i][8], agentgroup[i][9], agentgroup[i][10]))
        except:
            treeviewA.insert('', i, values=(i))

    for i in range(len(walls[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewW.heading(columns[i], text=walls[0][i])
    for i in range(1, len(walls)): #
        try:
            treeviewW.insert('', i, values=tuple(walls[i])) #[0], walls[i][1], walls[i][2], walls[i][3], walls[i][4], walls[i][5],  walls[i][6], walls[i][7], walls[i][8]))
        except:
            treeviewW.insert('', i, values=(i))
            
    for i in range(len(exits[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE.heading(columns[i], text=exits[0][i])
    for i in range(1, len(exits)): #
        try: 
            treeviewE.insert('', i, values=tuple(exits[i])) #[0], exits[i][1], exits[i][2], exits[i][3], exits[i][4], exits[i][5],  exits[i][6], exits[i][7], exits[i][8]))
        except:
            treeviewE.insert('', i, values=(i))
            
    for i in range(len(doors[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewD.heading(columns[i], text=doors[0][i])
    for i in range(1, len(doors)): #
        try: 
            treeviewD.insert('', i, values=tuple(doors[i])) #[0], doors[i][1], doors[i][2], doors[i][3], doors[i][4], doors[i][5],  doors[i][6], doors[i][7], doors[i][8]))
        except:
            treeviewD.insert('', i, values=(i))

    for i in range(len(exit2door[0])): #np.shape(arr1D_2D(agents))[1]):  # bind function: enable sorting in table headings
        treeviewE2D.heading(columns[i], text=exit2door[0][i])
    for i in range(1, len(exit2door)): #
        try: 
            treeviewE2D.insert('', i, values=tuple(exit2door[i])) #[0], exit2door[i][1], exit2door[i][2], exit2door[i][3], exit2door[i][4], exit2door[i][5],  exit2door[i][6], exit2door[i][7], exit2door[i][8]))
        except:
            treeviewE2D.insert('', i, values=(i))
    

def file_save(event=None):

    global agents, agent2exit, agentgroup, walls, exits, doors, exit2door
    global openFileName

    new_file_name = filedialog.asksaveasfilename()
    if new_file_name:
        openFileName = new_file_name

    if openFileName:
        #with open(self.active_ini_filename, "w") as ini_file:
        #self.active_ini.write(ini_file)

        saveCSV(agents, openFileName, 'Agent Data is written as below.')
        saveCSV(agent2exit, openFileName, 'Exit selection probilibty is written as below.')
        saveCSV(agentgroup, openFileName, 'Agent group data is written as below.')
        
        msg.showinfo("Saved", "File Saved Successfully")
    else:
        msg.showerror("No File Open", "Please open an csv file first")
        return


def saveCSV(dataNP, outputFile, inputStr=''):
    
    (I, J) = np.shape(dataNP)
    #(I, J) = np.shape(exit2doors)
    #print "The size of exit2door:", [I, J]
    #dataNP = np.zeros((I+1, J+1))

    #dataNP[1:, 1:] = exit2doors
    #np.savetxt(fileName, dataNP, delimiter=',', fmt='%s')   #'2darray.csv'
    try:
        with open(outputFile, mode='a+', newline='') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if inputStr:
                csv_writer.writerow([inputStr])
            for i in range(I):
                #print(dataNP[i])
                csv_writer.writerow(dataNP[i])
            csv_writer.writerow([])
            csv_writer.writerow([])               
    
    except:
        with open(outputFile, mode='a+') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if inputStr:
                csv_writer.writerow([inputStr])
            #csv_writer.writerow(['&Wall', '0/startX', '1/startY', '2/endX', '3/endY', '4/arrow', '5/shape', '6/inComp'])
            #index_temp=0
            for i in range(I):
                csv_writer.writerow(dataNP[i])
            csv_writer.writerow([])
            csv_writer.writerow([])
            #for wall in walls:
            #    csv_writer.writerow(['--', str(wall.params[0]), str(wall.params[1]), str(wall.params[2]), str(wall.params[3]), str(wall.arrow), str(wall.mode), str(wall.inComp)])
            #    index_temp=index_temp+1

root = Tk()

file_name_var = StringVar()
file_name_label = Label(root, textvar=openFileName, fg="black", bg="lightgrey", font=(None, 12))
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

notebook = Notebook(root,  width=45, height=300)      
notebook.pack(side=TOP, padx=2, pady=2)

frameAgent = Frame(root)
frameAgent2Exit = Frame(root)
frameAgentGroup = Frame(root)
frameWall = Frame(root)
frameExit = Frame(root)
frameDoor = Frame(root)
frameExit2Door = Frame(root)

notebook.add(frameAgent,text="  <AgentFeatures>  ")
notebook.add(frameAgent2Exit,text="  <AgentExitProb>  ")
notebook.add(frameAgentGroup,text="  <AgentGroup>  ")
notebook.add(frameWall,text="  <Wall/Obstruction>  ")
notebook.add(frameExit,text="  <Exit/SinkPoint>  ")
notebook.add(frameDoor,text="  <Door/Passage/WayPoint>  ")
notebook.add(frameExit2Door,text="  <Exit2DoorArray>  ")

#left_frame = Frame(root, width=200, height=600, bg="grey")
#left_frame.pack_propagate(0)
        
#right_frame = Frame(root, width=400, height=600, bg="lightgrey")
#right_frame.pack_propagate(0)

#columns = ("agent", "iniPosX", "iniPosY", "iniVx", "iniVy", "timelag", "tpre", "p", "pMode", "p2", "talkRange", "aType", "inComp", "tpreMode")

#columns = tuple(np.arange(1, 100))

col_list=[]
for i in range(26):
    col_list.append(chr(i+65))
print(col_list)
columns = tuple(col_list)
    
#columns =("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R")

scrollbarAy = Scrollbar(frameAgent, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAy.pack(side=RIGHT, fill=Y)

scrollbarAx = Scrollbar(frameAgent, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAx.pack(side=BOTTOM, fill=X)

treeviewA = Treeview(frameAgent, height=18, show="headings", columns=columns)  #Table
scrollbarAy.config(command=treeviewA.yview)
scrollbarAx.config(command=treeviewA.xview)

for i in range(26):
    treeviewA.column(chr(i+65), width=70, anchor='center')
treeviewA.pack(side=LEFT, fill=BOTH)

'''
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
'''

scrollbarA2Ey = Scrollbar(frameAgent2Exit, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarA2Ey.pack(side=RIGHT, fill=Y)

scrollbarA2Ex = Scrollbar(frameAgent2Exit, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarA2Ex.pack(side=BOTTOM, fill=X)

treeviewA2E = Treeview(frameAgent2Exit, height=18, show="headings", columns=columns)  #Table
scrollbarA2Ey.config(command=treeviewA2E.yview)
scrollbarA2Ex.config(command=treeviewA2E.xview)

'''
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
'''

for i in range(26):
    treeviewA2E.column(chr(i+65), width=70, anchor='center')
treeviewA2E.pack(side=LEFT, fill=BOTH)

scrollbarAGy = Scrollbar(frameAgentGroup, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAGy.pack(side=RIGHT, fill=Y)

scrollbarAGx = Scrollbar(frameAgentGroup, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAGx.pack(side=BOTTOM, fill=X)

treeviewAG = Treeview(frameAgentGroup, height=18, show="headings", columns=columns)  #Table
scrollbarAGy.config(command=treeviewAG.yview)
scrollbarAGx.config(command=treeviewAG.xview)

'''
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
'''

for i in range(26):
    treeviewAG.column(chr(i+65), width=70, anchor='center')
treeviewAG.pack(side=LEFT, fill=BOTH)


scrollbarWy = Scrollbar(frameWall, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarWy.pack(side=RIGHT, fill=Y)

scrollbarWx = Scrollbar(frameWall, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarWx.pack(side=BOTTOM, fill=X)

treeviewW = Treeview(frameWall, height=18, show="headings", columns=columns)  #Table
scrollbarWy.config(command=treeviewW.yview)
scrollbarWx.config(command=treeviewW.xview)

for i in range(26):
    treeviewW.column(chr(i+65), width=70, anchor='center')
treeviewW.pack(side=LEFT, fill=BOTH)

### Frame of Exit
scrollbarEy = Scrollbar(frameExit, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarEy.pack(side=RIGHT, fill=Y)

scrollbarEx = Scrollbar(frameExit, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarEx.pack(side=BOTTOM, fill=X)

treeviewE = Treeview(frameExit, height=18, show="headings", columns=columns)  #Table
scrollbarEy.config(command=treeviewE.yview)
scrollbarEx.config(command=treeviewE.xview)

for i in range(26):
    treeviewE.column(chr(i+65), width=70, anchor='center')
treeviewE.pack(side=LEFT, fill=BOTH)

### Frame of Exit
scrollbarDy = Scrollbar(frameDoor, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarDy.pack(side=RIGHT, fill=Y)

scrollbarDx = Scrollbar(frameDoor, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarDx.pack(side=BOTTOM, fill=X)

treeviewD = Treeview(frameDoor, height=18, show="headings", columns=columns)  #Table
scrollbarDy.config(command=treeviewD.yview)
scrollbarDx.config(command=treeviewD.xview)

for i in range(26):
    treeviewD.column(chr(i+65), width=70, anchor='center')
treeviewD.pack(side=LEFT, fill=BOTH)

### Frame of Exit
scrollbarE2Dy = Scrollbar(frameExit2Door, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarE2Dy.pack(side=RIGHT, fill=Y)

scrollbarE2Dx = Scrollbar(frameExit2Door, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarE2Dx.pack(side=BOTTOM, fill=X)

treeviewE2D = Treeview(frameExit2Door, height=18, show="headings", columns=columns)  #Table
scrollbarE2Dy.config(command=treeviewE2D.yview)
scrollbarE2Dx.config(command=treeviewE2D.xview)

for i in range(26):
    treeviewE2D.column(chr(i+65), width=70, anchor='center')
treeviewE2D.pack(side=LEFT, fill=BOTH)

'''
#treeviewE.column("/", width=30, anchor='center')
treeviewE2D.column("A", width=100, anchor='center')
treeviewE2D.column("B", width=70, anchor='center')
treeviewE2D.column("C", width=70, anchor='center')
treeviewE2D.column("D", width=70, anchor='center')
treeviewE2D.column("E", width=70, anchor='center')
treeviewE2D.column("F", width=70, anchor='center')
treeviewE2D.pack(side=LEFT, fill=BOTH)
'''

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
    temp = item_text[0].split(" ")
    rn = int(temp[0].strip("#"))
    
    print("cn:", cn)
    print("rn:", rn)

    #entryedit = Text(root,width=10+(cn-1)*16,height = 1)
    entryedit = Text(root, width=56, height = 2)
    #entryedit = Entry(root,width=10)
    entryedit.insert(END, str(item_text[0])+'|'+agents[0][cn-1]+' = '+str(item_text[cn-1]))
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

    okb = Button(root, text=str(item_text[0])+'|'+agents[0][cn-1]+': <Save Changes>', width=56, command=saveedit)
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
        if len(agents)==1:
            treeviewA.insert('', len(agents), values=(tuple(['agent'+str(len(agents)-1), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']))) #['agent'+str(len(agents))]+agents[-1]))
            agents.append(['agent'+str(len(agents)-1), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
        else:
            treeviewA.insert('', len(agents), values=(tuple(agents[-1]))) 
            agents.append(agents[-1])
            
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
add_menu.add_command(label="Add Agent", command=newrow_A, accelerator="Ctrl+A")
add_menu.add_command(label="Add Wall", command=newrow_A)
add_menu.add_command(label="Add Exit", command=newrow_A)
add_menu.add_command(label="Add Door", command=newrow_A)
menubar.add_cascade(label="Add", menu=add_menu)

delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Agent", command=deleterow_A, accelerator="Ctrl+D")
menubar.add_cascade(label="Delete", menu=delete_menu)

newA = Button(frameAgent, text='New Agent', width=20, command=newrow_A)
newA.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delA = Button(frameAgent, text='Delete Agent', width=20, command=deleterow_A)
delA.pack() #place(x=120,y=20 )

newA2E = Button(frameAgent2Exit, text='New Agent2Exit', width=20, command=newrow_A)
newA2E.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delA2E = Button(frameAgent2Exit, text='Delete Agent2Exit', width=20, command=deleterow_A)
delA2E.pack() #place(x=120,y=20 )

newAG = Button(frameAgentGroup, text='New AgentGroup', width=20, command=newrow_A)
newAG.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delAG = Button(frameAgentGroup, text='Delete AgentGroup', width=20, command=deleterow_A)
delAG.pack() #place(x=120,y=20 )

newW = Button(frameWall, text='New Wall', width=20, command=newrow_A)
newW.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delW = Button(frameWall, text='Delete Wall', width=20, command=deleterow_A)
delW.pack() #place(x=120,y=20 )

newE = Button(frameExit, text='New Exit', width=20, command=newrow_A)
newE.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delE = Button(frameExit, text='Delete Exit', width=20, command=deleterow_A)
delE.pack() #place(x=120,y=20 )

newD = Button(frameDoor, text='New Door', width=20, command=newrow_A)
newD.pack() #place(x=120,y=20 ) #(len(name)-1)*20+45)

delD = Button(frameDoor, text='Delete Door', width=20, command=deleterow_A)
delD.pack() #place(x=120,y=20 )

root.mainloop()
