# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [ x for x in content.split("\n") if x != '' ]

# Get the map of octopi
octoMap = []
for value in inputList:
    digits = [int(digit) for digit in value]
    octoMap.append(digits)


# Get the cardinal surrounding points based on current row and col
def getSurroundingPoints(rowIdx, colIdx, width, height):

    aboveIdx = rowIdx-1 if rowIdx > 0 else rowIdx
    belowIdx = rowIdx+1 if rowIdx < height-1 else rowIdx
    rightIdx = colIdx+1 if colIdx < width-1 else colIdx
    leftIdx = colIdx-1 if colIdx > 0 else colIdx

    # Indicate current point - so to avoid it in surrounding points
    currPoint = (rowIdx, colIdx)

    # Surrounding points: Above, RightDiagUp, Right, RightDiagDown, Below, LeftDiagUp, Left, LeftDiagDown
    points = [  (aboveIdx, colIdx), \
                (aboveIdx, rightIdx), \
                (rowIdx, rightIdx), \
                (belowIdx, rightIdx), \
                (belowIdx, colIdx), \
                (belowIdx, leftIdx), \
                (rowIdx, leftIdx), \
                (aboveIdx, leftIdx) \
            ]

    cardinalPoints = []
    for point in points:
        if point not in cardinalPoints and point != currPoint:
            cardinalPoints.append(point)
    
    cardinalPoints.sort()

    return cardinalPoints


# Energize some octopus
def energizeOctopi(octoMap):

    flashes = 0

    height = len(octoMap)
    width = len(octoMap[0])

    flashedMap = [ [ '' for digit in row] for row in octoMap ]
    octoMapCopy = octoMap[:]

    for rowIdx in range(0,height):

        for colIdx in range(0, width):

            # Get all the points that need to be updated
            currPoint = (rowIdx, colIdx)

            # Skip ones that already flashed:
            if (flashedMap[rowIdx][colIdx] == "flashed"):
                continue

            # Keep track of any points that also need to be updated because of a flash
            toBeEnergized = []


            # Increase energy of current point
            octoMapCopy[rowIdx][colIdx] +=1


            # Check if it is flashing
            if ( octoMapCopy[rowIdx][colIdx] == 10):
                flashes += 1
                octoMapCopy[rowIdx][colIdx] = 0
                flashedMap[rowIdx][colIdx] = "flashed"

                toBeEnergized += getSurroundingPoints(rowIdx, colIdx, width, height)

            while True:
                #print("Will attempt to expand")
                if (len(toBeEnergized) == 0):
                    break
                    
                nextPoint = toBeEnergized.pop(0)
                row2 = nextPoint[0]
                col2 = nextPoint[1]
                
                # Skip ones that already flashed:
                if (flashedMap[row2][col2] == "flashed"):
                    continue

                # Increase energy of surrounding point
                octoMapCopy[row2][col2] +=1

                # Check if it is flashing
                if ( octoMapCopy[row2][col2] == 10):
                    flashes += 1
                    octoMapCopy[row2][col2] = 0
                    flashedMap[row2][col2] = "flashed"


                    toBeEnergized += getSurroundingPoints(row2, col2, width, height)

    return (flashes, octoMapCopy)

# Print out the map
def printMap(map):
    for row in map:
        print(row)



PART = "2"  # Set this to run the part of the puzzle. 


magicNum = len(octoMap) * len(octoMap[0])
stateOfEnergy = octoMap[:]
totalFlashes = 0
stepWithAllFlash = 0
step = 0

# Run until some condition is met
while True:
    flashes,newState = energizeOctopi(stateOfEnergy)
    print("\nAfter step %d: " % (step+1) )
    totalFlashes += flashes
    stateOfEnergy = newState
    printMap(stateOfEnergy)
    
    # Break if conditions are met
    if PART == "1" and step == 99:
        break
    elif PART == "2" and flashes == magicNum:
        stepWithAllFlash = step+1
        break
    
    step += 1

print("\nTotal Flashes = %d" % totalFlashes)
print("\nStep when all flashes = %d" % (stepWithAllFlash))