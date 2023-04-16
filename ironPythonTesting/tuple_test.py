
def testTuples(): #Just testing some tuples....

    tupleNumber = (1, 2, 3)
    tupleString = ("this", "is", "a", "tuple")
    tupleFloat = (1.22, 3.3333, 77.2937129)
    tupleMixed = (0.333333, "twenty five", 3)

    tupleList = [("item1", 0.24, 4), ("item2", 0.777, 7), ("item3", 0.11, 11)]

    print("A tuple of numbers: ", tupleNumber)
    print("A tuple of strings: ",tupleString)
    print("A tuple of floats: ",tupleFloat)
    print("A tuple of mixed data: ",tupleMixed)
    print("A list of tuples: ",tupleList)
    print("Item 1 in the list of tuples: ", tupleList[0])


def generateThenTest():

    aNum = 2
    aWord = "string"
    aFloat = 33.33333 #float used in the generation
    generateList = []
    
    #Proof that making a mixed list of tuples is possible and easy
    for x in range(10):
        generateList.append((f'string{x}', x, aFloat)) 
        # F string is a literal string whose value is determined at RUNTIME not COMPILE TIME. They are useful for appending integers to strings
        aFloat*2

    


        #innerlist = []
        #for y in range(10):
            #aFloat * 2
            #nnerlist.append((f'string{y}', y, aFloat))
        #generateList.append(innerlist)

        #Someone on stack overflow recommended an inner list inside a nested for loop to generate a list of tuples
        #But that literally just made double the items in the list of tuples, so wtf? For what purpose?

    print("A 10 item list of tuples: \n")
    for item in generateList: #just print the generated list of tuples for viewing
        print(item)



def master(): #Add stuff to run here
    testTuples()
    generateThenTest()

master()