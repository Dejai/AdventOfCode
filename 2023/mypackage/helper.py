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

# Print out the answer
def printAnswer(part=1, value=1):
    print("\n")
    print("Part %d" % part)
    print(sep2*25)
    print("Answer = %s" % str(value))
    print(sep2*25)
    print("\n")

# Print out a given grid
def printGrid(grid, toFile=None):
    gridPrint = ""
    for row in grid:
        gridPrint += "".join(row) + "\n"
    if toFile is not None:
        file = open(toFile, "w+")
        file.write(gridPrint)
        file.close()
        print("Saved grid to file: {0}".format(toFile))
    else:
        print(gridPrint)

# Valdate a set of results
def compareLists(expectedList, resulstList):
    
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
