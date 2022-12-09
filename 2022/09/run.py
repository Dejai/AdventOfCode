
import helper
from classes import Knot

'''
***************************************************************
    Input
***************************************************************
'''

exampleInput = helper.getFileContentAsList("./example2.txt")
realInput = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions
***************************************************************
'''

# Get a list of knots
def getKnots(count=2):

    knots = []
    for idx in range(0,count):
        if idx == 0:
            knots.append(Knot("head"))
        else:
            knots.append(Knot(idx,knots[-1]))
    return knots


# Move the head & tail along a grid
def moveAlongGrid(knots, inputMoves):
        
    headKnot = knots[0]

    for move in inputMoves:
        splits = move.split(" ")
        direction = splits[0]
        count = int(splits[1])

        # print("Move: " + move)
        for idx in range(0, count):
            # print("  move #" + str(idx))
            rowMove = 1 if direction == "U" else (-1 if direction == "D" else 0)
            colMove = 1 if direction == "R" else (-1 if direction == "L" else 0)
            headKnot.moveKnot(rowMove, colMove)

            # For any subsequent knot, follow the leader
            for knot in knots:
                knot.followLeader()
            
    headKnot = knots[0]
    tailKnot = knots[-1]
    print("Head: " + str(headKnot))
    print("Tail: " + str(tailKnot))
    uniqueTailLocations = len(tailKnot.unique)
    return uniqueTailLocations


'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
knots = getKnots()
a1 = moveAlongGrid(knots, inputList)
helper.printAnswer(1,a1)

# Print answer for Part 2
knots = getKnots(10)
a2 = moveAlongGrid(knots, inputList)
helper.printAnswer(2,a2)