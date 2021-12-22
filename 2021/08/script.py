# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [ x for x in content.split("\n") if x != '' ]


'''
    Purpose: Get a map of which characters line up with a segment

    Assumptions:
        > 2 letters align with the two right segments (doesn't matter order)
        > 3 letters, two should be mapped already (the right ones), so the last one must be the top
        > 4 letters, two should be mapped already (the right ones), so the last two are either topLeft or middle
'''
def getKnownSegments(inputSet):

    segmentMap = {} # Mapping of positional segment to a character
    charsMapped = [] # Keep track of which chars already mapped

    # Sort the input list and get the ones with length <= 4
    sortedSet = sorted(inputSet, key=len)
    uniqueInput = [ x for x in sortedSet if len(x) <= 4]

    # These are the keys to set in the map
    keysToMap = ["rightTop", "rightBottom", "top", "middle", "leftTop"]

    # Loop through values and chars, and setup map
    for value in uniqueInput:
        
        for char in value:

            alreadyMapped = (char in charsMapped) # don't attempt to map a char if already mapped
            if(alreadyMapped):
                continue

            # Get the next available key and map the char to that.
            segmentMap[keysToMap.pop(0)] = char
            charsMapped.append(char)

    return segmentMap



'''
    Purpose: Take in a value and get the resulting number from it;

    Assumptions:
        > The digits with a unique number of segments can be automatically set/returend
        > For 5 letters - only the '3' digit has the two right positions; And only '5' digit would have the possible "leftTop" char
        > For 6 letters - the '0' digit does not have the middle; And the '9' has both right positions
'''
def getSegmentNumber(segmentMap, value):
    
    # A map for the number based on unique segment count
    uniqueMap = { 2:1, 3:7, 4:4, 7:8}

    number = -1
    valueLength = len(value)
    # First take care of natural assumptions:
    if (valueLength in [2, 3, 4, 7]):
        number = uniqueMap[valueLength]
    elif( valueLength == 5):
        if (segmentMap["rightTop"]) in value and  (segmentMap["rightBottom"] in value):
            number = 3
        elif (segmentMap["middle"] in value) and (segmentMap["leftTop"] in value):
        #elif (segmentMap["middle"] in value) and ( (segmentMap["rightTop"] in value) or (segmentMap["rightBottom"] in value) ):
            number = 5
        else: 
            number = 2
    elif (valueLength == 6):
        if not ((segmentMap["middle"] in value) and (segmentMap["leftTop"] in value)) :
            number = 0
        elif (segmentMap["rightTop"] in value) and (segmentMap["rightBottom"] in value) :
            number = 9
        else:
            number = 6

    return number




totalUnique = 0  # Store unique count (for part 1)
allNumbers = []  # Store the numbers from input to do the sum at the end

currentSum = 0

for line in inputList:

    splits = line.split(" | ")
    input = splits[0].split(" ")
    output = splits[1].split(" ")

    #charMap = getCharDigitMap(input)
    segmentMap = getKnownSegments(input)
    theDigits = ""

    # Part 1 - unique count
    for val in output:
        length = len(val)
        if length in [2,3,4,7]:
            totalUnique += 1

        # Get the number value of each output
        number = getSegmentNumber(segmentMap, val)
        theDigits += str(number)

    # Add number to complete list
    allNumbers.append( int(theDigits) )

    prettyOutput = " ".join(output)
    numSpaces = (35 - len(prettyOutput))
    print("%s: %s%s" % (prettyOutput, (" "*numSpaces), theDigits) )

    currentSum += int(theDigits)

print("*"*80)
print("\nPart1: Total unique = %d" % (totalUnique))

print("\nPart 2: Sum of outputs: %d" % sum(allNumbers))