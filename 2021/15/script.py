from typing import Collection, Dict
import shared

'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./example.txt")


'''
***************************************************************
    Class and Functions
***************************************************************
'''

# A class for the Nodes in the graph
class Node:

    def __init__(self, name, cost, rowIdx):
        self.name = name
        self.neighbors = []

        self.cost = int(cost)

        # For the path
        self.distance = float("inf")
        self.prev = None

        self.row = rowIdx

    def __repr__(self):
        return repr((self.name, self.distance))
    
    def addNeighbor(self, nodeName):
        if nodeName not in self.neighbors:
            self.neighbors.append(nodeName)

    # Get unvisited neighbor of node
    def getNeighbors(self):

        neighbors = []
        for n in self.neighbors:
            neighbors.append(n.name)
        
        return neighbors


# A helper to make the node name consistent
def getNodeName(row, col):
    return str(row) + "-" + str(col)


# Get the graph of the nodes
def createGraph(inputList):

    nodes = {}

    totalRows = len(inputList)

    for rowIdx in range(0, totalRows):

        row = inputList[rowIdx]
        rowLength = len(row)

        for colIdx in range(0, rowLength):

            cost = inputList[rowIdx][colIdx]

            name = getNodeName(rowIdx, colIdx)

            # Create the main node for this coordinate
            node = Node(name, cost, rowIdx)
            nodes[name] = node

            # Add the neighbors
            neighborRight = (rowIdx, colIdx+1) if colIdx < rowLength-1 else None
            neightborBelow = (rowIdx+1, colIdx) if rowIdx < totalRows-1 else None
            possibleNeighbors = [neighborRight, neightborBelow]
            # The list of neighbors
            neighbors = [ x for x in possibleNeighbors if x is not None]
            
            # Loop through any neighbors
            for n in neighbors:
                neighborName = getNodeName(n[0], n[1])

                # Get the cost for the node
                r = n[0]
                c = n[1]
                cost = inputList[r][c]
                
                if neighborName in nodes:
                    neighborNode = nodes[neighborName]
                    node.addNeighbor(neighborNode)
                elif neighborName not in nodes:
                    neighborNode = Node(neighborName,cost, rowIdx)
                    node.addNeighbor(neighborNode)

            
    
    return nodes


# Create the extended graph
def createExtendedGraph(inputList, rowLength, colLength):

    print("Extending the graph")

    newRowLength = rowLength * 5
    newColLength = colLength * 5

    newMap = []

    for rowIdx in range(0, newRowLength):
        isNewRow = rowIdx >= rowLength
        newRow = []

        for colIdx in range(0, newColLength):

            isNewCol = colIdx >= colLength


            newVal = -1
            oldVal = -1

            if isNewRow:
                oldVal = newMap[rowIdx-rowLength][colIdx]
            elif isNewCol:
                oldVal = newRow[colIdx-colLength]
            else:
                newVal = int(inputList[rowIdx][colIdx])

            if(isNewRow or isNewCol):
                newVal = oldVal+1 if oldVal < 9 else 1


            newRow.append(newVal)


        newMap.append(newRow)

    return newMap


# Run dijkstra to determine shortest path
def dijkstra(nodes, source, target):

    #theNodes = list(nodes.values())
    print("Running Dijkstra")

    # Set the source node to zero
    nodes[source].distance = 0

    theQueue = list(nodes.values())
    totalNodes = len(theQueue)
    print("Checking total nodes = " + str(totalNodes))

    visited = []

    count = 0

    smallest = nodes[source]

    while True:


        theQueue.sort(key=lambda node: node.distance)

        if ( len(theQueue) == 0):
            break

        node = theQueue.pop(0)

        #node = smallest

        # count += 1

        # if( ((totalNodes / count) * 100) % 10 == 0):
        #     print("Still chugging ... " + str(count))

        if node.name == target:
            print("\nTARGET FOUND!: ")
            print(node)
            break

        if node.name in visited:
            continue

        visited.append(node.name)
        
        for neighbor in node.getNeighbors():

            neighborNode = nodes[neighbor]
            if neighborNode.name in visited:
                continue
            tempDist = node.distance + neighborNode.cost
            if tempDist < neighborNode.distance:
                neighborNode.distance = tempDist
                neighborNode.prev = node


'''
***************************************************************
    Run
***************************************************************
'''

rows = len(inputList)
cols = len(inputList[0])
start = getNodeName(0, 0)
target = getNodeName(rows-1, cols-1)

# Part 1
graph = createGraph(inputList)
dijkstra(graph, start, target)

print("\n")

# Part 2
newMap = createExtendedGraph(inputList, rows, cols)
newGraph = createGraph(newMap)
newTarget = getNodeName( (rows*5)-1, (cols*5)-1 )
# NOT VERY EFFICIENT! TAKES VERY LONG TO RUN
dijkstra(newGraph, start, newTarget)