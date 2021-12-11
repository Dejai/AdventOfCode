# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [ x for x in content.split("\n") if x != '' ]

heightMap = []
for value in inputList:
    digits = [int(digit) for digit in value]
    heightMap.append(digits)


# Get the individual low points on the height map
def getLowPoints(heightMap):

    rowIdx = 0
    lowPointMap = [ [ '' for x in row] for row in heightMap ]

    theLowPoints = []
    lowPointsCoords = []

    # Loop through heightmap
    for rowIdx in range(0, len(heightMap)):

        currRow = heightMap[rowIdx]
        prevRowIdx = rowIdx-1 if rowIdx > 0 else rowIdx
        nextRowIdx = rowIdx+1 if rowIdx < len(heightMap)-1 else rowIdx

        for colIdx in range(0, len(currRow)):

            # Index of adjacent (left,right) values
            adjacentRightIdx = colIdx+1 if colIdx < len(currRow)-1 else colIdx
            adjacentLeftIdx = colIdx-1 if colIdx > 0 else colIdx

            # Get associated values
            value = heightMap[rowIdx][colIdx]

            # Get the values surrounding the value
            above = heightMap[prevRowIdx][colIdx]
            right = heightMap[rowIdx][adjacentRightIdx]
            below = heightMap[nextRowIdx][colIdx]
            left = heightMap[rowIdx][adjacentLeftIdx]

            # Adjust the values for corners and edges (ensure a value is considerd a low point even on the corner/edge)
            above += 1 if rowIdx == 0 else 0
            below += 1 if rowIdx == len(heightMap)-1 else 0
            left += 1 if colIdx == 0 else 0
            right += 1 if colIdx == len(currRow)-1 else 0

            if (value < above) and (value < right) and (value < below) and (value < left):
                theLowPoints.append(value)
                lowPointMap[rowIdx][colIdx] = "X"
                lowPointsCoords.append( (rowIdx, colIdx))

    return (theLowPoints, lowPointsCoords)


# Get the cardinal surrounding points based on current row and col
def getSurroundingPoints(rowIdx, colIdx, rightEdge, bottomEdge):

    aboveIdx = rowIdx-1 if rowIdx > 0 else rowIdx
    rightIdx = colIdx+1 if colIdx < rightEdge else colIdx
    belowIdx = rowIdx+1 if rowIdx < bottomEdge else rowIdx
    leftIdx = colIdx-1 if colIdx > 0 else colIdx
    
    # Adding the surrounding points: Above, Right, Below, Left
    surroundingPoints = [ (aboveIdx,colIdx), (rowIdx, rightIdx), (belowIdx, colIdx), (rowIdx, leftIdx) ]

    return surroundingPoints

# Gets the group of basins; Returns them sorted in descending order of count
def getBasins(heightMap, lowPointCoords):

    # A pool of possible basins
    basinsPool = [ "basin"+str(i+1) for i in range(0, len(lowPointCoords)) ]

    # Map to keep track of basin count
    basinCountMap = {}

    # Map to track what basin a value is in; Same dimensions as heightMap
    basinMap = [ [ ('?' if digit != 9 else 'n/a') for digit in row] for row in heightMap ]


    rightEdge = len(heightMap[0])-1
    bottomEdge = len(heightMap)-1

    for coord in lowPointCoords:
        row = coord[0]
        col = coord[1]


        basinValue = ""
        if  basinMap[row][col] == "?":
            basinValue = basinsPool.pop(0)
            basinMap[row][col] = basinValue
            basinCountMap[basinValue] = 0
            basinCountMap[basinValue] += 1


        surroundingPoints = getSurroundingPoints(row, col, rightEdge, bottomEdge)
        

        #print("Current Point = %s" % str(coord))
        expandBasin = True
        while expandBasin:
            
            if (len(surroundingPoints) == 0):
                expandBasin = False
                continue
            
            nextPoint = surroundingPoints.pop(0)
            row2 = nextPoint[0]
            col2 = nextPoint[1]
            #print("\tNext Point %s" % str(nextPoint))

            # If it is 9 -- move on
            if(heightMap[row2][col2] == 9):
                continue

            if basinMap[row2][col2] == "?":
                #print("\tAdding to basin = %s" % str(nextPoint))
                basinMap[row2][col2] = basinValue
                basinCountMap[basinValue] += 1

                newSurroundingPoints = getSurroundingPoints(row2, col2, rightEdge, bottomEdge)
                surroundingPoints += newSurroundingPoints
            
    basinTuple = [ (basin,count) for basin,count in basinCountMap.items() ]
    sortedBasins = sorted(basinTuple, key=lambda basin: basin[1], reverse=True )
    return sortedBasins


# Part 1
print("\nPart #1:")
theLowPoints, lowPointCoords = getLowPoints(heightMap)
riskLevel = [ x+1 for x in theLowPoints ]
print(" The low points == %s" % theLowPoints)
print(" The risk == %d" % sum(riskLevel))

# Part 2 
print("\nPart #2:")
basins = getBasins(heightMap, lowPointCoords)
threeLargest = basins[:3]
print("Three Largest Basins = %s" % str(threeLargest))
basinCounts = [ basin[1] for basin in threeLargest[:3]]
answer = basinCounts[0] * basinCounts[1] * basinCounts[2]
print("Total = %d" % answer)