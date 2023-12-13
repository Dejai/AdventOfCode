
from mypackage import helper
from mypackage.timer import MyTimer
from collections import deque
import itertools

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Classes & Functions
***************************************************************
'''
class Node:
    def __init__(self, name, pos):
        self.Name = name
        self.Position = pos
        self.Neighbors = set()
        self.Type = "Galaxy" if self.Name == "#" else "Space"

    def __repr__(self):
        return "{} {} -> {}".format(self.Type, str(self.Position))
    
    def addNeighbor(self, otherNode):
        if otherNode != self:
            self.Neighbors.add(otherNode)
            otherNode.Neighbors.add(self)

    # Get neighbors ordered by ones closest to goal
    def getNeighbors(self, goal):
        sourceRow,sourceCol = self.Position
        destRow,destCol = goal.Position
        minRow = min(sourceRow, destRow)
        maxRow = max(sourceRow, destRow)
        minCol = min(sourceCol, destCol)
        maxCol = max(sourceCol, destCol)
        rowRange = range(minRow, maxRow+1) 
        colRange = range(minCol, maxCol+1)
        neighbors = [ n for n in self.Neighbors if n.Position[0] in rowRange and n.Position[1] in colRange]
        return neighbors

class GraphBuilder:
    def __init__(self, inputList):
        self.Nodes = {}
        self.Input = inputList
        self.Rows = set(range(0,len(inputList)))
        self.Cols = set(range(0, len(inputList[0])))
        self.buildGraph()

    def buildGraph(self):
        for rowIdx,row in enumerate(self.Input):
            for colIdx,value in enumerate(row):
                node = self.getNode(rowIdx, colIdx)
                if rowIdx > 0:
                    node.addNeighbor(self.Nodes[(rowIdx-1, colIdx)])
                if colIdx > 0:
                    node.addNeighbor(self.Nodes[(rowIdx,colIdx-1)])

    def getNode(self, rowIdx, colIdx):
        if rowIdx < 0 or colIdx < 0:
            return None
        position = (rowIdx, colIdx)
        name = self.Input[rowIdx][colIdx]
        if position not in self.Nodes:
            node = Node(name, position)
            self.Nodes[position] = node
            # If a galaxy is found, remove that row/col from the set of all rows/cols
            if node.Type == "Galaxy":
                row,col = node.Position
                if row in self.Rows:
                    self.Rows.remove(row)
                if col in self.Cols:
                    self.Cols.remove(col)
        return self.Nodes[position]
    
    # Get the shortest path to the goal (using neighbors that are in the direction)
    def shortestPath(self, start, end):
        queue = deque([start])
        visited = set()
        expandedRows = set()
        expandedCols = set()
        dist1 = 0
        dist2 = 0
        exp1 = 2
        exp2 = 1000000
        while queue:
            node = queue.pop()
            visited.add(node)
            row,col = node.Position
            expanded = False
            if node != start:
                # Expanding rows
                if row in self.Rows and row not in expandedRows:
                    dist1 += exp1
                    dist2 += exp2
                    expandedRows.add(row)
                    expanded=True
                if col in self.Cols and col not in expandedCols:
                    dist1 += exp1
                    dist2 += exp2
                    expandedCols.add(col)
                    expanded=True
                # If not expanded, then just add 1
                if not expanded:
                    dist1 += 1
                    dist2 += 1
            if node == end:
                break                    
            for neigh in node.getNeighbors(goal=end):
                if neigh not in visited:
                    queue.append(neigh)
        return (dist1, dist2)
'''
***************************************************************
    Run
***************************************************************
'''
timer = MyTimer(save=True)
timer.start()

# Print answer for Part 1
graph = GraphBuilder(inputList)
galaxies = [x for x in graph.Nodes.values() if x.Name == "Galaxy" ]
galaxyPairs = itertools.combinations(galaxies,2)
distances = [ graph.shortestPath(source,dest) for source,dest in [pair for pair in galaxyPairs] ]
ans1 = sum( [ pair[0] for pair in  distances ] )
helper.printAnswer(1,ans1)

# Print answer for Part 2
ans2 = sum( [ pair[1] for pair in  distances ] )
helper.printAnswer(2, ans2)

timer.stop()