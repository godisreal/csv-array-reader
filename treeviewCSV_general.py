
import os, sys
import csv
#import numpy as np

#from math import *
#from config import *
#import re
#import random
#from ctypes import *
#import struct
#import time

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
    

##################################################
# This is the global data array from csv data file
# Initialize by None
dataCSV = None
openCSV = False
openFileName = None
FONT_SIZE = 16

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
    #print('\n')

    print('\n')
    print('#=======================#')
    print(fileName)
    #dataNP = np.array(strData)

    #print(strData[1:,1:])
    csvFile.close()
    return strData
    
'''
def saveCSV(dataNP, outputFile, inputStr=''):
    
    (I, J) = np.shape(dataNP)
    #(I, J) = np.shape(exit2doors)
    #print "The size of exit2door:", [I, J]
    #dataNP = np.zeros((I+1, J+1))

    #dataNP[1:, 1:] = exit2doors
    #np.savetxt(fileName, dataNP, delimiter=',', fmt='%s')   #'2darray.csv'
    try:
        with open(outputFile, mode='w+', newline='') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if inputStr:
                csv_writer.writerow([inputStr])
            for i in range(I):
                #print(dataNP[i])
                csv_writer.writerow(dataNP[i])
    
    except:
        with open(outputFile, mode='w+') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if inputStr:
                csv_writer.writerow([inputStr])
            #csv_writer.writerow(['&Wall', '0/startX', '1/startY', '2/endX', '3/endY', '4/arrow', '5/shape', '6/inComp'])
            #index_temp=0
            for i in range(I):
                csv_writer.writerow(dataNP[i])
            #for wall in walls:
            #    csv_writer.writerow(['--', str(wall.params[0]), str(wall.params[1]), str(wall.params[2]), str(wall.params[3]), str(wall.arrow), str(wall.mode), str(wall.inComp)])
            #    index_temp=index_temp+1
'''

