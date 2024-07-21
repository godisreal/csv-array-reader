
#-----------------------------------------------------------------------
# Copyright (C) 2020, All rights reserved
#
# Peng Wang
#
#-----------------------------------------------------------------------
#=======================================================================
# -*-coding:utf-8-*-
# Author: WP
# Email: wp2204@gmail.com

import os, sys
import numpy as np
#from math_func import *
from math import *
#from config import *
import re
import random
import csv
#from ctypes import *
import struct
import time
try:
    import matplotlib.pyplot as plt
except:
    print("Warning: matplotlib cannot be imported.  Unable to plot figures!")
    if sys.version_info[0] == 2: 
        raw_input("Please check!")
    else:
        input("please check!")


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

        dataOK = dataFeatures[IPedStart : IPedEnd]
        return dataOK, IPedStart, IPedEnd

    #data_result = np.array(dataOK)
    #return data_result[1:, 1:]
    

# This function is not used in this program
def readCSV(fileName, mode='float'):
    
    # read .csv file
    csvFile = open(fileName, "r")
    reader = csv.reader(csvFile)
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
    print (dataNP)
    print('np.shape(dataNP)', np.shape(dataNP))
    print('\n')

    #print(strData[1:,1:])
    csvFile.close()	
    
    if mode=='string':
        print (dataNP[1:, 1:])
        return dataNP[1:, 1:]
    
    if mode=='float':
        
        #print dataNP[1:, 1:]
        (I, J) = np.shape(dataNP)
        #print "The size of tha above matrix:", [I, J]
        #print "The effective data size:", [I-1, J-1]
        matrix = np.zeros((I, J))
        #print matrix

        for i in range(1,I):
            for j in range(1,J):
                matrix[i,j] = float(dataNP[i,j])

    print (matrix[1:, 1:])
    return matrix[1:, 1:]
    

def arr1D_2D(data, debug=True):
    #data is in type of 1D array, but it is actually a 2D data format.  
    
    NRow = len(data)
    NColomn = len(data[1])
    matrix = np.zeros((NRow, NColomn), dtype='|S20')
    for i in range(NRow):
            for j in range(NColomn):
                matrix[i,j] = data[i][j]
    if debug:
        print('Data in 2D array:\n', matrix)
        
    return matrix


def readFloatArray(tableFeatures, NRow, NColomn, debug=True):

    #tableFeatures, LowerIndex, UpperIndex = getData("newDataForm.csv", '&Ped2Exit')
    matrix = np.zeros((NRow, NColomn))
    for i in range(NRow):
            for j in range(NColomn):
                try:
                    matrix[i,j] = float(tableFeatures[i+1][j+1])
                except:
                    matrix[i,j] = float(0.0)
    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', matrix)
    return matrix

def readAgent2Exit(tableFeatures, NRow, NColomn, debug=True):

    #tableFeatures, LowerIndex, UpperIndex = getData("newDataForm.csv", '&Ped2Exit')
    matrixA2E = np.zeros((NRow, NColomn))
    matrixKW = np.zeros((NRow, NColomn))
    for i in range(NRow):
            for j in range(NColomn):
                if tableFeatures[i+1][j+1] and tableFeatures[i+1][j+1] != '0':
                    
                    temp=re.split(r'\s*[;\|\s]\s*', tableFeatures[i+1][j+1])
                    try:
                        matrixA2E[i,j] = float(temp[0])
                    except:
                        matrixA2E[i,j] = float(0.0)
                        
                    try:
                        matrixKW[i,j] = bool(temp[1])
                    except:
                        matrixKW[i,j] = False
                else:
                    matrixA2E[i,j] = 0.0
                    matrixKW[i,j] = False
                    
                # Coordinate consistency of matrixA2E and matrixKW
                if matrixA2E[i,j] > 0.0:
                    matrixKW[i,j] = True

    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', matrixA2E, matrixKW)
    return matrixA2E #, matrixKW


