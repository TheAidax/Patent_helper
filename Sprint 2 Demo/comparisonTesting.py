from difflib import *


def PatentComparison(pathToParent,pathToCIP):
    
    openParent = open(pathToParent,"r")
    openCIP = open(pathToCIP,"r")

    newFile = open("finalOuput2.txt","w")

    global parentLines
    global CIPLines
    global flag



    parent_data = openParent.readline()
    CIP_data = openCIP.readline()
    
    while parent_data != '' or CIP_data != '':
        # Compare the lines and print the result
        #if parent_data == CIP_data:
        if SequenceMatcher(None,parent_data,CIP_data).quick_ratio() < 0.6 and SequenceMatcher(None,parent_data,CIP_data).quick_ratio() > 0.2:
            flag = 1
            #print("NEW MATTER INSERTED: ",CIP_data)
            newFile.write("NEW MATTER INSERTED:")
            newFile.write(CIP_data)
            #print(SequenceMatcher(None,parent_data,CIP_data).quick_ratio())
            
            #break
        # Read the next line from each file
        
        elif SequenceMatcher(None,parent_data,CIP_data).quick_ratio() < 0.2:
            flag = 1
            newFile.write("DELETED MATTER:")
            newFile.write(parent_data)
            parent_data = openParent.readline()
            CIP_data = openCIP.readline()

        else:  
            newFile.write(parent_data)
            flag = 0
        if flag != 1:
            parent_data = openParent.readline()
            
        CIP_data = openCIP.readline()
    
    
    print('Process Completed')


 
    # closing files
    openParent.close()                                      
    openCIP.close()
    newFile.close()


parentLines=0
CIPLines=0
i=0
PatentComparison("test1.txt","test2.txt")