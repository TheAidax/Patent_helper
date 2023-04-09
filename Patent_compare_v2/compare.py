from pdfminer.high_level import extract_text, extract_pages
from difflib import SequenceMatcher # from difflib module for difflib plagarism check





#############################################################################################################
#                          Find differences in documents and display on front end                           #
#                                                                                                           #
#############################################################################################################




def compare():
    # Master prog: Run find changes and plagarism check functions
    resultChanges = findChanges()
    resultPlagarism = plagarismCheck()
    result = determine(resultPlagarism, resultChanges)
    display(result)





###################################################################################################################### END compare()






def findChanges():
    # find basic additions and removals from the text file using difflib
    x = 0




###################################################################################################################### END findchanges()



def plagarismCheck():
    # Check the text file for plagarism by vectorizing text and looking for sin-cos diffference?? 
    x = 0
 



 ###################################################################################################################### END plagarismCheck()
 
 
def importedCheck():
    #  Imported method for checking for plagarism using difflib
    x = 0



# Declaring string variables
string1 = 'I am geek' #Should be from parent
string2 = 'I am geeks' #Should be from CIP

# Using the SequenceMatcher()
match = SequenceMatcher(None,
					    string1, string2)

# convert above output into ratio
# and multiplying it with 100
result = match.ratio() * 100


#Display the final result
print(int(result), "%")


###################################################################################################################### END importedCheck()




def determine():
    # Determine the percent difference between docs                                  
    # Should return a percent based on all tests.      

    x = 0









###################################################################################################################### END determine()










#############################################################################################################
#                          Display the differences visually in the front end                                #
#                                                                                                           #
#############################################################################################################

def display(result):
    # Take the output of the plagarism checker and change finder and display 
    x = 0



###################################################################################################################### END display(result_doc, result)







#############################################################################################################
#                          Import files for comparison                                                      #
#                            (Imported code)                                                                #
#############################################################################################################




def pulling_Text(parentFilepath,CIPFilepath):
    getParentText = extract_text(parentFilepath)
    getCIPText = extract_text(CIPFilepath)

    parentText = open("parent.txt","w")
    CIPText = open("CIP.txt","w")

    parentText.write(getParentText)
    CIPText.write(getCIPText)

    parentText.close()
    CIPText.close()

pulling_Text("parentMadeSearchable.pdf","child.pdf")