def readGroupCABD(tableFeatures, NRow, NColomn, debug=True):

    # NRow and NColomn are the size of data to be extracted from tableFeatures
    matrixC = np.zeros((NRow, NColomn))
    matrixA = np.zeros((NRow, NColomn))
    matrixB = np.zeros((NRow, NColomn))
    matrixD = np.zeros((NRow, NColomn))
    
    for i in range(NRow):
        for j in range(NColomn):
            
            if tableFeatures[i+1][j+1] and tableFeatures[i+1][j+1] != '0':
                try:
                    #temp=re.split(r'[\s\/]+', tableFeatures[i+1][j+1])
                    temp=re.split(r'\s*[;\|\s]\s*', tableFeatures[i+1][j+1])
                    matrixC[i,j] = float(temp[0])
                    matrixA[i,j] = float(temp[1])
                    matrixB[i,j] = float(temp[2])
                    matrixD[i,j] = float(temp[3])
                except:
                    print("Error in reading group data!")
                    input("Please check!")
                    matrixC[i,j] = 0.0
                    matrixA[i,j] = 0.0
                    matrixB[i,j] = 0.0
                    matrixD[i,j] = 0.0
            else:
                matrixC[i,j] = 0.0
                matrixA[i,j] = 0.0
                matrixB[i,j] = 0.0
                matrixD[i,j] = 0.0
                
    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', matrixC, matrixA, matrixB, matrixD)
    return matrixC, matrixA, matrixB, matrixD


def readGroupABD(tableFeatures, NRow, NColomn, debug=True):

    # NRow and NColomn are the size of data to be extracted from tableFeatures
    matrixA = np.zeros((NRow, NColomn))
    matrixB = np.zeros((NRow, NColomn))
    matrixD = np.zeros((NRow, NColomn))
    
    for i in range(NRow):
        for j in range(NColomn):
            
            if tableFeatures[i+1][j+1] and tableFeatures[i+1][j+1] != '0':
                try:
                    #temp=re.split(r'[\s\/]+', tableFeatures[i+1][j+1])
                    temp=re.split(r'\s*[;\|\s]\s*', tableFeatures[i+1][j+1])
                    matrixA[i,j] = float(temp[0])
                    matrixB[i,j] = float(temp[1])
                    matrixD[i,j] = float(temp[2])
                except:
                    print("Error in reading group data!")
                    input("Please check!")
                    matrixA[i,j] = 0.0
                    matrixB[i,j] = 0.0
                    matrixD[i,j] = 0.0
            else:
                matrixA[i,j] = 0.0
                matrixB[i,j] = 0.0
                matrixD[i,j] = 0.0
                
    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', matrixA, matrixB, matrixD)
    return matrixA, matrixB, matrixD
    

def readGroupC(tableFeatures, NRow, NColomn, debug=True):
    # NRow and NColomn are the size of data to be extracted from tableFeatures
    matrixC = np.zeros((NRow, NColomn))
    if tableFeatures[i+1][j+1] and tableFeatures[i+1][j+1] != '0':
        try:    
            matrixC[i,j] = float(tableFeatures[i+1][j+1])        
        except:
            print("Error in reading group data!")
            input("Please check!")
            matrixC[i,j] = 0.0
    else:
        matrixC[i,j] = 0.0
                
    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', matrixC)
    return matrixC


def readArrayIndex(tableFeatures, NRow, NColomn, index=0, iniX=1, iniY=1, debug=True):

    #tableFeatures, LowerIndex, UpperIndex = getData("newDataForm.csv", '&Ped2Exit')

    #(dataX, dataY) = np.shape(tableFeatures)
    #NRow = dataX - iniX
    #NColomn = dataY - iniY

    # NRow and NColomn are the size of data to be extracted from tableFeatures
    matrixC = np.zeros((NRow, NColomn))
    #matrixB = np.zeros((NRow, NColomn))
    #matrixD = np.zeros((NRow, NColomn))
    
    for i in range(NRow):
        for j in range(NColomn):
            try:
                if tableFeatures[i+iniX][j+iniY] and tableFeatures[i+iniX][j+iniY] != '0':
                    #temp=re.split(r'[\s\/]+', tableFeatures[i+1][j+1])
                    temp=re.split(r'\s*[;\|\s]\s*', tableFeatures[i+iniX][j+iniY])
                    matrixC[i,j] = float(temp[index])
                    #matrixB[i,j] = float(temp[1])
                    #matrixD[i,j] = float(temp[2])
                else:
                    matrixC[i,j] = 0.0
                    #matrixB[i,j] = 1.0
                    #matrixD[i,j] = 1.0
            except:
                print("Error in reading data!")
                input("Please check!")
                matrixC[i,j] = 0.0
                #matrixB[i,j] = 1.0
                #matrixD[i,j] = 1.0
                
    if debug:
        print(tableFeatures, '\n')
        print('Data in Table:', '\n', 'Index Number:', index, '\n', matrixC, '\n\n') #, matrixB, matrixD)
    return matrixC #, matrixB, matrixD



