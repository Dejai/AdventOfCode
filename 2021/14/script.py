import shared
from collections import deque

'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./input.txt")


'''
***************************************************************
    Class and Functions
***************************************************************
'''

class Pair:

    def __init__(self, name, insert):
        self.name = name
        self.insert = insert
        self.leftChar = name[0]
        self.rightChar = name[1]

    def getResultingPairs(self, count):
        leftPair = self.leftChar + self.insert
        rightPair = self.insert + self.rightChar

        newPairs = [(leftPair,count), (rightPair,count)]
        #newPair = [leftPair, rightPair] #* count
        char = self.insert
        return (newPairs, char)



# Get char frequency
def getCharFrequency(chars, freq={}):
    for c in chars:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

# Get/update frequency of character appearances
def getUniqueAppearances(pairList, freq={}):

    for pair,count in pairList:
        if pair not in freq:
            freq[pair] = count
        else:
            freq[pair] += count

    return freq


# Compare Most vs. Least common frequencies
def compareFreq(freq):
    largest = 0
    smallest = float("inf")

    for key in freq:

        count = freq[key]
        largest = count if count > largest else largest
        smallest = count if count < smallest else smallest

    return largest-smallest


# Get the initial polymer, and pair objects
def getInitialState(inputList):
    polymer = inputList[0]
    mapping = inputList[1:]

    # character frequency
    freq = {}

    # The pair objects
    pairs = {}

    for map in mapping:
        splits = map.split(" -> ")
        name = splits[0]
        insert = splits[1]

        pair = Pair(name, insert)

        pairs[name] = pair

    # Get initial frequency
    for c in polymer:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    return (polymer, pairs)


'''
***************************************************************
    Run
***************************************************************
'''

polymer,pairs = getInitialState(inputList)
print("Initial Polymer: %s\n%s " % (polymer, ("*"*100)))

# Setup the initial pairs, frequency and grouped pairs
initialPairs = [ ( (polymer[x]+polymer[x+1],1) ) for x in range(0,len(polymer)-1 ) ]
uniqPairs = getUniqueAppearances(initialPairs)

# Setup the queue
theQueue = deque()
theQueue.append(uniqPairs)

# Get an initial character frequency
charFreq = getCharFrequency(polymer)

# Set limit and loop
limit = 40
counter = 0
while True:


    if counter == limit:
        res = compareFreq(charFreq)
        print("Most common minus Least Common == %d" % res)
        break

    print("After step %d" % int(counter+1))

    # Pop th enext group to check
    nextBatch = theQueue.popleft()
    groups = [ x for x in nextBatch]

    
    # Storing frequency for next batch to be queued
    apperances = {}

    #for group in groups:
    for pair in nextBatch:
        pairObj = pairs[pair]
        count = nextBatch[pair]

        newPairs,char = pairObj.getResultingPairs(count)

        # Evaluate the number of apperaances
        apperances = getUniqueAppearances(newPairs, apperances)

        # Update the character appearances
        if char not in charFreq:
            charFreq[char] = count
        else:
            charFreq[char] += count
    
    theQueue.append(apperances)

    counter += 1