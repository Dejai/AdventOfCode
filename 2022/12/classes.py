import math

# A class for each location node in the "graph"
class LocationNodes:

    def __init__(self, name, index):
        self.Name = name
        self.Row = int(index[0])
        self.Col = int(index[1])
        self.Index = "{0}-{1}".format(self.Row, self.Col)
        self.Neighbors = []
        self.Distance = float('inf')
        self.Cost = 1
        self.Prev = None

        # Value/weight of node
        self.Ord = ord(self.Name)
        if self.Name == "S":
            self.Ord = 97
        elif self.Name == "E":
            self.Ord = 122
        

    def __repr__(self):
        return "Node: {0} ({1}) -> {2}".format(self.Name, self.Index, self.Distance)

    def addNeighbor(self, neighbor):
        diff = neighbor.Ord - self.Ord
        if (diff <= 1):
            self.Neighbors.append(neighbor)

    def getNeighbors(self):
        self.Neighbors.sort(key=lambda node: node.Ord)
        # print(self.Neighbors)
        return self.Neighbors

    
class Grid:

    def __init__(self, rows, cols):
        self.grid = [ ["." for i in range(0,cols)] for j in range(0,rows) ]

    # Set a specific coordinate with a specific value
    def setKeyNode(self,value,row,col):
        self.grid[row][col] = "{0}".format(value)

    def addNode(self, fromNode, toNode=None):
        if fromNode.Name != "S":
            self.grid[fromNode.Row][fromNode.Col] = "{0}".format(fromNode.Name)

    # Set the full path of the grid
    def setPath(self, node):

        currNode = node
        prevNode = node.Prev

        self.addNode(currNode,currNode)

        while prevNode is not None:
            self.addNode(prevNode, currNode)
            # Jump back one
            currNode = prevNode
            prevNode = currNode.Prev


    def printGrid(self):
        gridPrint = ""
        for row in self.grid:
            gridPrint += "".join(row) + "\n"
        print(gridPrint)