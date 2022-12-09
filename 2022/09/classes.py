class Knot:

    def __init__(self, name, leader=None):
        self.name = name
        self.row = 0
        self.col = 0

        # The knot that this knot should "follow"
        self.leader = leader

        # Unique locations of this knot
        self.unique = set()
        
        # Set locations where knot has been
        self.visitedLocations = []

        # Set initial location
        self.setVisitedLocation(0,0)

    
    def __repr__(self):
        return "Knot: {0} (unique: {1}) ".format(self.name, str(len(self.unique)))

    def moveKnot(self,row,col):
        self.row += row
        self.col += col
        self.setVisitedLocation(row,col)

    def setKnotLocation(self, row,col):
        self.row = row
        self.col = col
        self.setVisitedLocation(row,col)

    def setVisitedLocation(self,row,col):
        self.visitedLocations.append( (row,col) )
        self.unique.add("{0}-{1}".format(self.row, self.col))


    def followLeader(self):
        # print("Checking Knot") 

        if self.name == "head":
            return
        
        # Move this knot if the leader knot is too far
        leaderRow = self.leader.row
        leaderCol = self.leader.col
        thisRow = self.row
        thisCol = self.col

        # # First set the visited locations of this knot to be the last 2 visited by the leader knot
        # for visited in self.leader.visitedLocations[-2:-1]:
        #     self.setVisitedLocation(visited[0], visited[1])
            
        # If two rows above - move to one row below, same col
        if leaderRow > thisRow+1:
            # print("\tMoving tail based on head row (above)")
            # self.setKnotLocation(thisRow+1, leaderCol)

            if leaderCol > thisCol:
                # Move diagonal left UP
                self.setKnotLocation(thisRow+1,thisCol+1)
            elif leaderCol < thisCol:
                # Move diagonal left DOWN
                self.setKnotLocation(thisRow+1,thisCol-1)
            else:
                # Move left
                self.setKnotLocation(thisRow+1, thisCol)


        # If two columns to the right - move to one col behind, same row
        elif leaderCol > thisCol+1:
            # print("\tMoving tail based on head col (right)")
            # self.setKnotLocation(leaderRow, leaderCol-1)

            if leaderRow > thisRow:
                # Move diagonal left UP
                self.setKnotLocation(thisRow+1,thisCol+1)
            elif leaderRow < thisRow:
                # Move diagonal left DOWN
                self.setKnotLocation(thisRow-1,thisCol+1)
            else:
                # Move left
                self.setKnotLocation(thisRow, thisCol+1)
        
        # If two rows below - move to one row above, same col
        elif leaderRow < thisRow-1:
            # print("\tMoving tail based on head row (below)")
            # self.setKnotLocation(leaderRow+1, leaderCol)

            if leaderCol > thisCol:
                # Move diagonal left UP
                self.setKnotLocation(thisRow-1,thisCol+1)
            elif leaderCol < thisCol:
                # Move diagonal left DOWN
                self.setKnotLocation(thisRow-1,thisCol-1)
            else:
                # Move left
                self.setKnotLocation(thisRow-1, thisCol)
            
        
        # If two columns left - move to one col right, same row
        elif leaderCol < thisCol-1:
            # print("\tMoving tail based on head col (left)")
            # self.setKnotLocation(leaderRow, leaderCol+1)
            if leaderRow > thisRow:
                # Move diagonal left UP
                self.setKnotLocation(thisRow+1,thisCol-1)
            elif leaderRow < thisRow:
                # Move diagonal left DOWN
                self.setKnotLocation(thisRow-1,thisCol-1)
            else:
                # Move left
                self.setKnotLocation(thisRow, thisCol-1)