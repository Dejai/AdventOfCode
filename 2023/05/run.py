
from mypackage import helper
from collections import deque

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt", "\n\n")

'''
***************************************************************
    Functions & Class
***************************************************************
''' 
# Class to keep track of 
class MyRange: 
    def __init__(self, start, end, converter=None):
        self.setRange( int(start), int(end))
        self.Converter = converter
        self.IsValid = self.End > self.Start
    def __repr__(self):
        return str(self.Range)
    def setRange(self, start, end):
        self.Start = start
        self.End = end
        self.Length = self.End - self.Start
        self.Range = range(self.Start, self.End)
# Get mapping for a single seed
def getMappingForSeed(seed, categoriesList):
    mappings = []
    prevVal = seed
    for category in categoriesList:
        nextVal = prevVal
        for map in category:
            if prevVal in map.Range:
                nextVal = prevVal if len(map.Range) == 1 else (prevVal - map.Start) + map.Converter
        prevVal = nextVal
        mappings.append(nextVal)
    return (seed, mappings)

# Get the set of category ranges
def getCategory(details):
    category = []
    for row in details:
        nums = [ int(x) for x in helper.toList(row) ]
        start = nums[1]
        end = start + nums[2]
        conv = nums[0]
        category.append(MyRange(start, end, conv))
    return category

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
seeds = [ int(x) for x in helper.toList(inputList[0].split(":")[-1]) ]
categories = [ getCategory( category.split("\n")[1:] ) for category in inputList[1:] ]
mappings = [ getMappingForSeed(seed, categories) for seed in seeds ]
ans1 = min([ x[-1][-1] for x in mappings ])
helper.printAnswer(1, ans1)

# Print answer for Part 2
seedRanges = [ MyRange(seeds[idx],  (seeds[idx] + seeds[idx+1]) ) for idx,val in enumerate(seeds) if idx %2 == 0 ]
ans2List = []
for seedRange in seedRanges:
    input = [ seedRange ]
    for category in categories:
        output = []
        for mapRange in category:
            notConverted = []
            while len(input) > 0:
                seed = input.pop()
                if seed.Start in mapRange.Range and seed.End-1 in mapRange.Range:
                    newStart = (seed.Start - mapRange.Start) + mapRange.Converter
                    newEnd = (newStart+seed.Length)
                    seed.setRange(newStart, newEnd)
                    output.append(seed)
                # Right side of seed range overlaps mapping range
                elif seed.Start not in mapRange.Range and seed.End-1 in mapRange.Range:
                    unmappedStart = seed.Start
                    unmappedEnd = mapRange.Start
                    notConverted.append(MyRange(unmappedStart, unmappedEnd))
                    newStart = max(mapRange.Start, seed.Start)
                    newStart = (newStart - mapRange.Start) + mapRange.Converter
                    newEnd = (seed.End - mapRange.Start) + mapRange.Converter
                    output.append(MyRange(newStart, newEnd))
                # Left side of seed range overlaps mapping range
                elif seed.Start in mapRange.Range and seed.End-1 not in mapRange.Range:
                    # The mapped side
                    newStart = seed.Start
                    newStart = (newStart - mapRange.Start) + mapRange.Converter
                    newEnd = min(seed.End, mapRange.End)
                    newEnd = (newEnd - mapRange.Start) + mapRange.Converter
                    output.append(MyRange(newStart, newEnd))
                    # The unmapped side
                    unmappedStart = mapRange.End
                    unmappedEnd = seed.End
                    notConverted.append(MyRange(unmappedStart, unmappedEnd))
                else:
                    notConverted.append(seed)
            input = notConverted
        input = output + notConverted
    ans2List += input
sortedAnswers = sorted(ans2List, key=lambda x: x.Start)
ans2 = sortedAnswers[0].Start
helper.printAnswer(2, ans2)