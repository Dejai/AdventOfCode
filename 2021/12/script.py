# Import modules
from collections import deque
import shared
from helper import createCaves


# Get the input
inputList = shared.getFileContentAsList("./input.txt")


# Check if a cave can be added
def canAddNextCave(path, cave, limit=0):

    if(not cave.isSmall()):
        return True

    
    caveName = cave.name

    # Check if cave not in path
    notInPath = (caveName not in path)

    allowedDup = True if limit > 0 else False
    seen = ""
    dupCount = 0
    if(limit > 0):

        pathList = path.split(",")
        #print(pathList)
        smallCaves = [ x for x in pathList if (x not in ["start"] and x == x.lower() and x != ''  ) ]
        #print(smallCaves)

        for x in smallCaves:
            
            dupCount += 1 if x in seen else 0
            if(dupCount == limit):
                allowedDup = False
            
            seen += x

    addSmallAgain = allowedDup and caveName in path

    canAdd = notInPath or addSmallAgain

    return canAdd

    
# Get the different paths to the target cave
def getPaths(start, target, duplicateLimit=0):

    theQueue = deque()
    paths = []  # Store all paths found

    # Determine if duplicates are allowed; And how many already accounted for
    isAllowedDuplicate = True if duplicateLimit > 0 else False
    duplicateCount = 0

    # Add all the ones from the "Start" to the queue
    for adjacentCave in start.adjacentCaves:
        pair = (adjacentCave, start.name)
        theQueue.append(pair)


    # Loop until the queue is empty
    while theQueue:

        # Pop the next value to check from queue
        cave,path = theQueue.popleft()

        # Update path
        path += ","+cave.name

        # If th target/end cave, then append to list of paths
        if(cave.name == target.name):
            paths.append(path)
            continue
        else:

            # Get adjacent caves from this latest cave
            for nextCave in  cave.adjacentCaves:           

                # Can this cave be added to queue?
                canAddCave = canAddNextCave(path, nextCave, duplicateLimit)
                
                if(canAddCave):
                    pair = (nextCave, path)
                    theQueue.append(pair)                

    return paths



# Create the Cave objects; Returns a MAP of cave name to cave object
caves = createCaves(inputList)
# Get the starting and target caves
start = caves["start"]
target = caves["end"]
           
# Part 1 
pathsList = getPaths(start, target)
shared.printAnswer(len(pathsList))

# Part 2 - includ limit for number of revisits
pathsList = getPaths(start, target, 1)
shared.printAnswer(len(pathsList))

# Validation
# expected = shared.getFileContentAsList("./expected1_pt2.txt")
# shared.validateResults(expected, pathsList)
# #shared.validateCount(226, len(pathsList))