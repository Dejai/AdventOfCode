import shared
from helper import Pair
'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./input.txt")


'''
***************************************************************
   Functions
***************************************************************
'''

# Add 2 numbers
def add2Numbers(number1, number2):

    resultingPair = Pair()

    number1.parent = resultingPair
    number2.parent = resultingPair

    resultingPair.left = number1
    resultingPair.right = number2

    return resultingPair


# Compare the magnitudes of 2 numbers
def compareMagnitudes(number1, number2):

    added = add2Numbers( Pair(eval(number1)), Pair(eval(number2)) )
    added.reduce()

    magnitude = added.getMagnitude()

    return magnitude



# Test an addition (confirming the end results)
def testAddition(number1, number2, expected):

    added = add2Numbers( Pair(eval(number1)), Pair(eval(number2)) )
    added.reduce()
    print(added.getMagnitude())

    results = str(added)

    print("Expected:\t %s"  % str(expected))
    print("What I got:\t %s"  % results)
    print("-"*50)
    print( str(expected) == results )
    print("-"*50)



'''
***************************************************************
    Run
***************************************************************
'''

snailfishNums = inputList[:]
allCombined = Pair(eval(snailfishNums[0]))
largestMagnitude = 0

for idx in range(0, len(snailfishNums)):

    currNumber = snailfishNums[idx]

    for idx2 in range(0, len(snailfishNums)):

        # No need to add a number to itself
        if idx2 == idx:
            continue

        nthNumber = snailfishNums[idx2]

        # For Part 1
        if idx == 0 and idx2 > 0:
            nextCombo = add2Numbers(allCombined, Pair(eval(nthNumber)) )
            nextCombo.reduce()
            allCombined = nextCombo

        # Fort Part 2
        comboMagnitude = compareMagnitudes(currNumber, nthNumber)
        largestMagnitude = max(largestMagnitude, comboMagnitude)
    
# Part 1
shared.printAnswer(allCombined.getMagnitude())

# Part 2
shared.printAnswer(largestMagnitude,2)

# TESTING:
#testAddition("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]","[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]","[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]")
#testAddition("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]", "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
#testAddition("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]","[7,[5,[[3,8],[1,4]]]]","[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
#testAddition("[[[[1,1],[2,2]],[3,3]],[4,4]]")