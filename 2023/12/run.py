
from mypackage import helper
from collections import deque
import re

'''
***************************************************************
    Input
***************************************************************
'''
inputList = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functionsb & Classes
***************************************************************
'''
class Record:
    def __init__(self, input):
        springs,groups = input.split(" ")
        self.BasePattern = springs
        self.Groups = helper.toList(groups, splitChar=",", type="int")
        self.Regex = "\.+".join( [ "#{{{}}}".format(x) for x in self.Groups ]) + "\.*$"
        self.Variations = list(self.getVariations(self.BasePattern))
        self.VariationsCount = len(self.Variations)
        # For part 2:
        # self.BasePattern2 = "?" + self.BasePattern + "?"
        # self.Variations2 =list( self.getVariations(self.BasePattern2) )
        # self.Variations2Count = 1 if self.VariationsCount == 1 and self.Variations[0].endswith("#") else self.VariationsCount * pow(len(self.Variations2), 4)

    def __repr__(self):
        return "{} {}".format(self.BasePattern, str(self.Groups))

    def getVariations(self, basePattern):
        queue = deque([basePattern])
        patternSeen = set()
        variations = set()
        while queue:
            pattern = queue.popleft()
            patternSeen.add(pattern)
            if "?" in pattern:
                option1 = pattern.replace("?", ".", 1)
                option2 = pattern.replace("?", "#", 1)
                if option1 not in patternSeen:
                    queue.append(option1)
                if option2 not in patternSeen:
                    queue.append(option2)
            else:
                if re.search(self.Regex, pattern) is not None:
                    # Remove the matching part & see if there are any "#" leftover; if none, then this IS a full matching pattern
                    minusMatchingPart = re.sub(self.Regex, ".", pattern)
                    if "#" not in minusMatchingPart and minusMatchingPart != "":
                        variations.add(pattern)
        return variations

'''
***************************************************************
    Run
***************************************************************
'''
# Print answer for Part 1
print("Getting records ...")
records = [ Record(x) for x in inputList ]
ans1 = sum( [ record.VariationsCount for record in records ])
helper.printAnswer(1,ans1)

# Print answer for Part 2
# ans2 = sum([x.Variations2Count for x in records])
# helper.printAnswer(2, ans2)
# 3818526322969 -- Too high