from collections import deque


# A class for the Nodes in a graph
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


# Get a simple name for a given row/col pair
def getNodeName(row, col):
    return str(row) + "-" + str(col)

# Create a graph, given a set of inputs & parameters
def createGraph(inputList):

    graph = {}

    totalRows = len(inputList)

    for rowIdx in range(0, totalRows):

        row = inputList[rowIdx]
        rowLength = len(row)

        for colIdx in range(0, rowLength):

            cost = inputList[rowIdx][colIdx]

            name = getNodeName(rowIdx, colIdx)

            # Create the main node for this coordinate
            node = Node(name, cost, rowIdx)
            graph[name] = node

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
                
                if neighborName in graph:
                    neighborNode = graph[neighborName]
                    node.addNeighbor(neighborNode)
                elif neighborName not in graph:
                    neighborNode = Node(neighborName,cost, rowIdx)
                    node.addNeighbor(neighborNode)

    return graph



# Dijkstra: Determine shortest path
def dijkstra(nodes, source, target):

    print("Running Dijkstra")

    # Set the source node to zero
    nodes[source].distance = 0

    # Setup the initial queue
    theQueue = list(nodes.values())
    totalNodes = len(theQueue)
    print("Checking total nodes = " + str(totalNodes))

    # Keep track of visited
    visited = []
    count = 0
    smallest = nodes[source]

    #  Keep going until loop is broken
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


# Run BFS
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