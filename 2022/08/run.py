
import helper
from classes import Tree

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
# Get the key based on indexes
def getKey(row,col):
    return "{0}-{1}".format(row,col)

# Get the trees
def getTreeMap(inputList):

    rows = len(inputList)
    cols = len(inputList[0])

    treeMap = {}

    for rowIdx in range(0,rows):
        for colIdx in range(0,cols):
            key = getKey(rowIdx,colIdx)

            if key not in treeMap:
                height = inputList[rowIdx][colIdx]
                treeMap[key] = Tree(height, key)
            
            # Current tree
            currTree = treeMap[key]

            # Surrounding trees
            if colIdx > 0:
                leftTree = treeMap[ getKey(rowIdx, colIdx-1) ]
                # Set left/right    
                currTree.setNeighbor("left",leftTree)
                leftTree.setNeighbor("right",currTree)
            if rowIdx > 0:
                aboveTree = treeMap[ getKey(rowIdx-1, colIdx) ]
                # Set above/below
                currTree.setNeighbor("above",aboveTree)
                aboveTree.setNeighbor("below",currTree)

    return treeMap


'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
tMap = getTreeMap(inputList)
# print(inputList)

# Print answer for Part 1
visibleTrees = [ tree for tree in tMap.values() if tree.visible() ]
a1 = len(visibleTrees)
helper.printAnswer(1,a1)

# Print answer for Part 2
scenic = [ tree.getScenicScore() for tree in tMap.values() ]
a2 = max(scenic)
helper.printAnswer(2, a2)