

# Get the file input as a list
def getInputList(input):
    inputList = []
    for line in input:
        inputList.append(int(line))
    return inputList


inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()

# Get list of content
inputList = [int(x) for x in content.split("\n") if x != '']


''''
    Get details for Part 1
'''
increases = [ inputList[i] > inputList[i-1] for i in range(1,len(inputList))]
increasesOnly = [ x for x in increases if x == True ]
print("Increases == %d" %(len(increasesOnly)))

decreases = [ inputList[i] < inputList[i-1] for i in range(1,len(inputList))]
decreasesOnly = [ x for x in decreases if x == True ]
print("Decreases == %d" %(len(decreasesOnly)))

nochange = [ inputList[i] == inputList[i-1] for i in range(1,len(inputList))]
noChangeOnly = [ x for x in nochange if x == True]
print("No Change == %d" %(len(noChangeOnly)))



print('\n')

''''
    Get details for Part 1
'''

groupedInputList = [ sum(inputList[i-2:i+1]) for i in range(2,len(inputList)) ]

increases = [ groupedInputList[i] > groupedInputList[i-1] for i in range(1,len(groupedInputList))]
increasesOnly = [ x for x in increases if x == True ]
print("Increases == %d" %(len(increasesOnly)))

decreases = [ groupedInputList[i] < groupedInputList[i-1] for i in range(1,len(groupedInputList))]
decreasesOnly = [ x for x in decreases if x == True ]
print("Decreases == %d" %(len(decreasesOnly)))

nochange = [ groupedInputList[i] == groupedInputList[i-1] for i in range(1,len(groupedInputList))]
noChangeOnly = [ x for x in nochange if x == True]
print("No Change == %d" %(len(noChangeOnly)))




# # Get details for original input
# input = open("input.txt", "r+")
# getDetails(input)
# input.close()

# print("\n")
# input = open("./input.txt", "r+")
# inputList = getInputList(input)

# input.close()


# print("\n\n")
# input2 = open("input2.txt", "r+")
# getDetails(input2)
# input2.close()

# print("\n")
# input = open("./input.txt", "r+")
# inputList = getInputList(input)
# grouped = [ sum(inputList[i-2:i+1]) for i in range(2,len(inputList)) ]
# changes = [ grouped[i] > grouped[i-1] for i in range(1,len(grouped))]
# increases = [ x for x in changes if x == True ]
# print(len(increases))
# input.close()



