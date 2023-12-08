
from mypackage import helper

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions
***************************************************************
'''
def productOfList(numList):
    results = 1
    for num in numList:
        results *= num
    return results

def compareToRecord(hold, raceTime, dist):
    userTime = raceTime - hold
    travelDist = (hold * userTime)
    return hold if travelDist > dist else None

def processWaysToWin(time,dist):
    wins = []
    raceRange = range(0, time+1)
    lowest = None
    highest = None
    idx = 0
    while lowest is None or highest is None:
        lowest = compareToRecord(raceRange[idx], time, dist) if lowest is None else lowest
        highest = compareToRecord(raceRange[time-idx], time, dist) if highest is None else highest
        idx += 1
    wins.append( len(range(lowest,highest+1)) )
    return wins

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
times = [ int(x) for x in helper.toList(inputList[0].split(": ")[1]) ]
dists = [ int(x) for x in helper.toList(inputList[1].split(": ")[1]) ]
timeRecords = zip(times, dists)
waysToWin = []
for time,dist in timeRecords:
    waysToWin += processWaysToWin(time,dist)
ans1 = productOfList(waysToWin)
helper.printAnswer(1,ans1)

# Print answer for Part 2
time = int(inputList[0].split(": ")[1].replace(" ", ""))
dist = int(inputList[1].split(": ")[1].replace(" ", ""))
ans2 = productOfList( processWaysToWin(time, dist) )
helper.printAnswer(2, ans2)