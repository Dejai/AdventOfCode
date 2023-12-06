
from mypackage import helper
from collections import deque

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./example1.txt", "\n\n")

'''
***************************************************************
    Functions & Class
***************************************************************
''' 
class MyRange:
    def __init__(self, details):
        detailsLength = len(details)
        self.Start = int(details[1] if detailsLength == 3 else details[0])
        self.Length = int(details[2] if detailsLength == 3 else details[1])
        self.Range = range(self.Start, self.Start+self.Length)
        self.DestRange = None
        if(detailsLength == 3):
            destStart = int(details[0])
            self.DestRange = MyRange([destStart, self.Length])
        self.Adder = int(details[0]) if detailsLength == 3 else None
    def __repr__(self):
        dest = " : " + str(self.DestRange) if self.DestRange is not None else ""
        return str(self.Range) + " " + str(self.Length) + dest
    # ( ": " + str(self.Adder) if self.Adder is not None else "")
    def hasOverlap(self, other):
        start = max(self.Range[0], other.Range[0])
        end = min(self.Range[-1], other.Range[-1])
        newRange = range(start, end+1)
        return len(newRange) > 0
    def updateRange(self, map):
        self.Start = (self.Start - map.Start) + (map.Adder)
        self.Length = map.Length
        self.Range = range(self.Start, self.Start+self.Length)
    def copy(self):
        newDetails = [self.Adder, self.Start, self.Length] if self.Adder is not None else [self.Start, self.Length]
        return MyRange(newDetails)

def toRange(start, length, mapper=None):
    return ( range(start, start+length), mapper)

def getMaps(mapDetails):
    name,ranges = mapDetails.split(":")
    ranges = helper.toList(ranges, "\n")
    return ranges

def getRanges(mapDetails):
    ranges = helper.toList(mapDetails.split(":")[1], "\n")
    rangeList = []
    for rangeDetails in ranges:
        destStart,sourceVal,rangeLength = map(lambda x: int(x), rangeDetails.split(" "))
        xx = ( range(sourceVal, (sourceVal+rangeLength)), destStart )
        rangeList.append(xx)
    return rangeList

def getSeedMappings(seed, maps):
    mappings = []
    prevVal = seed
    for ranges in maps:
        nextVal = prevVal
        for range in ranges:
            destVal,sourceVal,rangeLength = map(lambda x: int(x), range.split(" "))
            if prevVal >= sourceVal and prevVal < (sourceVal + rangeLength):
                nextVal = destVal + (prevVal - sourceVal)
        prevVal = nextVal
        mappings.append(nextVal)
    results = (seed, mappings)
    return results

def getSeedMappings2(seed, mapsList):
    mappings = []
    prevVal = seed
    for mapCategory in mapsList:
        nextVal = prevVal
        for map in mapCategory:
            if prevVal in map.Range:
                nextVal = map.Adder + (prevVal - map.Start)
        prevVal = nextVal
        mappings.append(nextVal)
    return (seed, mappings)

def processSeedRanges(seedRanges):
    lowestSeedRange = None
    lowestLocRange = None
    lowestLocStart = float('inf')
    for seedRange in seedRanges:
        seedCopy = seedRange.copy()
        print(seedCopy)
        for mapCategory in mapsList:
            print("\tNew category")
            print("\t  +Starting with: " + str(seedCopy))
            for map in mapCategory:
                print("\t\t" + str(map))
                if seedCopy.hasOverlap(map):
                    seedCopy.updateRange(map)
                    print("\t\t\tOverlapping range; Breaking")
                    print("\t\t\t" + str(seedCopy))
                    break
        if seedCopy.Start < lowestLocStart:
            lowestSeedRange = seedRange
            lowestLocRange = seedCopy
            lowestLocStart = seedCopy.Start
    print("Lowest Start: " + str(lowestSeedRange))
    print("Lowest Location: " + str(lowestLocRange))
    return lowestSeedRange

def processSeedPairs(seedRange):
    lowest = float('inf')
    lowestSeed = None
    highest = float('-inf')
    highestSeed = None
    for seedPair in seedRange:
        seed = seedPair[0]
        seedRange = seedPair[1]
        midRange = seedRange // 2

        while midRange >= 1:
            subMappings = [ getSeedMappings(x, maps) for x in [ seed, (seed+midRange), (seed+(seedRange-1))]]
            for subM in subMappings:
                loc = subM[1][-1]
                if loc < lowest:
                    lowest = loc
                    lowestSeed = subM
                if loc > highest:
                    highest = loc 
                    highestSeed = subM
            subSorted = sorted(subMappings, key=lambda x: (x[0], x[1][-1]), reverse=False)
            seed = subSorted[1][0]
            seedRange = subSorted[2][0] - seed
            midRange = seedRange // 2
    print("Lowest: " + str(lowestSeed))
    print("Highest: " + str(highestSeed))
    return lowest