def readCrowdEgressCSV(FileName, debug=True, marginTitle=1, ini=1):

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
    
    return agentFeatures, obstFeatures, exitFeatures, doorFeatures




##############################################
# This function will be used to read CHID from FDS input file
def readCHID(FileName):

    findHEAD=False
    for line in open(FileName):
        if re.match('&HEAD', line):
            findHEAD=True
        if  findHEAD:
            if re.search('CHID', line):
                temp1=line.split('CHID')
                line1=temp1[1].strip().strip('=').strip()
                temp2 =  re.split(r'[\s\,]+', line1)
                keyInfo = temp2[0]
                return keyInfo
            if re.search('/', line):
                findHEAD = False
    return None

# Find the first &MESH line in FDS input file and return the value
def readMesh(FileName):
    findMESH=False
    for line in open(FileName):
        if re.match('&MESH', line):
            findMESH=True
        if  findMESH:
            if re.search('IJK', line):
                temp1=line.split('IJK')
                line1=temp1[1].strip().strip('=').strip()
                temp2 =  re.split(r'[\s\,]+', line1)
                xpoints = temp2[0]
                ypoints = temp2[1]
            if re.search('XB', line):
                temp1=line.split('XB')
                line1=temp1[1].strip().strip('=').strip()
                temp2 =  re.split(r'[\s\,]+', line1)
                xmax = temp2[1]-temp2[0]
                ymax = temp2[3]-temp2[2]
            if re.search('/', line):
                findMESH = False
                return xpoints, ypoints, xmax, ymax
                # Only find the first &MESH line
                # The second or other MESH lines are ignored
    return None


def readTEnd(FileName):
    findTIME=False
    for line in open(FileName):
        if re.match('&TIME', line):
            findTIME=True
        if  findTIME:
            if re.search('T_END', line):
                temp1=line.split('T_END')
                line1=temp1[1].strip().strip('=').strip()
                temp2 =  re.split(r'[\s\,]+', line1)
                keyInfo = temp2[0]
                return keyInfo   # Return a string
            if re.search('/', line):
                findTIME = False
            
    keyInfo=0.0    #If T_END is not found, then return 0.0
    return keyInfo
    #return None
    

# To be added
def readKeyOnce(FileName, Title, Key):
    findTitle=False
    for line in open(FileName):
        if re.match(Title, line):
            findTitle=True
        if  findTitle:
            if re.search(Key, line):
                temp1=line.split(Key)
                line1=temp1[1].strip().strip('=').strip()
                temp2 =  re.split(r'[\s\,]+', line1)
                keyInfo = temp2[0]
                findTitle=False
                return keyInfo
            #if re.match(Title, line)==False and re.match('&', line):
            if re.search('/', line):
                findTitle = False
    return None



### A illustration of OBST PATH and EXIT in RECTANGULAR SHAPE
##############################
### p1-----------------p4  ###
###  |                  |  ###
###  |                  |  ###
###  |                  |  ###
### p2-----------------p3  ###
##############################
            
