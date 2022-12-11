
import helper
from classes import Monkey
import sys
import math

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
printRounds = False


# Get set of monkeys
def getMonkeys(inputList):
    monkeys = {}
    for details in inputList:
        monkey = Monkey(details)
        monkeys[monkey.Name] = monkey
    return monkeys

# Run the rounds of shenanigans 
def shenanigans(monkeyMap, rounds, divideFactor=None):

    for idx in range(0,rounds):
        for monkey in monkeyMap.values():
            currentTurn = True
            while currentTurn:
                passToMonkey,value = monkey.inspectItem(divideFactor)
                if(passToMonkey is not None):
                    monkeyMap[passToMonkey].addItem(value)
                else:
                    currentTurn = False
        if(printRounds):
            print("== After round {0} ==".format(idx+1))
            for monkey in monkeys.values():
                print("Monkey {0} inspected items {1} times".format(monkey.Name, str(monkey.NumItemsInspected)))
            print("\n")
    
    itemsInspected = [ monkey.NumItemsInspected for monkey in monkeyMap.values()]
    itemsInspected.sort()
    return (itemsInspected[-2] * itemsInspected[-1])

# Try to predict monkey business after a certain amount of rounds
# Got idea for solution from: https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izsn7we/?utm_source=share&utm_medium=web2x&context=3
def getLCM(monkeys):
    divisibles = [ int(m.Divisible) for m in monkeys.values() ]
    return math.lcm(*divisibles)



'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print the output after each round?
printRounds = False 

# Print answer for Part 1
monkeys = getMonkeys(inputList)
a1 = shenanigans(monkeys, 20)
helper.printAnswer(1,a1)

# Print answer for Part 2
monkeys = getMonkeys(inputList)
a2 = shenanigans(monkeys, 10000, getLCM(monkeys) )
helper.printAnswer(2, a2)
