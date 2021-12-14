

# Separators I use often
sep1 = "*"
sep2 = "-"


# Get the file input as a list of rows
def getFileContentAsList(filePath):
    inputFile = open(filePath, "r+") # open file
    content = inputFile.read() # read full content
    inputFile.close()
    # Split on new line and insert each frow in list
    inputList = [ x for x in content.split("\n") if x != '' ]

    return inputList



def printAnswer(value):
    print("\n")
    print(sep2*25)
    print("Answer = %s" % str(value))
    print(sep2*25)


# Valdate a set of results
def validateResults(expectedList, resulstList):
    
    matches = [ format("%s: %s" % ((x in resulstList), str(x)) )  for x in expectedList ]

    good = [ x for x in matches if "True" in x]
    bad = [ x for x in matches if "False" in x]
    
    print(sep1*50)

    print("\nVALIDATING RESULTS")
    print("Good = %d" % len(good))
    print("Bad = %d" % len(bad))
    print(sep2*50)
    

    for line in matches:
        print(line)


    if(len(resulstList) > len(expectedList)):
        print(sep2*25)
        print("EXTRAS")
        extras = [ x for x in resulstList if x not in expectedList]
        for line in extras:
            print(line)

    print(sep1*50)



# Validate if the count is as expected
def validateCount(expectedCount, resultsCount):

    print(sep1*50)
    mathingCount = expectedCount == resultsCount
    print("\nVALIDATING RESULTS")
    print("Results / Expected == %d/%d" % (resultsCount, expectedCount ))

    print(sep1*50)