
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [ x for x in content.split("\n") if x != '' ]


chunkSyntaxMap = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

openChars = "([{<"
closeChars = ")]}>"

illegalCharPoints = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}



# Get the set of syntax errors and completions for each line
def getLineDetails(lines):

    errorTracker = []
    completions = []

    for line in inputList:
        
        queue = []
        error = False

        for char in line:
            
            if error:
                break

            if char in openChars:
                pair = (char, chunkSyntaxMap[char])
                queue.append(pair)

            elif char in closeChars:
                #while True:
                lastChar,expectedChar = queue.pop()
                if(char != expectedChar):
                    error = True
                    errorTracker.append(char)

        if not error:
            queue.reverse()
            completionChars = [ close for open,close in queue ]
            completionLine = "".join(completionChars)
            completions.append(completionLine)

    return errorTracker, completions


# Get autocomplete score
def getAutoCompleteScore(line):

    scoreMap = { ")": 1, "]": 2, "}": 3, ">": 4 }
    score = 0
    for char in line:
        score *= 5
        score += scoreMap[char]

    return score

# Part 1
errors,completions = getLineDetails(inputList)
print("\nFound %d errors. :(" % (len(errors)))

errorPoints = [ illegalCharPoints[x] for x in errors]
print("Syntax Error Score = %d" % (sum(errorPoints)))


# Part 2
scores = []
for line in completions:

    score = getAutoCompleteScore(line)
    scores.append(score)

scores.sort()
middle = len(scores) // 2
print("\nMiddle score = %d" % (scores[middle]))