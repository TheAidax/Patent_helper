from difflib import *

def PatentComparison(pathToParent,pathToCIP):
    
    openParent = open(pathToParent,"r")
    openCIP = open(pathToCIP,"r")

    newFile = open("finalOuput.txt","w")

    global parentLines
    global CIPLines
    global flag

    parent_data = openParent.readline()
    CIP_data = openCIP.readline()
    

    while parent_data != '' or CIP_data != '':
        # Compare the lines and print the result
        #if parent_data == CIP_data:
        if SequenceMatcher(None,parent_data,CIP_data).quick_ratio() > 0.7:
            flag = 1
            #print("NEW MATTER INSERTED: ",CIP_data)
            newFile.write("NEW MATTER INSERTED:")
            newFile.write(CIP_data)
            #break
        # Read the next line from each file
        else:  
            #print("IDENTICAL:\n",'parent line: ', parent_data, "CIP line: ", CIP_data)
            newFile.write(parent_data)
            flag = 0
        if flag != 1:
            parent_data = openParent.readline()
        CIP_data = openCIP.readline()
    else:
        print('Files are identical')


 
    # closing files
    openParent.close()                                      
    openCIP.close()
    newFile.close()


parentLines=0
CIPLines=0
i=0
PatentComparison("parentOutput.txt","2chars.txt")