##############################################
# This function will be used to read OBST from FDS input file
def readOBST(FileName, Keyword='&OBST', Zmin=0.0, Zmax=3.0, outputFile=None, debug=True):
    #fo = open("OBSTout.txt", "w+")
    obstFeatures = []
    findOBST=False
    for line in open(FileName):
        if re.match(Keyword, line):
            findOBST=True
        if  findOBST:
            if re.search('XB', line):
                temp1=line.split('XB')
                dataXYZ=temp1[1].strip().strip('=').strip()
                #line1=temp1[1].strip('= ')
                #temp =  line1.split('=')
                #dataXYZ = temp[1].strip()
                coords = re.split(r'[\s\,]+', dataXYZ)
                print(coords)
                obstFeature = []
                obstFeature.append(float(coords[0]))
                obstFeature.append(float(coords[2]))
                obstFeature.append(float(coords[1]))
                obstFeature.append(float(coords[3]))
                obstFeature.append(float(coords[4]))
                obstFeature.append(float(coords[5].rstrip('/')))
                obstFeatures.append(obstFeature)
                findOBST=False

            if debug:
                print (line, '\n', obstFeature)
                #print >>fo, line
                #print >>fo, obstFeature

            #print >>fo, 'test\n'
            #print >>fo, 'OBST Features\n'
            #print >>fo, obstFeatures
    
    walls = []
    index = 0
    for obstFeature in obstFeatures:
        if obstFeature[4]<Zmin and obstFeature[5]<Zmin:
            continue
        if obstFeature[4]>Zmax and obstFeature[5]>Zmax:
            continue
        wall = obst()
        wall.params[0]= float(obstFeature[0])
        wall.params[1]= float(obstFeature[1])
        wall.params[2]= float(obstFeature[2])
        wall.params[3]= float(obstFeature[3])
        wall.arrow = 0
        wall.inComp = 1
        wall.mode = 'rect'
        wall.oid = index
        index = index+1
        walls.append(wall)

    if outputFile is not None:
        updateWallData(walls, outputFile)
    return walls


#######################################################
# This function will be used to read HOLE or DOOR from FDS input file
def readPATH(FileName, Keyword='&HOLE', Zmin=0.0, Zmax=3.0, outputFile=None, debug=True):
    #fo = open("HOLEout.txt", "w+")
    holeFeatures = []
    
    findPATH=False
    findPATH_XB=False
    findPATH_IOR=False
    for line in open(FileName):
        if re.match(Keyword, line):
            findPATH=True
            findPATH_XB=True
            findPATH_IOR=True
            
        if findPATH:
            if re.search('XB', line):
                temp1=line.split('XB')
                dataXYZ=temp1[1].strip().strip('=').strip()
                #line1=temp1[1]
                #temp =  line1.split('=')
                #dataXYZ = temp[1].strip()    
                coords = re.split(r'[\s\,]+', dataXYZ)
                
        #if findPATH and findPATH_IOR:
        #    if re.search('IOR', line):
        #        temp1=line.split('IOR')
        #        dataXYZ=temp1[1].strip().strip('=').strip()
        #        result_IOR = re.split(r'[\s\,]+', dataXYZ)              
        #if findPATH and not findPATH_XB and not findPATH_IOR:            
                holeFeature = []
                holeFeature.append(float(coords[0]))
                holeFeature.append(float(coords[2]))
                holeFeature.append(float(coords[1]))
                holeFeature.append(float(coords[3]))
                holeFeature.append(float(coords[4]))
                holeFeature.append(float(coords[5].rstrip('/')))
                holeFeatures.append(holeFeature)
                findPATH=False

                if debug:
                    print (line, '\n', holeFeature)
                    #print >>fo, line
                    #print >>fo, holeFeature

                #print >>fo, 'test\n'
                #print >>fo, 'HOLE Features\n'
                #print >>fo, holeFeatures

    doors = []
    index = 0
    for holeFeature in holeFeatures:
        if holeFeature[4]<Zmin and holeFeature[5]<Zmin:
            continue
        if holeFeature[4]>Zmax and holeFeature[5]>Zmax:
            continue
        door = passage()
        door.params[0]= float(holeFeature[0])
        door.params[1]= float(holeFeature[1])
        door.params[2]= float(holeFeature[2])
        door.params[3]= float(holeFeature[3])
        door.arrow = 0
        door.oid = index
        index = index+1
        door.inComp = 1
        door.exitSign = 0
        door.pos = (np.array([door.params[0], door.params[1]]) + np.array([door.params[2], door.params[3]]))*0.5
        doors.append(door)
        
    if outputFile: 
        updateDoorData(doors, outputFile)

    return doors


