
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
def getCardDetails(inputList):
    cardDetails = []
    for card in inputList:
        points = 0
        matches = 0
        cardName,numbers = card.split(": ")
        winNums,myNums = numbers.split("|")
        winNums = [ x.strip() for x in winNums.split(" ") if x != "" ]
        myNums = [ x.strip() for x in myNums.split(" ") if x != ""]
        for num in myNums:
            if num in winNums:
                matches += 1
                if points == 0:
                    points = 1
                else:
                    points *= 2
        cardDetails.append(  { "Name": cardName, "Points": points, "Matches": matches, "Instances": 1 } )
    return cardDetails

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
cardDetails = getCardDetails(inputList)
points = [ card["Points"] for card in cardDetails ]
ans1 = sum(points)
helper.printAnswer(1,ans1)

# Print answer for Part 2
for idx in range(0, len(cardDetails)):
    currCard = cardDetails[idx]
    matches = currCard["Matches"]
    instances = currCard["Instances"]
    for copyIdx in range(0, instances):
        for subIdx in range(idx+1, (idx+matches)+1):
            nextCard = cardDetails[subIdx]
            nextCard["Instances"] += 1
instances = [ card["Instances"] for card in cardDetails]
ans2 = sum(instances)
helper.printAnswer(2, ans2)