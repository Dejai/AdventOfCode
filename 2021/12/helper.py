
# Class to represent a cave
class Cave:

    def __init__(self, name):
        self.adjacentCaves = []
        self.name = name # name of the cave
        self.type = ""  # The type of cave (start, end, small, or large)
        self.paths = []

        self.visited = []
        self.priority = 1 if name == "end" else 2

        self.setType(name)

    # Setup the type of cave (based on casing of name or strat/end)
    def setType(self, name):
        if name in ["start", "end"]:
            self.type = name
        else:
            self.type = "small" if name == name.lower() else "big"

    # Add an adjacent cave
    def addAdjacentCave(self, cave):
        self.adjacentCaves.append(cave)

    # Return if it is a small cave
    def isSmall(self):
        return self.type == "small"




# Function to create a set of Caves
# Create the individual caves from the list - with their adjacent caves
def createCaves(inputList):
    theCaves = {}

    for line in inputList:
        splits = line.split("-")

        caveName1 = splits[0]
        caveName2 = splits[1]


        # Setup caves if not exists
        if caveName1 not in theCaves:
            theCaves[caveName1] = Cave(caveName1)

        if caveName2 not in theCaves:
            theCaves[caveName2] = Cave(caveName2)


        cave1 = theCaves[caveName1]
        cave2 = theCaves[caveName2]

        
        #print("%s -- %s" % (caveName1, caveName2))
        if( caveName2 == "end"):
            cave1.addAdjacentCave(cave2)
            # print("\tOne: %s -> %s" % (caveName1, caveName2))

        elif (caveName2 == "start"):
            cave2.addAdjacentCave(cave1)
            # print("\tTwo: %s -> %s" % (caveName2, caveName1))

        elif(caveName1 == "end"):
            cave2.addAdjacentCave(cave1)
            # print("\tThree: %s -> %s" % (caveName2, caveName1))

        elif (caveName1 == "start"):
            cave1.addAdjacentCave(cave2)
            # print("\tFour: %s -> %s" % (caveName1, caveName2))
            
        else:
            cave1.addAdjacentCave(cave2)
            # print("\tFive: %s -> %s" % (caveName1, caveName2))

            cave2.addAdjacentCave(cave1)
            # print("\tSix: %s -> %s" % (caveName2, caveName1))

    return theCaves



