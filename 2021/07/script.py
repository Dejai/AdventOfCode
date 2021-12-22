
# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = content.split(",")
inputNums = [ int(x) for x in inputList ]

# Set a baseline minimum cost and position
minCost = float("inf")
minPos = -1

# Get the smallest and largest number in set
maxNum = max(inputNums)
minNum = min(inputNums)

for i in range(minNum, maxNum+1):
    # Part 1
    #diffs = [ abs(i - x) for x in inputNums]
    #sumDiff = sum(diffs) 
    
    # For Part 2
    diffs = [ abs(i - x) for x in inputNums]
    rangeSum = [ sum(range(1,x+1)) for x in diffs]
    sumDiff = sum(rangeSum) # Part 2

    if(sumDiff < minCost):
        minCost = sumDiff
        minPos = i

print("Min Position = %d (cost = %d)" %(minPos, minCost))
