
import helper
from collections import deque
import re 

'''
***************************************************************
    Input
***************************************************************
'''

exampleInput = helper.getFileContentAsList("./example.txt")
realInput = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions & Class
***************************************************************
'''
class Stack:

    def __init__(self, name):
        self.name = name
        self.crates = deque()

    def __repr__(self):
        return str(self.crates)
    
    # Add single crate to stack
    def addCrate(self, crate):
        self.crates.append(crate)

    # Always move the top crate first
    def moveCrate(self):
        return self.crates.pop()

    # Just get create at top
    def peek(self):
        return self.crates[-1]


## Get the list of stacks and create the appropriate class instance
def getStacks(listOfStacks):

    # A mapping of stacks
    stacks = {}

    # Get the pieces of the stack data (stack nums & crates)
    stackData = listOfStacks.split("\n")
    crateData = stackData[:-1]
    crates = [ re.sub(r'\s{1,4}', "x",x) for x in crateData ]
    crates.reverse()

    stackNums = [ x for x in stackData[-1].split(" ") if x != "" ]
    for num in stackNums:
        if num not in stacks:
            stacks[num] = Stack(num)

    # Add crates to stacks
    for group in crates:
        splits = group.split("x")
        for idx in range(0, len(splits)):
            box = splits[idx]
            if str(idx+1) in stacks and box != "":
                stacks[str(idx+1)].addCrate(splits[idx])

    return stacks

# process the set of stacks with the given instructions
def processStacks(stacks, instructions, crateMoverVersion=9000):
    instSet = instructions.split("\n")

    for line in instSet:
        num,source,dest = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        sourceStack = stacks[source]
        destStack = stacks[dest]

        # Keep track of crates to move
        cratesToMove = []

        # Get the crates to be moved
        for i in range(0,int(num)):
            crate = sourceStack.moveCrate()
            if(crateMoverVersion == 9001):
                cratesToMove.insert(0,crate)
            else:
                cratesToMove.append(crate)
        
        # Move crates to new stack
        for c in cratesToMove:
            destStack.addCrate(c)

    topLetters = [ x.peek().replace("[","").replace("]","") for x in stacks.values() ]
    return "".join(topLetters)

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
stacks = getStacks(inputList[0])
a1 = processStacks(stacks, inputList[1])
helper.printAnswer(1,a1)

# Print answer for Part 2
stacks = getStacks(inputList[0])
a2 = processStacks(stacks, inputList[1], 9001)
helper.printAnswer(2, a2)