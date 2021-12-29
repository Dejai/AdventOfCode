import math
from math import floor,ceil
from collections import deque


DEBUG = False

class Pair:

    def __init__(self, array=None, parent=None):

        self.parent = parent
        self.left = None
        self.right = None

        if array is not None:
            self.createPair(array)

    def __repr__(self):
        return repr([self.left,self.right]).replace(" ", "")
    

    # Create a pair from "scratch" (i.e. with provided array values)
    def createPair(self, array):
        left = array[0]
        right = array[1]

        self.left = Pair(left, self) if type(left) != int else left
        self.right = Pair(right, self) if type(right) != int else right

    # Reduce a number
    def reduce(self):

        if DEBUG:
            print("Reducing: %s" % str(self))

        while True:

            actionTaken = False

            # Scan the tree to find actionable items
            nodeMap,explodable,splittable = self.scanTree()

            # EXPLODE (if applicable)
            if len(explodable) == 1:
                node = explodable.pop()
                node.explode(nodeMap)
                actionTaken = True

            # SPLIT (if applicable)
            elif len(splittable) == 1:
                node = splittable.pop()
                node.split()
                actionTaken = True

            # Stop reducing if no actions were taken
            if not actionTaken:
                break
        
        if DEBUG:
            print("Result: %s" %str(self))


    # Use Depth First search to scan the tree and get details on Explodable and Splittable nodes
    def scanTree(self):

        '''
            Each tuple in the queue contains:
                node = the node in the graph (could be pair or digit)
                parent = the parent node of the current node
                depth = the depth away from root
        '''

        # Setup queue, with root node first
        theQueue = deque()        
        theQueue.append( (self, None, 0) )

        digits = []
        neighborMap = {}
        parents = []
        sides = []
        explodable = []
        splittable = []
        checking = []
        
        # Use DFS to get the left/right digits based on left-side priority of nodes
        while theQueue:

            node,parent,depth = theQueue.pop()
            nodeType = type(node)


            if nodeType == Pair and node not in neighborMap:
                neighborMap[node] = {"left":None, "right": None}


            # This is a "leaf", and nothing left to expand
            if nodeType == int:
                
                # Check if previous digit/parent was added:
                if len(parents) > 0 and parents[-1] != parent:
                    prevNode = parents[-1]
                    neighborMap[parent]["left"] = prevNode
                    neighborMap[prevNode]["right"] = parent
                
                digits.append(node)
                parents.append(parent)

                # Add splits
                if node >= 10 and len(splittable) == 0:
                    splittable.append(parent)

                continue

            elif nodeType == Pair and depth >= 4 and node.isAllDigits() and len(explodable) == 0:
            
                explodable.append(node)

            
            # Adding right first, so it's checked last
            theQueue.append( (node.right, node, depth+1) )

            # Adding left last, so it's popped first
            theQueue.append( (node.left, node, depth+1) )

        return neighborMap,explodable,splittable


    # Explode a pair if it is too deep
    def explode(self,nodeMap):

        if DEBUG:
            print("\t\tEXPLODING: %s ; parent=%s" % ( str(self), str(self.parent)))
            print("\n")

        # Get left node
        left = nodeMap[self]["left"]
        if left is not None:
            left.increaseDigit(self.left, "left")

        # Get right node
        right = nodeMap[self]["right"]
        if right is not None:
            right.increaseDigit(self.right, "right")

        # Set the pair (right) to a zero (if applicable)                
        if self.parent.right == self:
            self.parent.right = 0

        # Set the pair (left) to a zero (if applicable)                
        if self.parent.left == self:
            self.parent.left = 0
        

    # Split a given node's higher value (prioritizing left)
    def split(self):

        value = None
        side = None

        if type(self.left) == int and self.left >= 10:
            value = self.left
            side = "left"
        elif type(self.right) == int and self.right >= 10:
            value = self.right
            side = "right"

        if DEBUG:
            print("\t\tSPLITTING: %s (value=%d)" %(str(self), value))
            print("\n")

        # Create the split pair
        if value is not None and side is not None:
            # Setup new split pair
            newLeft = floor(value/2)
            newRight = ceil(value/2)
            newPair = Pair( [newLeft, newRight], self )

            # Reassign the split pair, and account for explode if needed
            if side == "left":
                self.left = newPair

            elif side == "right":
                self.right = newPair
        


    # Get magnitude of the current number
    def getMagnitude(self):

        leftVal = 0
        rightVal = 0

        if type(self.left) == Pair:
            leftVal = self.left.getMagnitude()
        else: 
            leftVal = self.left

        if type(self.right) == Pair:
            rightVal = self.right.getMagnitude()
        else: 
            rightVal = self.right

        
        return (3*leftVal) + (2*rightVal)


    # HELPER: Increase the digit of the respective node by the given value
    def increaseDigit(self, value, comingFrom):

        # Prioritize left side integers if expanding from right
        if comingFrom == "right":
            if type(self.left) == int:
                self.left += value
            elif type(self.right) == int:
                self.right += value

        # Otherwise, prioritize right side value if expanding from left
        elif comingFrom == "left":
            if type(self.right) == int:
                self.right += value
            elif type(self.left) == int:
                self.left += value


    # HELPER METHOD: Returns if the current pair contains all digits
    def isAllDigits(self):
        isDigits = type(self.left) == int and type(self.right) == int
        return isDigits



