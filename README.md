
### Universal csv array reader

The source code was written for both Python 3.x, and python2.7. Tkinter and Numpy are required to run the source code.  The csv data could be visualized with matplotlib.  This ongoing project could be useful for our simulation platform of crowdEgress.  So far there are two version of the programe.  One version is named by treeviewCSV_crowdEgress.py, which is especially designed to prepare the input csv data for crowdEgress.  Another version is named by treeviewCSV_universal.py, which is distributed as a general version for csv data editor, and it could be embedded into other program easily.    

### How-To: 
Open a console in your operating system and run python command as below.  
python treeviewCSV_CrowdEgress.py
python treeviewCSV_universal.py

(1) When tkinter window (GUI) is activated, please select a csv input file.  
 --> In the menu bar please select <File>, and select <Open> to open a csv file, and csv data should be visualized in GUI 
 --> edit csv data in GUI 
 --> quit the program
The program has been tested in windows and linux OS, but not yet on macOS.  If you find any bugs when running the program in macOS, please report the bugs by using issue trackers.   



Please take a look at the user guide and examples for details.  

(2) When pygame screen is activated, press certain keys to adjust the display features:  
Use pageup/pagedown to zoom in/zoom out the entities.  
Use space key to pause the simulation.  
Use arrows to move the entities vertically or horizonally in screen.    



