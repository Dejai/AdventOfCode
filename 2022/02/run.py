
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
# Rock (A, X) / Paper (B, Y) / Scissors (C, Z)
def getScore(oppChoice, myChoice):
    
    choiceMap = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    choiceMapVal = {"A":"Rock", "B":"Paper", "C":"Scissors", "X":"Rock", "Y":"Paper", "Z":"Scissors"}
    
    oVal = choiceMap[oppChoice] #opponent 
    mVal = choiceMap[myChoice] #mine

    outcome = "Draw"
    if oVal > mVal and (oVal != 1 and mVal != 3):
        outcome = "Lose"
    if oVal > mVal and (oVal == 3 and mVal == 1):
        outcome = "Win"
    elif oVal < mVal and (oVal == 1 and mVal == 3):
        outcome = "Lose"
    elif mVal > oVal:
        outcome = "Win"

    # print("{0} -- {1} == {2}".format(choiceMapVal[oppChoice], choiceMapVal[myChoice], outcome))
    outcomeMap = {"Lose":0, "Draw":3, "Win":6}

    return mVal + outcomeMap[outcome]


# Rock (A) / Paper (B) / Scissors (C)
# Lose (X) / Draw (Y) / Win (Z)
def getStrategy(oppChoice, neededOutcome):
    # Mapping what each letters (beats, loses to)
    choiceMap = { 
        "A":["C", "B"],
        "B":["A", "C"],
        "C":["B", "A"]
    }
    score = 0

    if(neededOutcome == "X"):
        score = getScore(oppChoice, choiceMap[oppChoice][0]) 
    elif neededOutcome == "Y":
        score = getScore(oppChoice, oppChoice)
    elif neededOutcome == "Z":
        score = getScore(oppChoice, choiceMap[oppChoice][1])
    
    return score


'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
scores = [ getScore(x[0], x[1]) for x in (y.split(" ") for y in inputList)]
a1 = sum(scores)
helper.printAnswer(1,a1)


# Print answer for Part 2
scores = [ getStrategy(x[0], x[1]) for x in (y.split(" ") for y in inputList)]
a2 = sum(scores)
helper.printAnswer(2, a2)