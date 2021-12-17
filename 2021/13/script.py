import shared

'''
***************************************************************
    Input
***************************************************************
'''


inputList = shared.getFileContentAsList("./input.txt")

# Get the coordinates and the fold instructions
coords = [x for x in inputList if x[0] != 'f']
#Get the folds
folds = [ x.split(" ")[2] for x in inputList if x[0] == 'f' ]


'''
***************************************************************
    Functions
***************************************************************
'''

# Map the current points
def mapPoints(coords):

    map = {}

    rowSize = 0
    colSize = 0

     #Get the details from the input
    for coord in coords:
        col, row = coord.split(',')
        
        col = int(col)
        row = int(row)

        # Update row and column size if applicable
        rowSize = row if row > rowSize else rowSize
        colSize = col if col > colSize else colSize

        if row not in map:
            map[row] = []
        
        map[row].append(col) #[col] = "#"

    return (map, rowSize+1, colSize+1)


# Create a grid of rows/cols
def createGrid(rows, cols):

    global map

    grid = []

    for rowIdx in range(0, rows):

        newRow = []
        rowDetails = map[rowIdx] if (rowIdx in map) else {}

        for colIdx in range(0, cols):
            val = "#" if colIdx in rowDetails else "."
            newRow.append(val)
        
        grid.append(newRow)
    
    return grid
        

# Make a fold and return the new grid
def makeFold(axis, index, grid):

    print("\nFolding along %s=%s" %(axis, index))
    index = int(index)
    visibleDots = 0    
    
    totalRows = len(grid)
    rowLength = len(grid[0])

    newGrid = []


    # If folding via X axis
    if(axis == "x"):
        print("Folding right side to left side")
        for rowIdx in range(0, totalRows):

            row = grid[rowIdx]
            
            # Counters for which element to get on either side of split
            left = -1
            right = 1

            # List for fold
            fold = []

            while True:

                val = "."
                leftIndex = index+left
                rightIndex = index+right
                
                if leftIndex >= 0 and rightIndex <= rowLength-1:
                    v1 = row[index+left]
                    v2 = row[index+right]

                    val = v1 if v1 == "#" else v2

                elif leftIndex < 0 and rightIndex <= rowLength-1:
                    val = row[index+right]

                elif leftIndex >= 0 and rightIndex >= rowLength:
                    val = row[index+left]
                else:
                    break

                if(val == "#"):
                    visibleDots += 1

                fold.insert(0,val)
                left -= 1
                right += 1

            newGrid.append(fold)

    # If folding via y axis
    elif (axis == "y"):
        print("Folding lower side to upper side")

        upper = -1
        lower = 1

        while True:

            val = "."
            upperIndex = index+upper
            lowerIndex = index+lower

            fold = []

            if upperIndex >= 0 and lowerIndex <= totalRows-1:
                row1 = grid[index+upper]
                row2 = grid[index+lower]

                fold = [ (row1[x] if row1[x] == "#" else row2[x])  for x in range(0, rowLength)]

            elif upperIndex < 0 and lowerIndex <= totalRows-1:
                fold = grid[index+lower]

            elif upperIndex >= 0 and lowerIndex >= totalRows:
                fold = grid[index+upper]
            else:
                break

            dots = [ x for x in fold if x == "#"]
            visibleDots += len(dots)

            upper -= 1
            lower += 1

            newGrid.insert(0,fold)

    print("Visible Dots = %d\n" % visibleDots)
    return newGrid

# Print out a grid
def printGrid(grid):
    for row in grid:
        print("\t%s" % ("".join(row)))



'''
***************************************************************
    Run
***************************************************************
'''


map,rows,cols = mapPoints(coords)

print("Rows = " + str(rows))
print("Cols = " + str(cols))

# Create a grid from the rows/cols and the mapped points
newGrid = createGrid(rows,cols)

latestGrid = newGrid[:]
# Loop through the folds
for fold in folds:
    splits = fold.split("=")
    axis = splits[0]
    index = splits[1]

    # Make fold
    latestGrid = makeFold(axis, index, latestGrid)


print("FINAL GRID")    
printGrid(latestGrid)