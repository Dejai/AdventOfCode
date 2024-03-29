# Separators I use often
sep1 = "*"
sep2 = "-"

# Get the file input as a list of rows
def getFileContentAsList(filePath, splitChar="\n"):
    inputList = []
    with open(filePath, "r+") as inputFile:
        content = inputFile.read().split(splitChar) # read full content
        inputList = [ x for x in content if x != "" ]
    return inputList

# Convert a string to a list, based on split char
def toList(value, splitChar=" ",type="str"):
    newList = list( filter(lambda x: x != "", value.split(splitChar)) )
    if type == "int":
        intList = [ int(x) for x in newList if x != ""]
        return intList
    return newList

# Print out the answer
def printAnswer(part=1, value=1):
    print("\n")
    print("Part %d" % part)
    print(sep2*25)
    print("Answer = %s" % str(value))
    print(sep2*25)
    print("\n")

# Print a list to a file
def printToFile(inputList, fileName="output.txt"):
    with open(fileName, "w+") as outputFile:
        for line in inputList:
            outputFile.write(str(line)+"\n")

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


# Map input list to output list
def mapInputToOutput(inputList, outputList):
    idx = 0
    mapList = []
    fileName = "./compare.txt"
    for idx in range(0, len(inputList)):
        inputVal = inputList[idx]
        outputVal = outputList[idx] if idx < len(outputList) else None
        results = "{0} - {1}".format(inputVal, outputVal)
        mapList.append(results)
    with( open(fileName, "w+") as output):
        for line in mapList:
            output.write(line + '\n')
    print("Comparison results at: " + fileName)
    