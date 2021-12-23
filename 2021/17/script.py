import shared

'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./input.txt")

expected = shared.getFileContentAsList("./expected.txt")


'''
***************************************************************
    Functions
***************************************************************
'''

# Check if a coordinate is beyond the target range
def getTargets(inputList):
    inputVal = inputList[0]
    targets = inputVal[ inputVal.index(":")+1: ].split(",")

    xTargets = targets[0].strip().replace("x=","").split("..")
    yTargets = targets[1].strip().replace("y=","").split("..")


    xMin = int(xTargets[0])
    xMax = int(xTargets[1])

    yMin = int(yTargets[0])
    yMax = int(yTargets[1])

    return ( (xMin, xMax), (yMin, yMax) )


# Get start/end values to check for initial velocities
def getInitialVelocityRanges(xRange, yRange):

    xStart = min(0, xRange[0], xRange[1], abs(xRange[0]), abs(xRange[1]))
    xEnd = max(xRange[0], xRange[1], abs(xRange[0]), abs(xRange[1]))

    yStart = min(yRange[0], yRange[1], abs(yRange[0]), abs(yRange[1]))
    yEnd = max(yRange[0], yRange[1], abs(yRange[0]), abs(yRange[1]))

    return (xStart, xEnd, yStart, yEnd)


# Get the results of a trajactory based on initial velocity
def getTrajectoryResults(xV, yV, xRangeVals, yRangeVals):

    
    highestPoint = 0
    hitTarget = False

    # The edge/limit of the target area
    xEdge = xRangeVals[-1]
    yEdge = yRangeVals[0]

    debug = False

    x = 0
    y = 0

    while True:

        # Update position
        x += xV
        y += yV

        if(debug):
            print(x, y)

        # Update the highest point
        if y > highestPoint:
            highestPoint = y


        # Update velocities
        xV += 1 if (xV < 0) else (-1 if (xV > 0) else 0)
        yV += -1

        # Check if in range
        inRange = (x in xRangeVals) and (y in yRangeVals)

        # Check if gone too far
        x_too_far = True if (xEdge > 0 and x > xEdge) or (xEdge < 0 and x < xEdge) else False
        y_too_far = True if (yEdge > 0 and y > yEdge) or (yEdge < 0 and y < yEdge) else False


        if inRange:
            hitTarget = True
            break
        if x_too_far or y_too_far:
            #print("Gone too far!")
            break

    return (highestPoint, hitTarget)


'''
***************************************************************
    Run
***************************************************************
'''

xRange, yRange = getTargets(inputList)

# Get the range values
xRangeVals = [ x for x in range(xRange[0], xRange[1]+1) ]
yRangeVals = [ y for y in range(yRange[0], yRange[1]+1) ]

# Get the start/end vals
xStart, xEnd, yStart, yEnd = getInitialVelocityRanges(xRange, yRange)

# Part 1
bestVelocity = 0
bestHeight = 0

hitVelocities = []

for x in range(xStart, xEnd+1 ):
    for y in range(yStart, yEnd+1 ):

        # Get the highest point and if it hit target or not
        height,hit = getTrajectoryResults(x,y, xRangeVals, yRangeVals)

        if (hit):
            hitVelocity = format("%d,%d" % (x,y))
            if hitVelocity not in hitVelocities:
                hitVelocities.append( hitVelocity )

            bestVelocity = y if y > bestVelocity else bestVelocity
            bestHeight = height if height > bestHeight else bestHeight

shared.printAnswer(bestHeight)

# Part 2
shared.printAnswer(len(hitVelocities), 2)

#shared.validateResults(expected,hitVelocities)