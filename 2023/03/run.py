
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
def processSchematic(inputList):
    totals = 0
    gears = {}
    for rowIdx in range(0, len(inputList)):
        currRow = inputList[rowIdx] 
        modRow = currRow + "." # Add a dot to increase line length (to account for numbers at the end of the line)
        num = ""
        for colIdx in range(0, len(modRow)):
            char = modRow[colIdx]         
            if char.isdigit():
                num += char
            else:
                # If the current number is a digit
                if num.isdigit():
                    #  Loop through adjacent rows & check if we should add this number to totals
                    addNum = False 
                    for subRowIdx in range(rowIdx-1, rowIdx+2):
                        startNumIdx = colIdx-len(num)
                        endNumIdx = colIdx-1
                        for subColIdx in range( startNumIdx-1, endNumIdx+2):
                            # If this index isn't possible, don't bother
                            if subRowIdx < 0 or subRowIdx >= len(inputList) or subColIdx < 0 or subColIdx >= len(currRow):
                                continue
                            # Compare current char to another char
                            comparisonChar = inputList[subRowIdx][subColIdx]
                            if not comparisonChar.isdigit() and comparisonChar != ".":
                                addNum = True
                                if(comparisonChar == "*"):
                                    gearKey = "{0}-{1}".format(subRowIdx, subColIdx)
                                    if gearKey not in gears:
                                        gears[gearKey] = list()
                                    gears[gearKey].append((int(num)))
                    totals += int(num) if addNum else 0
                num = ""
    return totals,gears

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
ans,gears = processSchematic(inputList)
helper.printAnswer(1,ans)

# Print answer for Part 2
gearRatios = [ (x[0] * x[1]) for x in gears.values() if len(x) == 2 ]
ans2 = sum(gearRatios)
helper.printAnswer(2, ans2)