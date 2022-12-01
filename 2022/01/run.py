
import helper

'''
***************************************************************
    Input
***************************************************************
'''
exampleInput = helper.getFileContentAsList("./example.txt")
realInput = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with
inputList = realInput
# print(inputList)

# Print answer for Part 1
elfVal = 0
elfVals = []
for x in inputList:
    if x == "":
        # max = elfVal if elfVal > max else max
        elfVals.append(elfVal)
        elfVal = 0
    else:
        elfVal += int(x)

maxNum = max(elfVals)    
helper.printAnswer(1, maxNum)


# Print answer for Part 2
elfVals.sort(reverse=True)
maxNum = sum(elfVals[0:3])
helper.printAnswer(2, maxNum)