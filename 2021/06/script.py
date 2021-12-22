
# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [ int(x) for x in content.split(",") if x != '']


# Structures to keep track of how many new fish are spawned;
spawnMap = {}
totalLanternFish = len(inputList) # initial length is the given input

# Spawns the new fish for the "2nd generation"; These ones will all spawn at the same time
def spawnLanternFish(currDay, targetDay, batchAmount):
    global spawnMap
    
    dayAfterDelay = currDay+2  # Account for 2-day delay
    diff = targetDay - dayAfterDelay  # Get number of days this batch could produce children

    if(diff > 0):
        for day  in range(dayAfterDelay, targetDay+1, 7) :
            # For each day that they can produce, update the batch amount on that day
            if(day != dayAfterDelay):

                if(day not in spawnMap):
                    spawnMap[day] = 0
                spawnMap[day] += batchAmount



targetDay = 256

state = inputList[:]
# start with "1st generation"; Filling out spawnMpa for next generation
for day in range(0, targetDay):

    numZeros = state.count(0)
    new_state = [ (6 if x == 0 else x-1) for x in state ]

    if(numZeros > 0):
        spawnMap[day+1] = numZeros
        
    state = new_state


# Loop through to process the "2nd generation"
while True:
    if (len(spawnMap) == 0):
        break
    
    keys = list(spawnMap.keys())
    keys.sort()
    day = keys[0]
    batchAmount = spawnMap.pop(day)
    totalLanternFish += batchAmount
    spawnLanternFish(day,targetDay,batchAmount)

print("\nTotal after %d days: %d\n" %(targetDay, totalLanternFish) )
