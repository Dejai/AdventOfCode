import shared

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
# Convert binary to key
def convertBinarytoKey(value):
    preceeding = "0" * (9-len(value))
    binary = preceeding + value

    key = binary.replace("0",".").replace("1","#")
    return key


# Get the mapping of all possible keys to their corresponding image algorithm output
def getMap(imageAlgo):
    keyMap = {}
    for idx in range(0,512):
        key = convertBinarytoKey( format(idx,'b') )
        value = imageAlgo[idx]
        keyMap[key] = value

    return keyMap


# Setup the "canvas" of the given image
def createCanvas(input):
    canvas = []
    for val in input:
        row = []
        for char in val:
            row.append(char)
        canvas.append(row)

    return canvas


# Adds 1 column/row surrounding the given canvas
def expandCanvas(canvas, default):

    newCanvas = canvas[:]

    width = len(newCanvas[0])
    
    newCanvas.insert(0,[default]*width)
    newCanvas.append([default]*width)

    for row in newCanvas:
        row.insert(0,default)
        row.append(default)
    
    return newCanvas


# Process canvas
def processCanvas(expandedCanvas,default):

    global keyMap
    global imageAlgo

    # Dimensions of canvas
    height = len(expandedCanvas)
    width = len(expandedCanvas[0])

    # Store the newly formed rows; Used to make new canvas
    latestRows = []

    for rowIdx in range(0,height):

        newRowCopy = ["."]*width

        for colIdx in range(0,width):

            aboveLeft = expandedCanvas[rowIdx-1][colIdx-1] if rowIdx > 0 and colIdx > 0 else default
            above = expandedCanvas[rowIdx-1][colIdx] if rowIdx > 0 else default
            aboveRight = expandedCanvas[rowIdx-1][colIdx+1] if rowIdx > 0 and colIdx < width-1 else default
            
            left = expandedCanvas[rowIdx][colIdx-1] if colIdx > 0 else default
            center = expandedCanvas[rowIdx][colIdx]
            right = expandedCanvas[rowIdx][colIdx+1] if colIdx < width-1 else default
            
            belowLeft = expandedCanvas[rowIdx+1][colIdx-1] if rowIdx < height-1 and colIdx > 0 else default
            below = expandedCanvas[rowIdx+1][colIdx] if rowIdx < height-1 else default
            belowRight = expandedCanvas[rowIdx+1][colIdx+1] if rowIdx < height-1 and colIdx < width-1 else default

            ninePixels = [aboveLeft, above, aboveRight, left, center, right, belowLeft, below, belowRight ]

            # Get the new pixel
            key = "".join(ninePixels)
            value = keyMap[key]

            newRowCopy[colIdx] = value
        latestRows.append(newRowCopy)
    
    nextCanvas = createCanvas(latestRows)
    return nextCanvas

    
# Print the "canvas" so it looks similar to AoC page
def printCanvas(canvas):

    lit = 0
    lit2 = 0

    for row in canvas:
        subRow = row[2:-2]

        val = "".join(row)
        lit += val.count("#")
        print(val)

        val2 = "".join(subRow)
        lit2 += val2.count("#")
    
    print("Total Lit = " + str(lit))
    print("\n")



# Iterate the process of updating the canvas
def iterateCanvasUpdate(canvas, iterations):

    infiniteFlag = None
    
    for idx in range(0,iterations):
        
        default = infiniteFlag if infiniteFlag is not None else "."

        expandedCanvas = expandCanvas(canvas, default)
        nextCanvas = processCanvas(expandedCanvas, default)
        canvas = nextCanvas

        infiniteFlag = keyMap[default*9]

    printCanvas(canvas)

    

'''
***************************************************************
    Run
***************************************************************
'''


imageAlgo = inputList.pop(0)
keyMap = getMap(imageAlgo)
canvas = createCanvas(inputList)

# Part 1
iterateCanvasUpdate(canvas,2)

# Part 2
iterateCanvasUpdate(canvas,50)