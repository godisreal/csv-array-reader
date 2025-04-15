
### Universal csv array editor

This is a small-size csv editor developed by Python Treeview/Tkinter, and it could be integrated into any python-based programs for easy data processing. Another version is also provided as a simple text-based csv editor, which use tab (/t) to separate the data elements in csv editor. The source code could be run on Python2 or Python3 with Tkinter. Compared with many table-processing software, this small program will not add many commas at the end of each line because it is specially developed for csv data.  
Comments and feedback are welcome! Have fun!

So far there are two version of the programe.  One version is named by treeviewCSV_generalOO.py and textCSV_edit.py, which is distributed as a general version for csv data editor, and it could be embedded into other program easily. Another special version is named by treeviewCSV_crowdEgress.py, which is especially designed to prepare the input csv data for our simulation platform CrowdEgress.  

### How-To: 
Open a console in your operating system and run python command as below.  
python treeviewCSV_general.py
python textCSV_edit.py
python treeviewCSV_CrowdEgress.py

(1) When tkinter window (GUI) is activated, please select a csv input file.  
 --> In the menu bar please select <File>, and select <Open> or <New> to open a csv file, and csv data should be visualized in GUI 
 --> Edit csv data in GUI by double click on the cell and input the text in the cell.  When a new csv file is created, users need add lines first and then edit the cell in each line.  The line could also be dynamcially added or deleted by either using the commonds in the menubar, or using <Ctrl+A> or <Ctrl+D>.  
 --> Quit the program
The program has been tested in windows and linux OS.  If you find any bugs when running the program, please report the bugs by using issue trackers.   


The major codework was initially learned from a manuscript by David Love.  
Python Tkinter By Example, January 18, 2018

