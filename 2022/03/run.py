
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

def getSharedUnique(entry):

    length = len(entry)
    middle = length//2
    c1 = entry[0:middle]
    c2 = entry[middle:]

    l1 = [x for x in c1]
    l2 = [y for y in c2]

    set1 = set(l1)
    set2 = set(l2)

    shared = set1 & set2
    sharedValue = shared.pop()
    return sharedValue

def getSharedUnique3set(elfGroup):

    s1 = set([x for x in elfGroup[0]])
    s2 = set([x for x in elfGroup[1]])
    s3 = set([x for x in elfGroup[2]])

    badge = s1 & s2 & s3
    badgeVal = badge.pop()
    return badgeVal

def getValue(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetList = [x for x in alphabet]
    isUpper = letter.isupper()
    lowered = letter.lower()
    idx = alphabetList.index(lowered)+1
    val = idx + 26 if isUpper else idx
    # print("{} = {}".format(letter, val))
    return val

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)


# Print answer for Part 1
vals = [ getValue(getSharedUnique(x)) for x in inputList]
a1 = sum(vals)
helper.printAnswer(1,a1)


# Print answer for Part 2
vals = []
for i in range(0, len(inputList), 3):
    vals.append(getValue(getSharedUnique3set(inputList[i:i+3])))
a2 = sum(vals)
helper.printAnswer(2, a2)