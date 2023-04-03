from difflib import *

def PatentComparison(pathToParent,pathToCIP):
    
    openParent = open(pathToParent,"r")
    openCIP = open(pathToCIP,"r")

    global parentLines
    global CIPLines
    global flag

    parent_data = openParent.readline()
    CIP_data = openCIP.readline()
    

    while parent_data != '' or CIP_data != '':
        # Compare the lines and print the result
        if SequenceMatcher(None,parent_data,CIP_data).ratio() != 1.0:
            flag = 1
            print("NEW MATTER INSERTED: ",CIP_data)
            #break
        # Read the next line from each file
        else:  
            print("IDENTICAL:\n",'parent line: ', parent_data, "CIP line: ", CIP_data)
            flag = 0
        if flag != 1:
            parent_data = openParent.readline()
        CIP_data = openCIP.readline()
    else:
        print('Files are identical')


 
    # closing files
    openParent.close()                                      
    openCIP.close()           


parentLines=0
CIPLines=0
i=0
PatentComparison("test1.txt","test2.txt")