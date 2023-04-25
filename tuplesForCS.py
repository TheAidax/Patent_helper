from difflib import *
from importlib.resources import path
import sys


def makingTuples():
    
    pathToParent = sys.argv[1]
    pathToCIP = sys.argv[2]

    openParent = open(pathToParent,"r")
    openCIP = open(pathToCIP,"r")

######       Use these if you wanna debug       #######
    #pathToParent = open("test1.txt","r")
    #pathToCIP = open("test2.txt","r")

    #openParent = pathToParent
    #openCIP = pathToCIP




    #global listoftuples
    #global listforlist
    
    #global linestatus           #can be either: new, deleted, or common
    #global similarityratio
    
    #global commonlinenum        #for highlighting deleted matter   (purple)
    #global ciplinenum           #for highlighting new matter       ( blue )
    




    #global flag

    parent_data = openParent.readline()
    CIP_data = openCIP.readline()

    CIPLineNum = 0
    commonLineNum = 0

    listOfTuples = []
    listForList = []
    

    while parent_data != '' or CIP_data != '':
        flag = 0
    
        #This if statement catches new matter in the CIP
        if SequenceMatcher(None,parent_data,CIP_data).quick_ratio() < 0.5:
            flag = 1
            lineStatus = "new"
            similarityRatio = SequenceMatcher(None,parent_data,CIP_data).ratio()
        
            
        #this if statement catches deleted matter in the parent doc
        elif SequenceMatcher(None,parent_data,CIP_data).quick_ratio() <= 0.8 and SequenceMatcher(None,parent_data,CIP_data).quick_ratio() >= 0.5:
            flag = 2
            lineStatus = "deleted"
            similarityRatio = SequenceMatcher(None,parent_data,CIP_data).quick_ratio()    
        
        #This else statement catches the common lines
        else:  
            flag = 0
            lineStatus = "common"
            similarityRatio = SequenceMatcher(None,parent_data,CIP_data).quick_ratio()
        

        
        if flag != 1:
            commonLineNum += 1;
            parent_data = openParent.readline()
        
        if flag != 2:    
            CIPLineNum += 1
            CIP_data = openCIP.readline()


        ###               save material to tuple          ###

        if lineStatus == 'common':
            listForList = [lineStatus,similarityRatio,commonLineNum]
        else:
            listForList = [lineStatus,similarityRatio,CIPLineNum]
        print(listForList)

        listOfTuples.append(listForList)


    print('Process Completed')

 
    # closing files
    openParent.close()                                      
    openCIP.close()
    #newFile.close()
    return listOfTuples


if __name__ == "__main__":
    makingTuples()

print(makingTuples())


#PatentComparison("test1.txt","test2.txt")