##############################################
# This function will be used to read EXIT from FDS input file
def readEXIT(FileName, Keyword='&EXIT', Zmin=0.0, Zmax=3.0, outputFile=None, debug=True):
    #fo = open("EXITout.txt", "w+")
    exitFeatures = []
    findEXIT=False
    findEXIT_XB=False
    findEXIT_IOR=False
    
    for line in open(FileName):
        if re.match(Keyword, line):
            findEXIT=True
            findEXIT_XB=True
            findEXIT_IOR=True
            
        if findEXIT:
            if re.search('XB', line):
                temp1=line.split('XB')
                dataXYZ=temp1[1].strip().strip('=').strip()
                #line1=temp1[1]
                #temp =  line1.split('=')
                #dataXYZ = temp[1]
                #coords = dataXYZ.split(',')
                coords = re.split(r'[\s\,]+', dataXYZ)
                
        #if findEXIT and findEXIT_IOR:
        #    if re.search('IOR', line):
        #        temp1=line.split('IOR')
        #        dataXYZ=temp1[1].strip().strip('=').strip()
        #        result_IOR = re.split(r'[\s\,]+', dataXYZ)              
        #if findEXIT and not findEXIT_XB and not findEXIT_IOR:
                exitFeature = []
                exitFeature.append(float(coords[0]))
                exitFeature.append(float(coords[2]))
                exitFeature.append(float(coords[1]))
                exitFeature.append(float(coords[3]))
                exitFeature.append(float(coords[4]))
                exitFeature.append(float(coords[5].rstrip('/')))
                exitFeatures.append(exitFeature)
                findEXIT=False

                if debug:
                    print (line, '\n', exitFeature)
                    #print >>fo, line
                    #print >>fo, exitFeature

            
                #print >>fo, 'test\n'
                #print >>fo, 'EXIT Features\n'
                #print >>fo, exitFeatures

        #if re.search('/', line): ???  Not used
        #    findEXIT=False
        #    findEXIT_XB=False
        #    findEXIT_IOR=False

    exits = []
    index = 0
    for exitFeature in exitFeatures:
        if exitFeature[4]<Zmin and exitFeature[5]<Zmin:
            continue
        if exitFeature[4]>Zmax and exitFeature[5]>Zmax:
            continue
        exit = passage()
        exit.params[0]= float(exitFeature[0])
        exit.params[1]= float(exitFeature[1])
        exit.params[2]= float(exitFeature[2])
        exit.params[3]= float(exitFeature[3])
        exit.arrow = 0   #  This need to be improved
        exit.oid = index
        exit.inComp = 1
        exit.exitSign = 0
        exit.pos = (np.array([exit.params[0], exit.params[1]]) + np.array([exit.params[2], exit.params[3]]))*0.5

        # In FDS input file exit is a planary surface and agents go into the surface
        # In our simulaiton exit is a rectangular area and agent reach the area
        if exit.params[0]==exit.params[2]:
            exit.params[0]=exit.params[0]-0.3
            exit.params[2]=exit.params[2]+0.3
            exitFeature[0]=exitFeature[0]-0.3
            exitFeature[2]=exitFeature[2]+0.3
            
            
        if exit.params[1]==exit.params[3]:
            exit.params[1]=exit.params[1]-0.3
            exit.params[3]=exit.params[3]+0.3
            exitFeature[1]=exitFeature[1]-0.3
            exitFeature[3]=exitFeature[3]+0.3
            
        exits.append(exit)
        index = index+1

    if outputFile:
        updateExitData(exits, outputFile)              
    return exits


