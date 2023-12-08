
from mypackage import helper
from collections import deque
import math
'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt", "\n\n")

'''
***************************************************************
    Functions * Class
***************************************************************
'''
def getNodesMap(nodesList):
    nodeMap = {}
    for nodeInput in nodesList:
        node,pairs = nodeInput.split(" = ")
        left,right = pairs.replace("(", "").replace(")","").split(", ")
        nodeMap[node] = (left, right, 1)
    return nodeMap

def getStepsToGoal(nodeMap, start, goal, endsWith=False):
    directions = deque( list(inputList[0]))
    isGoal = False 
    steps = 0
    currNode = start
    if start in nodeMap:
        while not isGoal:
            dir = directions.popleft()
            directions.append(dir) # add the direction back, as we gotta keep going until we get to the end
            dirIdx = 0 if dir == "L" else 1
            steps += 1
            currNode = nodeMap[currNode][dirIdx]
            isGoal = (currNode[-1] == goal) if endsWith else (currNode == goal)
    return steps

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
nodesList = [ line for line in inputList[1].split("\n") if line != ""]
nodeMap = getNodesMap(nodesList)
ans1 = getStepsToGoal(nodeMap, "AAA", "ZZZ", )
helper.printAnswer(1,ans1)

# Print answer for Part 2
nodes = [ x for x in list(nodeMap.keys()) if x[-1] == "A" ]
steps = [ getStepsToGoal(nodeMap, start, "Z", endsWith=True) for start in nodes ]
ans2 = math.lcm(*steps)
helper.printAnswer(2, ans2)