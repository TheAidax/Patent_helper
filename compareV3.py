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
        flag = 0
        
        if SequenceMatcher(None,parent_data,CIP_data).quick_ratio() < 0.5:
            flag = 1
            #print("NEW MATTER INSERTED: ",CIP_data)
            newFile.write("NEW MATTER INSERTED:")
            newFile.write(CIP_data)
            print("1st if")
            #similarityRatio = SequenceMatcher(None,parent_data,CIP_data).quick_ratio()
            print(SequenceMatcher(None,parent_data,CIP_data).quick_ratio())
            
        # Read the next line from each file
        
        elif SequenceMatcher(None,parent_data,CIP_data).quick_ratio() <= 0.8 and SequenceMatcher(None,parent_data,CIP_data).quick_ratio() >= 0.5:
            print("2nd if")
            flag = 2
            newFile.write("DELETED MATTER:")
            newFile.write(parent_data)
            #similarityRatio = SequenceMatcher(None,parent_data,CIP_data).quick_ratio()
            print(SequenceMatcher(None,parent_data,CIP_data).quick_ratio())
                   
        else:  
            #print("IDENTICAL:\n",'parent line: ', parent_data, "CIP line: ", CIP_data)
            newFile.write(parent_data)
            flag = 0
            #similarityRatio = SequenceMatcher(None,parent_data,CIP_data).quick_ratio()


        if flag != 1 :
            parent_data = openParent.readline()

        if flag !=2 :
            CIP_data = openCIP.readline()
    

    print('Files are identical')


 
    # closing files
    openParent.close()                                      
    openCIP.close()
    newFile.close()


parentLines=0
CIPLines=0
i=0
PatentComparison("6charsParent.txt","6charsCIP.txt")
