
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

# Get a range of coordinates
def getCoordRange(point1, point2):

    coords = []

    # Get the Xs; Sorted
    x = [point1[0], point2[0]]
    x.sort()

    # Get the Ys; Sorted
    y = [point1[1], point2[1]]
    y.sort()

    # If same Xs, diff Ys
    if x[0] == x[1]:
        for idx in range(y[0], y[1]+1):
            coords.append( (x[0], idx) ) 
    # Else if diff Xs, same Ys
    elif x[0] != x[1] and y[0] == y[1]:
        for idx in range(x[0], x[1]+1):
            coords.append( (idx, y[0]) ) 
    return coords


# Get the coordinates of walls
def getCoordinates(inputList):

    print("Getting the coordinates ", end="")
    coordinates = []

    # Get coordinates of walls
    for line in inputList:
        coords = [ ( int(x[0]),int(x[1]) ) for x in [y.split(",") for y in line.split(" -> ") ] ]

        # Process these coordinates
        for idx in range (0, len(coords)-1):
            print(".", end="")
            point1 = coords[idx]
            point2 = coords[idx+1]
            coordinates += getCoordRange(point1, point2)

    print("\nDone")
    return coordinates

# Make a grid to follow the sand
def makeGrid(inputList):

    coordinates = getCoordinates(inputList)

    maxX = max([point[1] for point in coordinates])
    maxY = max([point[0] for point in coordinates])

    grid = []
    for row in range(0, maxX+3):
        rowVals = []
        for col in range(0, maxY*2):
            val = "#" if (col,row) in coordinates else "."
            rowVals.append(val)
        grid.append(rowVals)
    
    #Set the starting point
    grid[0][500] = "+"

    # Set the floor
    grid[-1] = ["#" for x in range(0,len(grid[0]))]

    return grid

# Process the falling sand
def fallingSand(grid, until="Abyss"):

    # Check if sand has reached the abyss
    theAbyss = False

    # Values that block
    blocking = ["O", "#"]

    sandUnits = 0
    sandUnitsTillFloor = 0

    # Keep producing units
    keepSandFlowing = True

    # Loop through a set of sand units until criteria reached
    while keepSandFlowing:

        # Start coordinate
        coord = [0,500]

        if grid[0][500] == "O":
            keepSandFlowing = False
            continue

        # Continue dropping sand until settled
        dropSand = True
        while dropSand:

            x = coord[0]
            y = coord[1]

            if x+1 >= len(grid) or y >= len(grid[0]):
                dropSand = False
                print("Stopping at {0}".format((x+1, y)))
                continue

            # If the next coordinate is free
            if grid[x+1][y] == ".":
                coord = [x+1,y]
                continue

            # If next below is blocked
            elif grid[x+1][y] in blocking:
                if grid[x+1][y-1] not in blocking:
                    coord = [x+1,y-1]
                    continue
                elif grid[x+1][y+1] not in blocking:
                    coord = [x+1,y+1]
                    continue
                # No where to go, then settle
                else:
                    grid[x][y] = "O"
                    sandUnits += 1
                    dropSand = False
                    if x+1 == len(grid)-1 and sandUnitsTillFloor == 0:
                        sandUnitsTillFloor += sandUnits-1
                    continue
    
    return grid,sandUnitsTillFloor,sandUnits
    

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

print("Making the grid")
grid = makeGrid(inputList)

print("Falling the sand")
gridOut,a1,a2 = fallingSand(grid)

# Print answer for Part 1
helper.printGrid(gridOut, "grid.txt")
helper.printAnswer(1,a1)

# Print answer for Part 2
helper.printAnswer(2,a2)