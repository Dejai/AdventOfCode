import math

class Tree:

    def __init__(self,height, coord):
        self.height = int(height)
        self.coord = coord
        self.neighbor = {
            "left":None,
            "above":None,
            "right":None,
            "below":None,
        }

    def __repr__(self):
        return "{0} ({1})".format(str(self.height),str(self.coord))
            
    def setNeighbor(self, direction, tree):
        self.neighbor[direction] = tree

    def visible(self):
        
        # If edge tree, yes it is visible
        if (None in self.neighbor.values() ):
            return True

        else:    
            for direction in ["left", "above", "right", "below"]:
                visible = self.visibleInDirection(self.height, direction)
                if(visible):
                    return True

        # Default answer is nope;
        return False

    # Check if this tree is visible in a certain direction
    def visibleInDirection(self, height, direction):
        visible = True

        neighbor = self.neighbor[direction]
        
        # No neighbor, then visible
        if neighbor is None:
            return True

        if height > neighbor.height:
            return neighbor.visibleInDirection(height, direction)
        # default visible is nope;
        return False

    # Get the scenic score for a tree
    def getScenicScore(self):
        scores = []
        for direction in ["left", "above", "right", "below"]:
            visible = self.visibleTreesByDirection(self.height, direction)
            scores.append(visible)
        return math.prod(scores)

    def visibleTreesByDirection(self,height, direction):
        n = self.neighbor
        neighbor = self.neighbor[direction]

        if neighbor is None:
            return 0
        
        if neighbor.height == height:
            return 1
        elif neighbor.height < height:
            return 1 + neighbor.visibleTreesByDirection(height, direction)
        
        return 1
