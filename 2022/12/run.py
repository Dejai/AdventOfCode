
import helper
from classes import LocationNodes, Grid
from collections import deque

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

# Get set of nodes in a graph
def getNodes(inputList):

    nodes = {}
    start = None
    target = None

    for i in range(0, len(inputList)):
        row = inputList[i]
        for j in range(0, len(row)):
            # Get a key for name
            nodeKey = "{0}-{1}".format(i,j)
            leftNodeKey = "{0}-{1}".format(i,j-1)
            aboveNodeKey = "{0}-{1}".format(i-1,j)

            # Get the node for this item
            item = row[j]
            node = LocationNodes(item, (i,j))

            # Set node in map of nodes
            nodes[nodeKey] = node

            # Set neighbors
            if leftNodeKey in nodes:
                leftNode = nodes[leftNodeKey]
                leftNode.addNeighbor(node)
                node.addNeighbor(leftNode)
                
            if aboveNodeKey in nodes:
                aboveNode = nodes[aboveNodeKey]
                aboveNode.addNeighbor(node)
                node.addNeighbor(aboveNode)

            # Set start & target nodes
            if item.isupper():
                if item == "S":
                    start = node
                elif item == "E":
                    target = node
        
    return nodes,start,target

# # Run BFS
def bfs(nodes, source, target, grid=None):

    nodeQueue = deque()
    source.Distance = 0
    nodeQueue.append(source)
    for n in nodes.values():
        nodeQueue.append(n)

    # Set the Start and End nodes as their capital names
    if grid is not None:
        grid.setKeyNode(source.Name, source.Row, source.Col)
        grid.setKeyNode(target.Name, target.Row, target.Col)

    while len(nodeQueue) > 0:

        # Get current node
        node = nodeQueue.popleft()

        neighbors = node.getNeighbors()
        # print("Checking {0} neighbors for {1} : ".format( len(neighbors), node))

        for neighbor in neighbors:
            # print("\tChecking neighbor: " + str(neighbor))
            dist = node.Distance + neighbor.Cost
            if dist < neighbor.Distance:
                neighbor.Distance = dist
                neighbor.Prev = node
                nodeQueue.append(neighbor)

    if grid is not None:
        grid.setPath(target)
        grid.printGrid()

    print(target)
    return target


'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
nodes,start,target = getNodes(inputList)
grid = Grid(len(inputList), len(inputList[0]))
result = bfs(nodes, start, target, grid)
helper.printAnswer(1,result.Distance)

# Print answer for Part 2
nodes,start,target = getNodes(inputList)
grid = Grid(len(inputList), len(inputList[0]))
aNodes = [ node for node in nodes.values() if node.Name in ["a", "S"] ]
distances = []
for node in aNodes:
    result = bfs(nodes, node, target)
    distances.append(result.Distance)
a2 = min(distances)
helper.printAnswer(2, a2)