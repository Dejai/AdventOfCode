
from mypackage import helper

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions
***************************************************************
'''
def getNextValue(inputList, backwards=False):
    history = [ inputList[idx+1] - inputList[idx] for idx,i in enumerate(inputList[:-1])]
    historySet = set(history)
    if len(historySet) == 1 and history[0] == 0:
        return inputList[0] - history[0] if backwards else inputList[-1] + 0
    return inputList[0] - getNextValue(history, backwards=True) if backwards else inputList[-1] + getNextValue(history)

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
intLists = [ helper.toList(x, type="int") for x in inputList]
ans1 = sum([ getNextValue(y) for y in intLists] )
helper.printAnswer(1,ans1)

# Print answer for Part 2
ans2 = sum([ getNextValue(y, backwards=True) for y in intLists] )
helper.printAnswer(2, ans2)