
import helper

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

def getStartOfPacket(packet, distinct=4):
    
    pList = [ char for char in packet ]
    startOfPacket = -1
    
    for idx in range(0,len(pList)-distinct):
        subset = pList[idx:idx+distinct]
        uniqueChars = set(subset)
        if(len(uniqueChars) == distinct):
            startOfPacket = idx+distinct
            # print("".join(subset))
            break

    return startOfPacket

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)


# Print answer for Part 1
sops = [ getStartOfPacket(x) for x in inputList]
a1 = sops[0]
helper.printAnswer(1,a1)


# Print answer for Part 2
sops = [ getStartOfPacket(x, 14) for x in inputList]
a2 = sops[0]
helper.printAnswer(2, a2)