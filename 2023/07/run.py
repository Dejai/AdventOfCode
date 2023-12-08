
from mypackage import helper
from functools import cmp_to_key

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
def getHandRank(hand):
    rankings = ["[1, 1, 1, 1, 1]", "[2, 1, 1, 1]", "[2, 2, 1]", "[3, 1, 1]", "[3, 2]", "[4, 1]", "[5]"]
    freq = {}
    for card in list(hand):
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1
    freqVals = list(freq.values())
    freqVals.sort(reverse=True)
    freqKey = str(freqVals)
    idx = rankings.index(freqKey)
    return idx

def compareHands(pair1, pair2):
    hand1 = pair1[0]
    hand2 = pair2[0]

    hand1Rank = getHandRank(hand1)
    hand2Rank = getHandRank(hand2)
    if hand1Rank < hand2Rank:
        return -1
    elif hand1Rank > hand2Rank:
        return 1
    else:
        cards = list('23456789TJQKA')
        for idx in range(0, len(hand1)):
            h1_idx = cards.index(hand1[idx])
            h2_idx = cards.index(hand2[idx])
            if h1_idx < h2_idx:
                return -1
            elif h1_idx > h2_idx:
                return 1
        return 0
    
def getHandRankJoker(hand):
    rankings = ["[1, 1, 1, 1, 1]", "[2, 1, 1, 1]", "[2, 2, 1]", "[3, 1, 1]", "[3, 2]", "[4, 1]", "[5]"]
    freq = {}
    highestFreq = 0;
    highestCardFreq = ""
    for card in list(hand):
        if card not in freq:
            freq[card] = 0
        freq[card] += 1
        if freq[card] > highestFreq and card != "J":
            highestFreq = freq[card]
            highestCardFreq = card

    # Convert Js to te best other option & then remove
    if "J" in freq and highestCardFreq != "":
        freq[highestCardFreq] += freq["J"]
        del freq["J"]

    freqVals = list(freq.values())
    freqVals.sort(reverse=True)
    freqKey = str(freqVals)
    idx = rankings.index(freqKey)
    return idx

def compareHandsJoker(pair1, pair2):
    hand1 = pair1[0]
    hand2 = pair2[0]

    hand1Rank = getHandRankJoker(hand1)
    hand2Rank = getHandRankJoker(hand2)
    if hand1Rank < hand2Rank:
        return -1
    elif hand1Rank > hand2Rank:
        return 1
    else:
        cards = list('J23456789TQKA')
        for idx in range(0, len(hand1)):
            h1_idx = cards.index(hand1[idx])
            h2_idx = cards.index(hand2[idx])
            if h1_idx < h2_idx:
                return -1
            elif h1_idx > h2_idx:
                return 1
        return 0

'''
***************************************************************
    Run
***************************************************************
'''

# Print answer for Part 1
pairs = [ (card,int(bid) ) for card,bid in [x.split(" ") for x in inputList ] ]
pairsSorted = sorted(pairs, key=cmp_to_key(compareHands))
winnings = [ (pair[1] * (idx+1) ) for idx,pair in enumerate(pairsSorted) ]
ans1 = sum(winnings)
helper.printAnswer(1,ans1)

# Print answer for Part 2
pairsSorted2 = sorted(pairs, key=cmp_to_key(compareHandsJoker))
winnings2 = [ (pair[1] * (idx+1) ) for idx,pair in enumerate(pairsSorted2) ]
ans2 = sum(winnings2)
helper.printAnswer(2, ans2)