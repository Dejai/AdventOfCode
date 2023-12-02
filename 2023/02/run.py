
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
# defaults every cube to 0
def getCubeCounts(red=0, green=0, blue=0):
    return { "red": red, "green": green, "blue": blue}

# Get the product sume of a list of numbers
def productOfList(numList):
    results = 1
    for num in numList:
        results *= num
    return results

# Evaluate a game
def evalGame(gameResults):
    eligible = True
    game,subsets = gameResults.split(": ")
    fewest = getCubeCounts() 
    for cubeSet in subsets.split("; "):
        limits = getCubeCounts(12, 13, 14)
        for cubes in cubeSet.split(", "):
            count,color = cubes.split(" ")
            count = int(count)
            if color in fewest and count > fewest[color]:
                fewest[color] = count
            if color in limits:
                limits[color] -= count
                if limits[color] < 0:
                    eligible = False
    results = (int(game.split(" ")[-1]), eligible, fewest)
    return results

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
evalGames = [ evalGame(x) for x in inputList ]
validGames = [ x[0] for x in evalGames if x[1] is not False ]
ans = sum(validGames)
helper.printAnswer(1,ans)

# Print answer for Part 2
products = [ productOfList(list(x[2].values())) for x in evalGames ]
ans2 = sum(products)
helper.printAnswer(2, ans2)