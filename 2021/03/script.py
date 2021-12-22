


# Function convert input to list
def getInputList(input):
    theList = []
    for line in input:
        theList.append(line.replace("\n", ""))
    return theList

# Get the input list
input = open("./input.txt", "r+")
inputList = getInputList(input)

# Get the length of all expected bits
bitLength = len(inputList[0])

# Get the most common digit at an index
def getCommonValue(type, listOfVals, index):
    chars = [ val[index] for val in listOfVals]
    bits = [0, 0]
    for c in chars:
        digit = int(c)
        bits[digit] += 1

    answer = bits.index(max(bits)) if type == "max" else bits.index(min(bits))
    return answer



'''
    PART ONE: 
'''
gammaRate = ""
epsilonRate = ""

for idx in range(0, bitLength):    
    mostCommon = getCommonValue("max", inputList, idx)
    leastCommon = getCommonValue("min", inputList, idx)

    gammaRate += str(mostCommon)
    epsilonRate += str(leastCommon)

print("\n")
print("Gamma Rate = %s (%d)" % (gammaRate, int(gammaRate, 2)))
print("Epsilon Rate = %s (%d)" %(epsilonRate, int(epsilonRate, 2)))
powerConsumption =  int(gammaRate,2) * int(epsilonRate,2)
print("Power Consumption = %d" % (powerConsumption) )


'''
    PART TWO:
'''
print('\n')

def getRating(type, listOfVals):
    remaining_values = listOfVals[:]
    checkIdx = 0
    stillCheck = True
    while stillCheck:

        mostCommon = getCommonValue("max", remaining_values,checkIdx)
        leastCommon = getCommonValue("min", remaining_values,checkIdx)

        useIdx = mostCommon if type == "max" else leastCommon
        if(mostCommon == leastCommon):
            useIdx = 1 if type == "max" else 0

        new_list = [ x for x in remaining_values if x[checkIdx] == str(useIdx)]
        # update remaining values
        remaining_values = new_list
        if (len(remaining_values) == 1):
            stillCheck = False
        
        checkIdx += 1
    
    return remaining_values[0]

oxygenGenRating = int(getRating("max", inputList), 2)
co2ScrubberRating = int(getRating("min", inputList), 2)

print("Oxygen Generator Rating = %d" %(oxygenGenRating))
print("O2 Scrubber Rating = %d" %(co2ScrubberRating))
lifeSupportRating = oxygenGenRating * co2ScrubberRating
print("Life Support Rating = %d" %(lifeSupportRating))


input.close()