def updateDoorData(doors, outputFile, inputFile=None):
    try:
        with open(outputFile, mode='a+', newline='') as door_test_file:
            csv_writer = csv.writer(door_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['DOOR/PATH data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Door', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for door in doors:
                csv_writer.writerow(['--', str(door.params[0]), str(door.params[1]), str(door.params[2]), str(door.params[3]), str(door.arrow), str(door.mode), str(door.inComp)])
                index_temp=index_temp+1
    except:
        with open(outputFile, mode='wb+') as door_test_file:
            csv_writer = csv.writer(door_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['DOOR/PATH data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Door', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for door in doors:
                csv_writer.writerow(['--', str(door.params[0]), str(door.params[1]), str(door.params[2]), str(door.params[3]), str(door.arrow), str(door.mode), str(door.inComp)])
                index_temp=index_temp+1
                

def updateExitData(doors, outputFile, inputFile=None):
    try:
        with open(outputFile, mode='a+', newline='') as exit_test_file:
            csv_writer = csv.writer(exit_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['EXIT data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Exit', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for door in doors:
                csv_writer.writerow(['--', str(door.params[0]), str(door.params[1]), str(door.params[2]), str(door.params[3]), str(door.arrow), str(door.mode), str(door.inComp)])
                index_temp=index_temp+1
    except:
        with open(outputFile, mode='wb+') as exit_test_file:
            csv_writer = csv.writer(exit_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['EXIT data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Exit', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for door in doors:
                csv_writer.writerow(['--', str(door.params[0]), str(door.params[1]), str(door.params[2]), str(door.params[3]), str(door.arrow), str(door.mode), str(door.inComp)])
                index_temp=index_temp+1
            

def updateWallData(walls, outputFile, inputFile=None):
    try:
        with open(outputFile, mode='a+', newline='') as wall_test_file:
            csv_writer = csv.writer(wall_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['WALL/OBST data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Wall', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for wall in walls:
                csv_writer.writerow(['--', str(wall.params[0]), str(wall.params[1]), str(wall.params[2]), str(wall.params[3]), str(wall.arrow), str(wall.mode), str(wall.inComp)])
                index_temp=index_temp+1
    except:
        with open(outputFile, mode='wb+') as wall_test_file:
            csv_writer = csv.writer(wall_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['WALL/OBST data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            csv_writer.writerow(['&Wall', '1/startX', '2/startY', '3/endX', '4/endY', '5/arrow', '6/shape', '7/inComp'])
            index_temp=0
            for wall in walls:
                csv_writer.writerow(['--', str(wall.params[0]), str(wall.params[1]), str(wall.params[2]), str(wall.params[3]), str(wall.arrow), str(wall.mode), str(wall.inComp)])
                index_temp=index_temp+1
            

# Not used after the flow solver is integrated into our program
# This function was originally developed to dump exit2door data in TestGeom
def updateExit2Doors(exit2doors, outputFile, inputFile=None):
    (I, J) = np.shape(exit2doors)
    #print "The size of exit2door:", [I, J]
    #dataNP = np.zeros((I+1, J+1))

    dataNP=[]
    for i in range(I+1):
        row=[]
        if i==0:
            row.append('&Exit2Door')
            for j in range(1, J+1):
                row.append('DoorID'+str(j-1))
        else:
            row.append('ExitID'+str(i-1))
            for j in range(1, J+1):
                row.append(str(int(exit2doors[i-1, j-1])))
            
        dataNP.append(row)

    #dataNP[1:, 1:] = exit2doors
    #np.savetxt(fileName, dataNP, delimiter=',', fmt='%s')   #'2darray.csv'
    try:
        with open(outputFile, mode='a+', newline='') as exit2door_file:
            csv_writer = csv.writer(exit2door_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['exit2door data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            for i in range(I+1):
                #print(dataNP[i])
                csv_writer.writerow(dataNP[i])
    
    except:
        with open(outputFile, mode='wb+') as exit2door_file:
            csv_writer = csv.writer(exit2door_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([''])
            if inputFile is not None:
                csv_writer.writerow([inputFile])
            csv_writer.writerow(['exit2door data in TestGeom: '])
            csv_writer.writerow(['time:', time.strftime('%Y-%m-%d_%H_%M_%S')])
            #csv_writer.writerow(['&Wall', '0/startX', '1/startY', '2/endX', '3/endY', '4/arrow', '5/shape', '6/inComp'])
            #index_temp=0
            for i in range(I+1):
                csv_writer.writerow(dataNP[i])
            #for wall in walls:
            #    csv_writer.writerow(['--', str(wall.params[0]), str(wall.params[1]), str(wall.params[2]), str(wall.params[3]), str(wall.arrow), str(wall.mode), str(wall.inComp)])
            #    index_temp=index_temp+1
    
    


##############################################################
# The function writeFRec is modified from Topi's work
# python script: readFRec (by Topi on Google Forum)
# readFRec: Read fortran record, return payload as bytestring
##############################################################
#
def writeFRec(infile, fmt, data):
    len1 = np.size(data)
    if len1==0 or data is None:
        #len2=infile.read(4)
        #infile.write(0x00)
        temp = struct.pack('@I', 0)
        infile.write(temp)
    
        return None
    
    #if fmt=='s':
        #result  = struct.pack('@I', data.encode())
    #    infile.write(data.encode())
    # Not try data.encode().  Use standard format to write data
        
    fmt2 = str(len1)+fmt
    num  = len1 * struct.calcsize(fmt)
    
    # length of the data
    num2   = struct.pack('@I', num)
    infile.write(num2)
    
    # Modified on 2022 Apr2: Handle string type differently from int and float type
    if fmt=='s':
        result = struct.pack(fmt, data.encode())
        infile.write(result)
    
        # End symbol
        temp = struct.pack('@I', 0)
        infile.write(temp)
        return "write a string"

    # Write data
    for i in range(len1):
        result = struct.pack(fmt, data[i])
        infile.write(result)
    
    # End symbol
    temp = struct.pack('@I', 0)
    infile.write(temp)
    

    
#Read fortran record, return payload as bytestring
def readFRec(infile,fmt):
    len1   = infile.read(4)
    if not len1:
        return None
    len1   = struct.unpack('@I', len1)[0]

    if len1==0:
        len2=infile.read(4)
        return None
    num    = int(len1/struct.calcsize(fmt))
    fmt2   = str(num)+fmt
    if num>1:
        result = struct.unpack(fmt2,infile.read(len1))
    else:
        result = struct.unpack(fmt2,infile.read(len1))[0]
    len2   = struct.unpack('@I', infile.read(4))[0]
    if fmt == 's':
        result=result[0] #.rstrip()
    return result


#################################
# The function readPRTfile
def readPRTfile(fname, max_time=np.Inf, mode='evac'):

    fin = open(fname,'rb')
    #if wrtxt:
    #    temp = fname.split('.prt5')
    #    outfile = open(temp[0] + ".txt", "w")
    
    one_integer=readFRec(fin,'I')  #! Integer 1 to check Endian-ness
    version=readFRec(fin,'I')       # FDS version number
    n_part=readFRec(fin,'I')        # Number of PARTicle classes
    #print(n_part)
    q_labels = []
    q_units  = []
    for npc in range(0,n_part):
        n_quant,zero_int=readFRec(fin,'I')  # EVAC_N_QUANTITIES, ZERO_INTEGER
        for nq in range(0,n_quant):
            smv_label=readFRec(fin,'s')
            #print(smv_label)
            units    =readFRec(fin,'s')
            q_units.append(units)  
            q_labels.append(smv_label)
    #if wrtxt:
    #    outfile.write("one_integer:" + str(one_integer) + "\n")    
    #    outfile.write("n_part:" + str(n_part) + "\n") 
    #    outfile.write("n_quant:" + str(n_quant) + "\n")
        
    Q=[]
    T  = []
    #diam =[] ??? Not used in this program
    XYZ = []
    TAG = []
    while True:

        Time  = readFRec(fin,'f')  # Time index
        if Time == None or Time>max_time:
            break
        nplim = readFRec(fin,'I')  # Number of particles in the PART class
        if nplim>0:
            xyz  = np.array(readFRec(fin,'f'))
            tag  = np.array(readFRec(fin,'I'))
            q    = np.array(readFRec(fin,'f'))

            #print >> outfile, "g", q, "\n"
            if mode=='evac':
                xyz.shape = (7,nplim) # evac data: please check dump_evac() in evac.f90
            else: 
                xyz.shape = (3,nplim) # particle data: please check dump_part() in dump.f90
            
            q.shape   = (n_quant, nplim)
            
            #if wrtxt:
            #    outfile.write("Time:" + str(Time) + "\n")
            #    outfile.write("xyz:" + str(xyz) + "\n") 
            #    outfile.write("tag:" + str(tag) + "\n")           
            #    outfile.write( "q:" + str(q) + "\n")

            # process timestep data
            T.append(Time)
            XYZ.append(xyz)
            TAG.append(tag)
            Q.append(q)
        else:
            tmp = fin.read(24)
    
    fin.close()
    #if wrtxt:
    #    outfile.close()
    #np.savez( outfn + ".npz", T, XYZ, TAG, Q)
    #return (np.array(T),np.hstack(Q),q_labels,q_units)
    return T, XYZ, TAG, Q, n_part, version, n_quant


if __name__ == '__main__':

    test = readCSV_base(r"/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv")
    print(test)
    doorFeatures = getData(r"/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv", '&Door')
    
    #print (doorFeatures)
    print (np.shape(doorFeatures))

    pedFeatures = getData(r"/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv", '&Ped')
    #print (pedFeatures)
    print (np.shape(pedFeatures))

    agents = readAgents("/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv")
    walls = readWalls("/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv")
    doors = readDoors("/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv")
    exits = readExits("/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv")
    
    print ('Length of agents:', len(agents))
    print ('Length of walls:', len(walls))
    
    ped2ExitFeatures, LowerIndex, UpperIndex = getData(r"/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv", '&Ped2Exit')
    #print (ped2ExitFeatures)
    matrix = np.zeros((len(agents), len(exits)))
    
    for i in range(len(agents)):
            for j in range(len(exits)):
                matrix[i,j] = float(ped2ExitFeatures[i+1][j+1])
    print ('matrix', matrix)

    #Exit2DoorFeatures, LowerIndex, UpperIndex = getData("newDataForm.csv", '&Exit2Door')
    #print (Exit2DoorFeatures)
    #matrix = np.zeros((len(exits), len(doors)))
    #for i in range(len(exits)):
    #        for j in range(len(doors)):
    #            matrix[i,j] = float(Exit2DoorFeatures[i+1][j+1])
    #print ('matrix', matrix)
    
        #for index in range(Num_Data):
        #if dataFeatures[0,index]=='&Ped':
        #    IPedStart=index
        #    while dataFeatures[0,index]!='':
        #        index=index+1
        #    IPedEnd=index

    #agentFeatures = dataFeatures[IPedStart : IPedEnd]
    #[Num_Agents, Num_Features] = np.shape(agentFeatures)

    #doors = readDoors("doorData2019.csv", True)
    #exits = readExits("doorData2018.csv", True)
    
    # Initialize Desired Interpersonal Distance
    #DFactor_Init = readCSV("D_Data2018.csv", 'float')
    #AFactor_Init = readCSV("A_Data2018.csv", 'float')
    #BFactor_Init = readCSV("B_Data2018.csv", 'float')

    tableFeatures, LowerIndex, UpperIndex = getData(r"/mnt/sda6/gitwork2022/CrowdEgress/examples/ped2023Jan_problem.csv", '&groupB')
    BFactor_Init = readFloatArray(tableFeatures, len(agents), len(agents))
    BFactor_Init

    # Input Data Check
    #[Num_D1, Num_D2]=np.shape(DFactor_Init)
    #[Num_A1, Num_A2]=np.shape(AFactor_Init)
    #[Num_B1, Num_B2]=np.shape(BFactor_Init)

    #print >>f, np.shape(DFactor_Init), [Num_Agents, Num_Agents], '\n'

    print('\n', 'Test Output: exit2door.csv')
    exit2door=np.array([[ 1.0,  1.0,  1.0], [ 1.0,  -1.0,  -2.0], [ 1.0,  1.0,  1.0]])
    #print(exit2door)
    updateExit2Doors(exit2door, 'test_exit2door.csv')
    
    readDoorProb(r'/mnt/sda6/gitwork2022/CrowdEgress/examples/3Doors/ped2023Jan_2023-05-16_02_11_26.txt',0)
    
    
""" Test struct to read and write binary data
    n_part=2
    [n_quant,zero_int]=[1,0]
    f=open('test.bin', 'wb+')
    writeFRec(f, 'I', [1])      #! Integer 1 to check Endian-ness
    writeFRec(f, 'I', [653])    # FDS version number
    writeFRec(f, 'I', [n_part]) # Number of PARTicle classes
    for npc in range(n_part):
        writeFRec(f, 'I', [n_quant, zero_int])
        for nq in range(n_quant):
            smv_label =writeFRec(f,'s', "test")
            units     =writeFRec(f,'s', "Newton")
            #q_units.append(units)  
            #q_labels.append(smv_label)
    x1=[1.0, 2.0, 3.0]
    writeFRec(f, 'f', x1)
    x2=[1,2,3]
    writeFRec(f, 'I', x2)
    x3="abcdefg"
    writeFRec(f, 's', x3)
    f.close()
    
    f=open('test.bin', 'rb')
    testEnd =readFRec(f, 'I')
    ver =readFRec(f, 'I')
    n_part =readFRec(f, 'I')
    y1 = readFRec(f, 'f')
    y2 = readFRec(f, 'I')
    y3 = readFRec(f, 's') 
    print testEnd
    print ver
    print n_part
    print y1
    print y2
    print y3
    
"""