def processSingleSeedRange(seedRange, mapsList):
    lowest = float('inf')
    lowestSeed = None
    highest = float('-inf')
    highestSeed = None

    seed = seedRange.Start
    seedRange = seedRange.Length
    midRange = seedRange // 2

    seedsToTry = deque()
    seedsToTry.append( [seed, seed+midRange, seed+seedRange])

    while len(seedsToTry) > 0:
        nextSeeds = seedsToTry.popleft()
        subMappings = [ getSeedMappings2(x, mapsList) for x in nextSeeds ]
        newLow = False
        for subM in subMappings:
            loc = subM[1][-1]
            if loc < lowest:
                lowest = loc
                lowestSeed = subM
            if loc > highest:
                highest = loc 
                highestSeed = subM
        subSorted = sorted(subMappings, key=lambda x: (x[0], x[1][-1]), reverse=False)
        # for x in subSorted:
        #     print(x)
        # print('')
        for ii in range(0,2):
            seed = subSorted[ii][0]
            seedRange = subSorted[ii+1][0] - seed
            midRange = seedRange // 2
            # print("Sub mid range: " + str(midRange))
            if(midRange > 0):
                seedsToTry.append( [seed, seed+midRange, seed+seedRange] )
    print("Lowest: " + str(lowestSeed))
    print("Highest: " + str(highestSeed))
    return lowest

'''
***************************************************************
    Run
***************************************************************
'''

seeds = [ int(x) for x in helper.toList(inputList[0].split(":")[-1]) ]
mapsList = []
for mapCategory in inputList[1:] :
    maps = [ MyRange(helper.toList(x)) for x in mapCategory.split("\n")[1:]  ]
    mapsList.append(maps)
mappings = [ getSeedMappings2(x, mapsList) for x in seeds ]
ans1 = min([ x[-1][-1] for x in mappings ])
helper.printAnswer(1,ans1)


seedRanges = []
for idx in range(0, len(seeds), 2):
    newRange = MyRange([seeds[idx], seeds[idx+1]])
    seedRanges.append(newRange)
lowestSeedRange = processSeedRanges(seedRanges)
ans2 = processSingleSeedRange(lowestSeedRange, mapsList)
# print(lowestSeedRange)
# mappings = [ getSeedMappings2(x, mapsList) for x in list(lowestSeedRang.Range) ]
# ans2 = min([ x[-1][-1] for x in mappings ])
helper.printAnswer(2, ans2)


# print(inputList[1:])
# ranges = [ getRanges(x) for x in inputList[1:]]
# print(ranges)

# seedRanges = []
# for idx in range(0, len(seeds), 2):
#     newRange = MyRange([seeds[idx], seeds[idx+1]])
#     seedRanges.append(newRange)

# lowestSeedPair = None
# lowestLocRange = None
# lowestLocStart = float('inf')
# for seedPair in seedRanges:
#     seedCopy = seedPair.copy()
#     print(seedCopy)
#     for mapCategory in mapsList:
#         print("\tNew category")
#         print("\t  +Starting with: " + str(seedCopy))
#         for map in mapCategory:
#             print("\t\t" + str(map))
#             if seedCopy.hasOverlap(map):
#                 seedCopy.updateRange(map)
#                 print("\t\t\tOverlapping range; Breaking")
#                 print("\t\t\t" + str(seedCopy))
#                 break
#     if seedCopy.Start < lowestLocStart:
#         print("New Low : {0} > {1} ".format(seedCopy.Start, lowestLocStart))
#         print("New Low : "+ str(seedCopy))
#         lowestSeedPair = seedPair
#         lowestLocRange = seedCopy.copy()
#         lowestLocStart = seedCopy.Start

# print("*"*100)
# print("LOWEST")
# print(lowestSeedPair)
# print(lowestLocRange)
# ans2 = float('inf')
# for seed in list(lowestSeedPair.Range):
#     seed,mappings = getSeedMappings2(seed, mapsList)
#     ans2 = mappings[-1] if mappings[-1] < ans2 else ans2
# print("*"*100)
# helper.printAnswer(2, ans2)

# for seed in list(range(55, 68)):
#     getSeedMappings2(seed, mapsList)    

    

# mapRanges = []
# for conversions in inputList[1:] :
#     rangeVals = [ helper.toList(x) for x in conversions.split("\n")[1:] ]
#     mapRanges.append( [ toRange(int(d[1]), int(d[2]), int(d[0])) for d in rangeVals] )
#     # ranges = helper.toList(conversions.split(":")[1], "\n")
#     # print(ranges)
#     # mapRanges += [ toRange( int(d[1]), int(d[2]), int(d[0])) for d in map(lambda x: int(x), ranges.split(" ")) ]    
#     # print(mapRanges)
# for x in mapRanges:
#     print(x)


# seedPairMap = {}
# for seedPair in seedRanges:
#     seedPair[seedPair] = None
#     for conv in mapRanges:
#         for ranges in conv:
            


# Print answer for Part 1
# seeds = [ int(x) for x in helper.toList(inputList[0].split(":")[-1]) ]
# maps = [ getMaps(x) for x in inputList if not x.startswith("seeds:") ]
# mappings = [ getSeedMappings(x, maps) for x in seeds ]
# ans1 = min([ x[-1][-1] for x in mappings ])
# helper.printAnswer(1,ans1)

# # Print answer for Part 2
# seedPairs = []
# for idx in range(0, len(seeds), 2):
#     seedPairs.append( (seeds[idx], seeds[idx+1]))
# ans2 = processSeedPairs(seedPairs)
# helper.printAnswer(2, ans2)

# print("")
# newLow = ans2
# for idx in range( (3720099308), (3720099308+50000)):
#     xx= getSeedMappings(idx, maps)
#     loc = xx[1][-1]
#     if loc < ans2:
#         ans2 = loc
# print(ans2)



# 1,500,156,659 == too high
# 17616610 = not right
# 8797878 = not right
# 187099598 = not right
# 187099597 = not right
# 160497922 = not right
# 82868913 = not right
# 11548427
# 183212530
# 3523821988
# 4917124 == ??
