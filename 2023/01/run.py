
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
def getNumber(val):
    numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = None
    try:
        # Check if any numbers are in word
        numsInWord = [x for x in numberWords if x in val]
        if( len(numsInWord) > 0):
            number = numberWords.index(numsInWord[-1])+1
        else:
            number = int(val)
    except Exception as err:
        number = None
    return number

def getCalibrationVal(line, useWordNum=False):
    numbers = []
    word = ""
    for char in line:
        word += char
        charNum = getNumber(char)
        wordNum = getNumber(word)
        if charNum is not None:
            numbers.append(charNum)
        elif useWordNum and wordNum is not None:
            word = char
            numbers.append(wordNum)
    answer = 0
    if(len(numbers) > 0):
        first = str(numbers[0])
        last = str(numbers[-1])
        answer = int(first + last)            
    return answer

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
numbers = [ getCalibrationVal(x) for x in inputList ]
total = sum(numbers)
helper.printAnswer(1,total)

# Print answer for Part 2
numbers = [ getCalibrationVal(x, True) for x in inputList ]
total = sum(numbers)
helper.printAnswer(2, total)