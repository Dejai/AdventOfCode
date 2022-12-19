
import helper
from classes import Packet,Pair

'''
***************************************************************
    Input
***************************************************************
'''

exampleInput = helper.getFileContentAsList("./example.txt")
realInput = helper.getFileContentAsList("./input.txt")
testInput = helper.getFileContentAsList("./inputTest.txt")

'''
***************************************************************
    Functions
***************************************************************
'''

# Get the packets & Pairs
def getPacketDetails(inptuList):

    pairs = []
    packets = []

    for idx in range(0, len(inputList)):

        packetPair = inputList[idx]
        packetCouple = packetPair.split("\n")
        packet1 = Packet(packetCouple[0])
        packet2 = Packet(packetCouple[1])
        pair = Pair(idx+1, packet1, packet2)

        packets.append(packet1)
        packets.append(packet2)
        pairs.append(pair)

    return packets,pairs


# Sort the packets
def sortPackets(packetList):
    print("Sorting packets ..... ")
    idx = 0
    while True:
        if idx == len(packetList)-1:
            packetNames = [ p.Name for p in packetList ]
            return packetNames

        p1 = packetList[idx]
        p2 = packetList[idx+1]
        
        if p1.compareTo(p2):
            idx += 1
            continue
        else:
            temp = packetList[idx+1]
            packetList[idx+1] = packetList[idx]
            packetList[idx] = temp
            idx = 0 


'''
***************************************************************
    Run
***************************************************************
'''

# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
packets,pairs = getPacketDetails(inputList)
a1 = sum([p.Index for p in pairs if p.RightOrder == True])
helper.printAnswer(1,a1)

# Print answer for Part 2
runPt2 = input("Do you want to run part 2 (it takes a little while)? (y/n): ")
if runPt2 == "y":
    # Add the two new packets
    packet1,packet2 = [ "[[2]]", "[[6]]" ]
    packets.append( Packet(packet1) )
    packets.append( Packet(packet2) )

    # Sort the packets
    sortedPacketNames = sortPackets(packets)

    # Get index of dividers
    idx1, idx2 = [ sortedPacketNames.index(packet1)+1, sortedPacketNames.index(packet2)+1 ]
    a2 = idx1 * idx2
    helper.printAnswer(2, a2)
    