def file_new(event=None):
    
    global dataCSV
    global openCSV
    global openFileName
       
    dataCSV=[]
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA.update()   
    for i in range(len(dataCSV)): #
        try:
            treeviewA.insert('', i, values=(i+1, dataCSV[i][0], dataCSV[i][1], dataCSV[i][2], dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
        except:
            treeviewA.insert('', i, values=(i+1))
    openCSV=True
            

def file_open(event=None):
    
    global dataCSV
    global openCSV
    global openFileName
    
    dataCSV = None
    fnameCSV = tkf.askopenfilename(filetypes=(("csv files", "*.csv"),("All files", "*.*"))) #,initialdir=self.currentdir)
        #temp=self.fname_EVAC.split('/') 
    openFileName = fnameCSV
    temp=os.path.basename(fnameCSV)
    currentdir = os.path.dirname(fnameCSV)
    file_name_label.config(text = "The csv file selected: "+str(fnameCSV), fg="black", bg="lightgrey", font=(None, 10))
    #self.textInformation.insert(END, 'fname_EVAC:   '+self.fname_EVAC)
    print('fname', fnameCSV)
    #setStatusStr("Simulation not yet started!")
    #textInformation.insert(END, '\n'+'EVAC Input File Selected:   '+self.fname_EVAC+'\n')
    
    dataCSV = readCSV_base(fnameCSV)
    print(dataCSV)
    
    treeviewA.delete(*treeviewA.get_children())    
    treeviewA.update()  
    
    for i in range(len(dataCSV)): #
        try:
            treeviewA.insert('', i, values=(i+1, dataCSV[i][0], dataCSV[i][1], dataCSV[i][2], dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
        except:
            treeviewA.insert('', i, values=(i+1))
        
    openCSV=True
    #update_line_numbers()


def file_save(event=None):

    global dataCSV
    global openCSV
    global openFileName

    new_file_name = tkf.asksaveasfilename()
    if new_file_name:
        openFileName = new_file_name
    if openCSV is False:
        msg.showerror("No File Open", "Please open an csv file first")
        return

    #with open(self.active_ini_filename, "w") as ini_file:
    #    self.active_ini.write(ini_file)
    #saveCSV(dataCSV, openFileName)

    try:
        with open(openFileName, mode='w', newline='') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #for i in range(I):
                #print(dataNP[i])
                #csv_writer.writerow(dataNP[i])
            for item in treeviewA.get_children():
                item_text = treeviewA.item(item, "values")
                temp = list(item_text)
                print(temp[1:])
                csv_writer.writerow(temp[1:])
    except:
        with open(openFileName, mode='w') as exit_file:
            csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #csv_writer.writerow(['&Wall', '0/startX', '1/startY', '2/endX', '3/endY', '4/arrow', '5/shape', '6/inComp'])
            #index_temp=0
            #for i in range(I):
                #print(dataNP[i])
                #csv_writer.writerow(dataNP[i])
            for item in treeviewA.get_children():
                item_text = treeviewA.item(item, "values")
                temp = list(item_text)
                print(temp[1:])
                csv_writer.writerow(temp[1:])

    msg.showinfo("Saved", "File Saved Successfully")

'''
def treeview_sort_column(tv, col, reverse):  # Treeview

    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # sort method
    # rearrange items in sorted positions

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 
'''

def set_cell_value(event=None): # double click to edit the item

    for item in treeviewA.selection():

        #item = I001
        item_text = treeviewA.item(item, "values")
        print(item_text)
        print(int(item_text[0]))
        print(item)
        #print(item_text[0:2])  # Output the column number selected by users

    column= treeviewA.identify_column(event.x)# column
    row = treeviewA.identify_row(event.y)  # row

    cn = int(str(column).replace('#',''))
    rn = int(str(row).replace('I',''), base=16)
    
    print("cn:", column, cn)
    print("rn:", row, rn)

    rn = int(item_text[0])

    #entryedit = Text(root,width=10+(cn-1)*16,height = 1)
    entryedit = Text(root, width=20, height = 2)
    #entryedit = Entry(root,width=10)
    entryedit.insert(END, str(rn)+columns[cn-1]+'= '+str(item_text[cn-1]))
    #entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    entryedit.pack()
    #lb= Label(root, text = str(rn)+columns[cn-1])
    #lb.pack()

    def saveedit(event=None):
        
        global dataCSV
        try:
            temp=entryedit.get(0.0, 'end').split('=')
            treeviewA.set(item, column=column, value=temp[1].strip())
            #dataCSV[rn-1][cn-2]=temp[1].strip()
            #print(dataCSV) #[rn, cn])
        except:
            treeviewA.set(item, column=column, value=entryedit.get(0.0, 'end').strip())
            #dataCSV[rn-1][cn-2]=entryedit.get(0.0, 'end').strip()
            #print(dataCSV) #[rn, cn])
        #lb.destroy()
        entryedit.destroy()
        okb.destroy()

    okb = Button(root, text= str(rn)+columns[cn-1]+':OK', width=9, command=saveedit)
    okb.pack() #place(x=90+(cn-1)*130,y=2+rn*20)
    

def addrow(event=None):

    for item in treeviewA.selection():
        #item = I001
        item_text = treeviewA.item(item, "values")
        print(item_text)
        print(item)
        print(item.index)
        #print(item_text[0:2])  # Output the column number selected by users
    try:
        #rn = int(str(item).replace('I',''), base=16)
        rn = int(item_text[0])
    except:
        rn = int(len(dataCSV))
        
    try:
        treeviewA.insert('', int(rn), values=item_text) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
    except:
        treeviewA.insert('', int(rn), values=(int(rn)+1))
    #treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    updateRowNum()
    treeviewA.update()

    #newb.place(x=120, y=20) #y=(len(name)-1)*20+45)
    #newb.update()
    
def deleterow(event=None):
    
    global dataCSV
    for item in treeviewA.selection():
        #item = I001
        item_text = treeviewA.item(item, "values")
        print(item_text)
        print(item)

    #cn = int(str(column).replace('#',''))
    rn = int(str(item).replace('I',''), base=16)
    print(rn)
    try:
        treeviewA.delete(item) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
    except:
        treeviewA.delete(item)
    #treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
    updateRowNum()
    treeviewA.update()
    
def updateRowNum(event=None):
    i=1
    for item in treeviewA.get_children():
        item_text = treeviewA.item(item, "values")
        treeviewA.set(item, column=0, value=str(i))
        i=i+1
    return None


#newb = Button(root, text='New Agent', width=20, command=addrow)
#newb.place(x=120,y=20 ) #(len(name)-1)*20+45)


root = Tk() 

file_name_var = StringVar()
file_name_label = Label(root, textvar=openFileName, fg="black", bg="white", font=(None, 13))
file_name_label.pack(side=TOP, expand=1, fill=X)

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
add_menu.add_command(label="Add Item", command=addrow, accelerator="Ctrl+A")
menubar.add_cascade(label="Add", menu=add_menu)

delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Item", command=deleterow, accelerator="Ctrl+D")
menubar.add_cascade(label="Delete", menu=delete_menu)

'''
delete_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
delete_menu.add_command(label="Delete Item", command=file_open, accelerator="Ctrl+O")
menubar.add_cascade(label="Delete", menu=delete_menu)
'''

#left_frame = Frame(root, width=200, height=600, bg="grey")
#left_frame.pack_propagate(0)
        
#right_frame = Frame(root, width=400, height=600, bg="lightgrey")
#right_frame.pack_propagate(0)

#columns = ("agent", "iniPosX", "iniPosY", "iniVx", "iniVy", "timelag", "tpre", "p", "pMode", "p2", "talkRange", "aType", "inComp", "tpreMode")

COL=[]
for i in range(16):
    COL.append(chr(i+65))
#print(COL)
columns = tuple(COL)
#columns = ("A", "B")

scrollbarAy = Scrollbar(root, orient="vertical") #, orient="vertical", command=treeview.yview)
scrollbarAy.pack(side=RIGHT, expand=1, fill=Y)

scrollbarAx = Scrollbar(root, orient="horizontal") #, orient="vertical", command=treeview.yview)
scrollbarAx.pack(side=BOTTOM, expand=1, fill=X)

treeviewA = Treeview(root, height=18, show="headings", columns=columns)  #Table
scrollbarAy.config(command=treeviewA.yview)
scrollbarAx.config(command=treeviewA.xview)

for i in range(16):
    treeviewA.column(chr(i+65), width=70, anchor='center')
treeviewA.pack(side=TOP, fill=BOTH)


for col in columns:  # bind function: enable sorting in table headings
    treeviewA.heading(col, text=col) #, command=lambda _col=col: treeview_sort_column(treeviewA, _col, False))

treeviewA.bind('<Double-1>', set_cell_value) # Double click to edit items
root.bind("<Control-n>", file_new)
root.bind("<Control-o>", file_open)
root.bind("<Control-s>", file_save)
root.bind("<Control-a>", addrow)
root.bind("<Control-d>", deleterow)

#treeviewA.bind("<MouseWheel>", scroll_text_and_line_numbers)
#treeviewA.bind("<Button-4>", scroll_text_and_line_numbers)
#treeviewA.bind("<Button-5>", scroll_text_and_line_numbers)
#line_numbers.bind("<MouseWheel>", skip_event)
#line_numbers.bind("<Button-4>", skip_event)
#line_numbers.bind("<Button-5>", skip_event)
root.mainloop()

