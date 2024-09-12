
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

class Editor(object):
    def __init__(self, fname=None):
    
        self.dataCSV = None
        self.openCSV = False
        self.openFileName = fname
        self.currentdir = None
        self.FONT_SIZE = 16
        
        self.root = Tk() 
        
        self.file_name_var = StringVar()
        self.file_name_label = Label(self.root, textvar=self.openFileName, fg="black", bg="white", font=(None, 13))
        self.file_name_label.pack(side=TOP, expand=1, fill=X)
        
        #######################
        # Configure the menubar      
        self.menubar = Menu(self.root, bg="lightgrey", fg="black")
        self.root.config(menu=self.menubar)
        
        self.file_menu = Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="New", command=self.file_new, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.file_save, accelerator="Ctrl+S")
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        
        self.add_menu = Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.add_menu.add_command(label="Add Item", command=self.addrow, accelerator="Ctrl+A")
        self.menubar.add_cascade(label="Add", menu=self.add_menu)
        
        self.delete_menu = Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.delete_menu.add_command(label="Delete Item", command=self.deleterow, accelerator="Ctrl+D")
        self.menubar.add_cascade(label="Delete", menu=self.delete_menu)
        
        #left_frame = Frame(root, width=200, height=600, bg="grey")
        #left_frame.pack_propagate(0)
                
        #right_frame = Frame(root, width=400, height=600, bg="lightgrey")
        #right_frame.pack_propagate(0)
        
        COL=[]
        for i in range(16):
            COL.append(chr(i+65))
        #print(COL)
        self.columns = tuple(COL)
        #columns = ("A", "B")
        
        self.scrollbarAy = Scrollbar(self.root, orient="vertical") #, orient="vertical", command=treeview.yview)
        self.scrollbarAy.pack(side=RIGHT, expand=1, fill=Y)
        
        self.scrollbarAx = Scrollbar(self.root, orient="horizontal") #, orient="vertical", command=treeview.yview)
        self.scrollbarAx.pack(side=BOTTOM, expand=1, fill=X)
        
        self.treeviewA = Treeview(self.root, height=18, show="headings", columns=self.columns)  #Table
        self.scrollbarAy.config(command=self.treeviewA.yview)
        self.scrollbarAx.config(command=self.treeviewA.xview)
        
        for i in range(16):
            self.treeviewA.column(chr(i+65), width=70, anchor='center')
        self.treeviewA.pack(side=TOP, fill=BOTH)
        
        
        for col in self.columns:  # bind function: enable sorting in table headings
            self.treeviewA.heading(col, text=col) #, command=lambda _col=col: treeview_sort_column(self.treeviewA, _col, False))
        
        self.treeviewA.bind('<Double-1>', self.set_cell_value) # Double click to edit items
        self.root.bind("<Control-n>", self.file_new)
        self.root.bind("<Control-o>", self.file_open)
        self.root.bind("<Control-s>", self.file_save)
        self.root.bind("<Control-a>", self.addrow)
        self.root.bind("<Control-d>", self.deleterow)
        
        #self.treeviewA.bind("<MouseWheel>", scroll_text_and_line_numbers)
        #self.treeviewA.bind("<Button-4>", scroll_text_and_line_numbers)
        #self.treeviewA.bind("<Button-5>", scroll_text_and_line_numbers)
        #line_numbers.bind("<MouseWheel>", skip_event)
        #line_numbers.bind("<Button-4>", skip_event)
        #line_numbers.bind("<Button-5>", skip_event)

    def readCSV_base(self, fileName):
        
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
    
    def file_new(self, event=None):
           
        self.dataCSV=[]
        self.treeviewA.delete(*self.treeviewA.get_children())    
        self.treeviewA.update()   
        for i in range(len(self.dataCSV)): #
            try:
                self.treeviewA.insert('', i, values=(i+1, dataCSV[i][0], dataCSV[i][1], dataCSV[i][2], dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
            except:
                self.treeviewA.insert('', i, values=(i+1))
        self.openCSV=True
                
    
    def file_open(self, event=None):
        
        #self.dataCSV
        #self.openCSV
        #self.openFileName
        
        self.dataCSV = None
        fnameCSV = tkf.askopenfilename(filetypes=(("csv files", "*.csv"),("All files", "*.*"))) #,initialdir=self.currentdir)
            #temp=self.fname_EVAC.split('/') 
        self.openFileName = fnameCSV
        temp=os.path.basename(fnameCSV)
        currentdir = os.path.dirname(fnameCSV)
        self.file_name_label.config(text = "The csv file selected: "+str(fnameCSV), fg="black", bg="lightgrey", font=(None, 10))
        #lb_csv.config(text = "The input csv file selected: "+str(fnameCSV)+"\n")
        #self.textInformation.insert(END, 'fname_EVAC:   '+self.fname_EVAC)
        print('fname', fnameCSV)
        #setStatusStr("Simulation not yet started!")
        #textInformation.insert(END, '\n'+'EVAC Input File Selected:   '+self.fname_EVAC+'\n')
        
        iniArray = self.readCSV_base(fnameCSV)
        #print(iniArray)
        self.dataCSV = iniArray
        
        self.treeviewA.delete(*self.treeviewA.get_children())    
        self.treeviewA.update()  
        
        for i in range(len(self.dataCSV)): #
            try:
                self.treeviewA.insert('', i, values=([i+1]+self.dataCSV[i]))  #(i+1, dataCSV[i][0], dataCSV[i][1], dataCSV[i][2], dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
            except:
                self.treeviewA.insert('', i, values=(i+1))
            
        self.openCSV=True
        #update_line_numbers()
    
    
    def file_save(self, event=None):
    
        #self.dataCSV
        #self.openCSV
        #self.openFileName
    
        new_file_name = tkf.asksaveasfilename()
        if new_file_name:
             self.openFileName = new_file_name
        if  self.openCSV is False:
            msg.showerror("No File Open", "Please open an csv file first")
            return
    
        #with open(self.active_ini_filename, "w") as ini_file:
        #    self.active_ini.write(ini_file)
        #saveCSV(dataCSV, openFileName)
    
        try:
            with open(self.openFileName, mode='w', newline='') as exit_file:
                csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #for i in range(I):
                    #print(dataNP[i])
                    #csv_writer.writerow(dataNP[i])
                for item in self.treeviewA.get_children():
                    item_text = self.treeviewA.item(item, "values")
                    temp = list(item_text)
                    print(temp[1:])
                    csv_writer.writerow(temp[1:])
        except:
            with open(self.openFileName, mode='w') as exit_file:
                csv_writer = csv.writer(exit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #csv_writer.writerow(['&Wall', '0/startX', '1/startY', '2/endX', '3/endY', '4/arrow', '5/shape', '6/inComp'])
                #index_temp=0
                #for i in range(I):
                    #print(dataNP[i])
                    #csv_writer.writerow(dataNP[i])
                for item in self.treeviewA.get_children():
                    item_text = self.treeviewA.item(item, "values")
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
    
    def set_cell_value(self, event): # double click to edit the item
    
        for item in self.treeviewA.selection():
    
            #item = I001
            item_text = self.treeviewA.item(item, "values")
            print(item_text)
            print(int(item_text[0]))
            print(item)
            #print(item_text[0:2])  # Output the column number selected by users
    
        column= self.treeviewA.identify_column(event.x)# column
        row = self.treeviewA.identify_row(event.y)  # row
    
        cn = int(str(column).replace('#',''))
        rn = int(str(row).replace('I',''), base=16)
        
        print("cn:", column, cn)
        print("rn:", row, rn)
    
        rn = int(item_text[0])
        print("line number:", rn)
    
        #entryedit = Text(root,width=10+(cn-1)*16,height = 1)
        entryedit = Text(self.root, width = 20, height = 2)
        #entryedit = Entry(root,width=10)
        entryedit.insert(END, str(rn)+self.columns[cn-1]+'= '+str(item_text[cn-1]))
        #entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
        entryedit.pack()
        #lb= Label(root, text = str(rn)+self.columns[cn-1])
        #lb.pack()
    
        def saveedit():
            
            #self.dataCSV
            try:
                temp=entryedit.get(0.0, 'end').split('=')
                self.treeviewA.set(item, column=column, value=temp[1].strip())
                #dataCSV[rn-1][cn-2]=temp[1].strip()
                #print(dataCSV) #[rn, cn])
            except:
                self.treeviewA.set(item, column=column, value=entryedit.get(0.0, 'end').strip())
                #dataCSV[rn-1][cn-2]=entryedit.get(0.0, 'end').strip()
                #print(dataCSV) #[rn, cn])
            #lb.destroy()
            entryedit.destroy()
            okb.destroy()
    
        okb = Button(self.root, text = str(rn)+self.columns[cn-1]+':OK', width=9, command=saveedit)
        okb.pack() #place(x=90+(cn-1)*130,y=2+rn*20)
        
    
    def addrow(self):
    
        for item in self.treeviewA.selection():
            #item = I001
            item_text = self.treeviewA.item(item, "values")
            print(item_text)
            print(item)
            print(item.index)
            #print(item_text[0:2])  # Output the column number selected by users
        try:
            #rn = int(str(item).replace('I',''), base=16)
            rn = int(item_text[0])
        except:
            rn = int(len(self.dataCSV))
            
        try:
            self.treeviewA.insert('', int(rn), values=item_text) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
        except:
            self.treeviewA.insert('', int(rn), values=(int(rn)+1))
        #self.treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
        self.updateRowNum()
        self.treeviewA.update()
    
        #newb.place(x=120, y=20) #y=(len(name)-1)*20+45)
        #newb.update()
        
    def deleterow(self):
        
        #self.dataCSV
        for item in self.treeviewA.selection():
            #item = I001
            item_text = self.treeviewA.item(item, "values")
            print(item_text)
            print(item)
    
        #cn = int(str(column).replace('#',''))
        rn = int(str(item).replace('I',''), base=16)
        print(rn)
        try:
            self.treeviewA.delete(item) #dataCSV[i][3], dataCSV[i][4], dataCSV[i][5],  dataCSV[i][6], dataCSV[i][7], dataCSV[i][8], dataCSV[i][9], dataCSV[i][10]))
        except:
            self.treeviewA.delete(item)
        #self.treeviewA.insert('', len(name)-1, values=(name[len(name)-1], pos[len(name)-1], vel[len(name)-1]))
        self.updateRowNum()
        self.treeviewA.update()
    
    
    def updateRowNum(self):
        i=1
        for item in self.treeviewA.get_children():
            item_text = self.treeviewA.item(item, "values")
            self.treeviewA.set(item, column=0, value=str(i))
            i=i+1
        return None
    
    
    #newb = Button(root, text='New Agent', width=20, command=addrow)
    #newb.place(x=120,y=20 ) #(len(name)-1)*20+45)
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    editor = Editor()
    editor.start()
