
# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [x for x in content.split("\n") if x != '']


part = "One"

# Track which points have been crossed
pointsCrossed = {}

# Keep track of a point being crossed
def updatePointCrossed(point):
    global pointsCrossed

    pointString = str(point)

    if(pointString in pointsCrossed):
        pointsCrossed[pointString] += 1
    else:
        pointsCrossed[pointString] = 1


# Get points between 2 points, and update frequency of a point crossed
def getPointsBetween(point1, point2):

    # Coordinates from point 1
    x1 = point1[0]
    y1 = point1[1]
    # Coordinates from point 2
    x2 = point2[0]
    y2 = point2[1]

    # Increment/decrement for X coordinate
    xDiff = 0
    if( (x1 - x2) < 0 ):
        xDiff = 1
    elif ( (x1 - x2) > 0 ):
        xDiff = -1

    # Increment/decrement for Y  coordinate
    yDiff = 0
    if( (y1 - y2) < 0 ):
        yDiff = 1
    elif ( (y1 - y2) > 0 ):
        yDiff = -1

    # Part 1 - skip diagonals
    if( (part == "One") and xDiff != 0 and yDiff != 0):
        return

    # Mark the two points as being crossed
    updatePointCrossed(point1)
    updatePointCrossed(point2)

    findPoints = True
    newPoint = point1
    while findPoints:
        newX = newPoint[0] + xDiff
        newY = newPoint[1] + yDiff
        newPoint = [newX, newY]
        if newPoint != point2:
            updatePointCrossed(newPoint)
        else:
            findPoints = True
            break          


# Loop through input to get points
for line in inputList:
    coords = line.split(" -> ")
    point1 = [ int(i) for i in coords[0].split(",")]
    point2 = [ int(i) for i in coords[1].split(",") ]

    isHorizontal = point1[1] == point2[1]
    isVertical = point1[0] == point2[0]

    getPointsBetween(point1, point2)


totalOverlap = 0

for key in pointsCrossed:
    if(pointsCrossed[key] >= 2):
        totalOverlap += 1

print("Total Overlap = " + str(totalOverlap))
