
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
class CardSorter: 
    def __init__(self):
        self.Cards = list('23456789TJQKA')
        self.Rankings = ["[1, 1, 1, 1, 1]", "[2, 1, 1, 1]", "[2, 2, 1]", "[3, 1, 1]", "[3, 2]", "[4, 1]", "[5]"]
        self.Joker = False

    # Set whether the Joker variant is in effect
    def setJoker(self):
        self.Joker = True
        self.Cards = list('J23456789TQKA')
    
    # Get the rank of a single hand (based on frequency rankings)
    def getHandRank(self, hand):
        freq = {}
        highestFreq = 0
        highestCardFreq = ""
        for card in list(hand):
            if card not in freq:
                freq[card] = 0
            freq[card] += 1
            # Only bother with highest frequency if doing the Joker variant
            if self.Joker and freq[card] > highestFreq and card != "J":
                highestFreq = freq[card]
                highestCardFreq = card

        # Convert Js to te best other option & then remove (for Joker variant)
        if self.Joker and "J" in freq and highestCardFreq != "":
            freq[highestCardFreq] += freq["J"]
            del freq["J"]

        freqVals = list(freq.values())
        freqVals.sort(reverse=True)
        freqKey = str(freqVals)
        idx = self.Rankings.index(freqKey)
        return idx

    def compareHands(self, pair1, pair2):
        hand1 = pair1[0]
        hand2 = pair2[0]
        hand1Rank = self.getHandRank(hand1)
        hand2Rank = self.getHandRank(hand2)
        if hand1Rank < hand2Rank:
            return -1
        elif hand1Rank > hand2Rank:
            return 1
        else:
            for idx in range(0, len(hand1)):
                h1_idx = self.Cards.index(hand1[idx])
                h2_idx = self.Cards.index(hand2[idx])
                if h1_idx < h2_idx:
                    return -1
                elif h1_idx > h2_idx:
                    return 1
            return 0
        
    def sortCards(self, pairs):
        pairsSorted = sorted(pairs, key=cmp_to_key(self.compareHands))
        return pairsSorted

'''
***************************************************************
    Run
***************************************************************
'''
pairs = [ (card,int(bid) ) for card,bid in [x.split(" ") for x in inputList ] ]
cardSorter = CardSorter()

# Print answer for Part 1
pairsSorted = cardSorter.sortCards(pairs)
winnings = [ (pair[1] * (idx+1) ) for idx,pair in enumerate(pairsSorted) ]
ans1 = sum(winnings)
helper.printAnswer(1,ans1)

# Print answer for Part 2
cardSorter.setJoker()
pairsSorted2 = cardSorter.sortCards(pairs)
winnings2 = [ (pair[1] * (idx+1) ) for idx,pair in enumerate(pairsSorted2) ]
ans2 = sum(winnings2)
helper.printAnswer(2, ans2)