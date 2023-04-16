def compare():
    # Run find changes and plagarism check 
    x = 0


def findChanges():
    # find basic additions and removals from the text file
    x = 0



def plagarismCheck():
    # Check the text file for plagarism
    x = 0

    # Importing SequenceMatcher
# from difflib module
from difflib import SequenceMatcher

# Declaring string variables
string1 = 'I am geek' #Should be from parent
string2 = 'I am geeks' #Should be from CIP

# Using the SequenceMatcher()
match = SequenceMatcher(None,
					    string1, string2)

# convert above output into ratio
# and multiplying it with 100
result = match.ratio() * 100

# Display the final result
print(int(result), "%")



def display(result_doc, result):
    # Take the output of the plagarism checker and change finder and display 
    x = 0