
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
    Functions
***************************************************************
'''
# Get list from range
def getLists(rangePair):
    ranges = rangePair.split(",")
    return (getListFromRange(ranges[0]), getListFromRange(ranges[1]))

# Get list from a range    
def getListFromRange(rangeVal):
    digits = rangeVal.split("-")
    listVals = range(int(digits[0]), int(digits[1])+1)
    return listVals

# Determine if overlap
def getOverlap(rangePair,isFullSubset=True):
    l1,l2 = getLists(rangePair)
    set1 = set(l1)
    set2 = set(l2)
    isSubset = (set1.issubset(set2) or set2.issubset(set1))
    isIntersect = len(list(set1.intersection(set2))) > 0
    overlap = isSubset if isFullSubset else isIntersect
    return overlap

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
overlaps = [ getOverlap(x) for x in inputList if getOverlap(x) ]
helper.printAnswer(1,len(overlaps))

# Print answer for Part 2
overlaps = [ getOverlap(x, False) for x in inputList if getOverlap(x, False) ]
helper.printAnswer(2, len(overlaps))