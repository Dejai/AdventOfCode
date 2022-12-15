import json
from collections import deque

class Packet:
    def __init__ (self, items):
        self.Name = str(items)
        self.Items = self.setItemsList(items)

    def __repr__(self):
        # return "{0} --> {1}".format(self.Name, self.Items)
        return "{0}".format(self.Name)

    def test(self):
        print(self.test)
        for x in self.test:
            print(x)

    def setItemsList(self, items):
        itemsList = json.loads(items)
        numbers = self.getNumbers(itemsList)
        return [ int(x) for x in numbers.split(",") if x != ""]

    # Get the digit values from a packet
    def getNumbers(self, inputList, level=1):
        # If first element is a list & it is empty: return multiple -1 
        if len(inputList) == 1:
            if "list" in str(type(inputList[0])) and len(inputList[0]) == 0:
                return "-1," * level

        # If it is an empty list, return -1
        if len(inputList) == 0:
            return "-1,"

        # Get list of values
        values = ""

        for item in inputList:
            if "int" in str(type(item)):
                # print("Single Value = " + str(item))
                values += str(item)+","
            elif "list" in str(type(item)):
                # print("List Value = " + str(item))
                values += self.getNumbers(item, level+1)

        return values

class Pair:

    def __init__(self, index, packetPair):
        self.Index = index
        self.RightOrder = False

        # Create the packets
        packets = packetPair.split("\n")
        self.Left = Packet(packets[0])
        self.Right = Packet(packets[1])

        # Evaluate packets
        self.evaluatePair()

    def __repr__(self):
        return "{0} = {1} / {2} \n\t{3}\n".format(self.Index, self.Left, self.Right, self.RightOrder) 

    # Compare two packets to determine if they are in order
    def evaluatePair(self):
        self.RightOrder = True

        # Get two pairs of items
        leftQueue = deque(self.Left.Items)
        rightQueue = deque(self.Right.Items)

        idx = 0
        while len(leftQueue) > 0 or len(rightQueue) > 0:

            left = leftQueue.popleft() if len(leftQueue) > 0 else -1
            right = rightQueue.popleft() if len(rightQueue) > 0 else -1

            if len(leftQueue) == 0 and len(rightQueue) > 0:
                self.RightOrder = True
                return
            elif len(leftQueue) > 0 and len(rightQueue) == 0:
                self.RightOrder = False
                return 
            # print("Comparing {0} to {1}".format(left, right))

            if left < right:
                self.RightOrder = True
                return 
            
            if right < left:
                self.RightOrder = False
                return        
                
    # def evaluatePair2(self, left, right):

    #     leftList = self.toList(left)
    #     rightList = self.toList(right)

    #     if leftList[0].isnumeric() and rightList[0].isnumeric():
    #         return leftList[0] < rightList[0]

    #     while len(leftList) > 0 and len(rightList) > 0:
    #         self.evaluatePair2(leftList[idx], rightList[idx])

    #     if left is None and right is not None:
    #         return False
    #     elif left is not None and right is None:
    #         return False 

    #     leftQueue = deque(leftList)
    #     rightQueue = deque(rightList)




        
    def toList(self, val):
        if 'list' not in str(type(val)):
            return list(val)
        else:
            return val
        