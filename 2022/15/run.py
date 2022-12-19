
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

# Returns coordinates as a set of [(x,y),(x,y)] for source,beacon
def getCoordinates(line):
    coordinates = {}

    splits = line.split(":")

    # Get coordinates as a string
    x1,y1 = splits[0].replace("Sensor at x=","").replace(" y=","").split(",")
    x2,y2 = splits[1].replace(" closest beacon is at x=","").replace(" y=","").split(",")

    # Get the source and beacon coordinates
    sensor = (int(x1), int(y1))
    beacon = (int(x2), int(y2))
    distance = getManhattanDist(sensor, beacon)
    return (sensor, beacon, distance)

# Manhattan Distance
def getManhattanDist(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    dist = abs(x1-x2) + abs(y1-y2)
    return dist


def getNoBeaconCoords(source, distance):

    coordinateSet = set()

    # Get the X and Y values
    # x1,y1 = source.split(",")
    # x = int(x1)
    # y = int(y1)

    x,y = source

    for idx in range(0,distance+1):

        # How many columns to span
        span = distance-idx

        # Get rows above and below 
        rowAbove = y-idx
        rowBelow = y+idx
        for idx in range(x-span, x+(span+1)):
            keyAbove = "{0},{1}".format(idx,rowAbove)
            keyBelow = "{0},{1}".format(idx,rowBelow)
            coordinateSet.add(keyAbove)
            coordinateSet.add(keyBelow)

    coordinates = list(coordinateSet)
    coordinates.sort()
    return coordinates



'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = exampleInput
# print(inputList)


maxCoords = [0,0]

maxCol = 0
minCol = 0

# Map of coordinates (stored in dictionary)
coordinates = []

# Get the details for sensor, beacon, and distance
for line in inputList:
   sensor,beacon,distance = getCoordinates(line)
   print("{0} ---> distance:{1}".format(line, distance))
   coordinates.append((sensor, beacon, distance))

   t = getNoBeaconCoords(sensor,distance)
   print("\t" + str(t))

   maxCol = max(maxCol, sensor[0], beacon[0])
   minCol = min(minCol, sensor[0], beacon[0])

print("Min,Max = ( {0}, {1} )".format(minCol, maxCol))


# sourceLocations = set()

# mostLeftSourceCol = float('inf')
# mostLeftSource = None

# mostRightSourceCol = 0
# mostRightSource = None
# for s in coordinates:
#     if s[0][0] < mostLeftSourceCol:
#         mostLeftSource = s
#         mostLeftSourceCol = s[0][0]
#     if s[0][0] > mostRightSourceCol:
#         mostRightSource = s
#         mostRightSourceCol = s[0][0]

# print(mostLeftSource)
# print(mostRightSource)
# 3891093
# 46556

# The set of existing/known beacons
beacons = [ s[1] for s in coordinates ]


noBeaconCoords = set()
rowToCheck = 2000000 if (inputList == realInput) else 10


rowBeacons = [ s for s in coordinates if s[1][1] == rowToCheck and s[1] in beacons ]
columnsToCheck = range(-91140,3992558)

print(len(rowBeacons))
print(len(columnsToCheck))


# sourceLeft = [ s for s in coordinates if s[0][0] == -91140 or s[1][0] == -91140 ]
# minCol2 = 0
# for x in sourceLeft:
#     minCol2 = min(minCol2, (x[0][1] - x[2]), )
#     print(x)


#4083699 (too low) 
#4083699 + 158520 + 244555

#4486774 (too low)
#4486772
#4553708 (too low)
#4886370

# 12068809 not right 
# columnsToCheck = range(minCol-1, maxCol+1)
columnsToCheck = range(minCol-maxCol, maxCol+maxCol)
# columnsToCheck = range(-4083698,7985116)
# Left -249660,-91140
# Right 3992558, 4304053 
count = 0
total = len(columnsToCheck)

# Loop through the possible columns & get the ones that we know cannot be it
# checked = set()
# for col in columnsToCheck:
#     pointToCheck = (col,rowToCheck)
#     count += 1
#     print("Checking {0} of {1}".format(count,total))
#     for s in coordinates:
#         d = getManhattanDist(pointToCheck, s[0])
#         if d <= s[2]  and pointToCheck not in beacons:
#             # print("{0} --> {1}~{2} at dist: {3} < {4}".format( str(pointToCheck),  str(s[0]), str(s[2]), d, s[2]))
#             noBeaconCoords.add(pointToCheck)
#             break



# Print answer for Part 1
a1 = len(noBeaconCoords)
helper.printAnswer(1,a1)

# # Print answer for Part 2
# helper.printAnswer(2,a2)