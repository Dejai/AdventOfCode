import json
from collections import deque


# Represents a single packet
class Packet:
    def __init__ (self, items):
        self.Name = str(items)
        self.Items = json.loads(items)
        
    def __repr__(self):
        return "{0}".format(self.Name)

    # Compare this packet to another packet: Returns TRUE if less than, otherwise, FALSE
    def compareTo(self, packet):
        results = self.comparePackets(self.Items, packet.Items)
        return results

    # Evaluate if the packet pairs are in order
    def comparePackets(self, left, right):

        leftQueue = deque(self.toList(left))
        rightQueue = deque(self.toList(right))

        while True:
            leftItem = leftQueue.popleft() if len(leftQueue) > 0 else None
            rightItem = rightQueue.popleft() if len(rightQueue) > 0 else None

            # print("Comparing: {0} ..... {1}".format(leftItem, rightItem))

            # Get types
            leftType = self.getType(leftItem)
            rightType = self.getType(rightItem)

            # Check to see which lists run out ... and when 
            if leftItem is None and rightItem is None:
                return None 
            elif leftItem is None and rightItem is not None:
                return True
            elif rightItem is None and leftItem is not None:
                return False

            # Compare values
            if leftType == "INT" and rightType == "INT":
                
                if leftItem == rightItem:
                    continue
                elif leftItem < rightItem:
                    return True
                elif rightItem < leftItem:
                    return False
            else:
                result = self.comparePackets(leftItem, rightItem)

                if result is not None:
                    return result
                else:
                    continue      

    # Get the type of an item
    def getType(self, value):

        if "int" in str(type(value)):
            return "INT"
        return "LIST"

    # Ensure every item is converted to a list for comparison
    def toList(self, value):
        if 'list' not in str(type(value)):
            return [value]
        else:
            return value

# Represents a pair of packet
class Pair:

    def __init__(self, index, packet1, packet2):
    # def __init__(self, index,packetPair):
        self.Index = index
        self.Left = packet1
        self.Right = packet2

        # Evaluate packets
        self.RightOrder = self.Left.compareTo(self.Right)

    def __repr__(self):
        return "{0} = {1} / {2} \n\t{3}\n".format(self.Index, self.Left, self.Right, self.RightOrder)