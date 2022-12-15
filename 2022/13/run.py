
import helper
from classes import Pair

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


'''
***************************************************************
    Run
***************************************************************
'''

# What are we working with; Change this variable to use the real input when ready
inputList = exampleInput
# print(inputList)

# Print answer for Part 1
pairs = []
for idx in range(0, len(inputList)):
    pair = Pair(idx+1,inputList[idx])
    pairs.append(pair)
    print(pair)
a1 = sum([p.Index for p in pairs if p.RightOrder == True])
helper.printAnswer(1,a1)

falses = [p for p in pairs if p.RightOrder == False]
file = open("output.txt", "w+")
for f in falses:
    file.write("{0}\n".format(f))
    file.write("\t{0}\n\t{1}".format(f.Left.Items, f.Right.Items))
    file.write("\n\n")
file.close()

# Too low: 5394
# Too high: 5928


# Print answer for Part 2
# helper.printAnswer(2, "Part 2 Default")