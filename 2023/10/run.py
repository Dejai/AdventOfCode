
from mypackage import helper
from collections import deque

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions & Classes
***************************************************************
'''
class Pipe:
    def __init__(self, name, pos):
        self.Name = name
        self.Position = pos
        self.Neighbors = []
        self.Ends = {}
        self.Dist = 0 if name == "S" else None # distance from starting node
        self.Visited = 0
        self.Arrow = name
        self.setEnds()
    def __repr__(self):
        return "{} {}".format(self.Name, self.Position)
    def setEnds(self):
        if self.Name in list("|JLS"):
            self.Ends["North"] = None  
        if self.Name in list("|F7S"):
            self.Ends["South"] = None        
        if self.Name in list("-FLS"):
            self.Ends["East"] = None 
        if self.Name in list("-J7S"):
            self.Ends["West"] = None
    def addNeighbor(self, neighbor):
        if type(neighbor) is Pipe:
            pair1 = "North" in self.Ends and "South" in neighbor.Ends and (neighbor.Position[0] < self.Position[0])
            pair2 = "South" in self.Ends and "North" in neighbor.Ends and (neighbor.Position[0] > self.Position[0])
            pair3 = "East" in self.Ends and "West" in neighbor.Ends and (neighbor.Position[1] > self.Position[1])
            pair4 = "West" in self.Ends and "East" in neighbor.Ends and (neighbor.Position[1] < self.Position[1])
            if pair1 or pair2 or pair3 or pair4:
                self.Neighbors.append(neighbor)
                neighbor.Neighbors.append(self)
    def addArrow(self, parent):
        if parent.Position[0] < self.Position[0]:
            self.Arrow = "V"
        elif parent.Position[0] > self.Position[0]:
            self.Arrow = "^"
        elif parent.Position[1] < self.Position[1]:
            self.Arrow = ">"
        elif parent.Position[1] > self.Position[1]:
            self.Arrow = "<"

class GraphBuilder:
    def __init__(self, inputList):
        self.Nodes = {}
        self.Start = None
        self.Input = inputList
        self.buildGraph()
    def buildGraph(self):
        for rowIdx,row in enumerate(self.Input):
            for colIdx,value in enumerate(row):
                node = self.getNode(rowIdx, colIdx)
                if type(node) is Pipe:
                    if node.Name == "S":
                        self.Start = node
                    else:
                        above = self.getNode(rowIdx-1, colIdx)
                        node.addNeighbor(above)
                        left = self.getNode(rowIdx, colIdx-1)
                        node.addNeighbor(left)
    def getNode(self, rowIdx, colIdx):
        if rowIdx < 0 or colIdx < 0:
            return None
        position = (rowIdx, colIdx)
        name = self.Input[rowIdx][colIdx]
        if position not in self.Nodes:
            self.Nodes[position] = Pipe(name, position) if name != "." else None
        return self.Nodes[position]


# Search through graph using BFS
def bfs(graph):
    startingNode = graph.Start
    queue = deque([startingNode])
    visited = [startingNode]
    highest = 0
    while queue:
        node = queue.popleft()
        highest = node.Dist
        newDist = node.Dist + 1
        for neigh in node.Neighbors:
            neigh.Visited += 1
            # if neigh.Position == (0, 50):
            #     print("\tVisiting Neighbor:{0} --> from {1}".format(str(neigh), str(node)))
            #     print("\tNeigh Dist: {0} // Parent Dist:{1}".format(str(neigh.Dist), str(node.Dist)))
            if neigh.Dist is None:
                neigh.Dist = newDist
                neigh.addArrow(node)
                # print("\t\tAdding Neighbor for next check: " + str(neigh))
                queue.append(neigh)
    return highest
'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
graph = GraphBuilder(inputList)
ans1 = bfs(graph)
helper.printAnswer(1,ans1)

outputList = []
for rowIdx,row in enumerate(inputList):
    outRow = []
    for colIdx, value in enumerate(row):
        node = graph.Nodes[(rowIdx,colIdx)]
        if node is None:
            outRow.append(".")
        elif type(node) is Pipe:
            if node.Name == "S":
                outRow.append("S")
            elif node.Visited > 0:
                outRow.append(node.Arrow)
            else:
                outRow.append(value)
        else:
            outRow.append(value)
    outputList.append("\t\t".join(outRow))
helper.printToFile(outputList)

# 13449 -- Too high

# Print answer for Part 2
helper.printAnswer(2, "Part 2 Default")