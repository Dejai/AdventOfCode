
from math import dist

# The state represents the state of the burrow 
class State:

    def __init__(self, hallway, rooms, prevState=None):

        # Keeping track of the halway
        self.hallway = hallway
        self.rooms = rooms
        self.cost = 0

        # Set the previous state
        self.prevState = prevState


    # String representation of Amphipod; r=room; s=slot; h=hallway
    def __repr__(self) -> str:
        return repr( self.getStateIdentifier() )


    #---------------------------------------------------------------------------------
    #   General Setters and Getters
    #---------------------------------------------------------------------------------

    # Mapping of room to column
    def getColumnNumber(self, room):
        roomToCol = {1:2, 2:4, 3:6, 4:8}
        if room in roomToCol:
            return roomToCol[room]
        else:
            return None

    # Mapping of room number based on column
    def getRoomNumber(self, column):
        columnToRoom = {2:1, 4:2, 6:3, 8:4}
        if column in columnToRoom:
            return columnToRoom[column]
        else:
            return None

    # Get the target column based on a given pod
    def getTargetColumn(self,pod):
        targets = {"A":2, "B":4, "C":6, "D":8}
        return targets[pod]

    # Get the energy costs for a pod
    def getEnergyCost(self, pod):
        costs = {"A":1, "B":10, "C":100, "D":1000}
        return costs[pod]


    # A state identifier so we don't go down a state again
    def getStateIdentifier(self):
        hallway = self.hallway
        hallwayVals = "".join( [ str(hallway[x]) if hallway[x] is not None else '.' for x in hallway] )
        room1Vals = "".join( [x if x is not None else '.' for x in self.rooms[1]] )
        room2Vals = "".join( [x if x is not None else '.' for x in self.rooms[2]] )
        room3Vals = "".join( [x if x is not None else '.' for x in self.rooms[3]] )
        room4Vals = "".join( [x if x is not None else '.' for x in self.rooms[4]] )

        formatted = format("State: %s | r1:%s | r2:%s | r3:%s | r4:%s" % (hallwayVals, room1Vals, room2Vals, room3Vals, room4Vals))
        return formatted


    #---------------------------------------------------------------------------------
    #   Key Actions
    #---------------------------------------------------------------------------------

    # Get all the moves that could be made from this state
    def getMovesFromState(self):

        allMoves = []

        hallway = self.hallway
        rooms = self.rooms

        # Get moves from hallways to rooms first (if any)
        for col in hallway:
            pod = hallway[col]
            if type(pod) == str:
                allMoves += self.getAvailableMoves(pod,col)


        # Then get moves from room to hallway
        for room in rooms:
            roomSet = rooms[room]

            for idx in range(0,len(roomSet)):
                pod = roomSet[idx]

                if self.canLeaveRoom(pod,room,idx):
                    column = self.getColumnNumber(room)
                    allMoves += self.getAvailableMoves(pod,column,idx)

        # Sort the moves based on a certain combo of priority
        #srted = sorted(allMoves, key = lambda x: (x['moveType'],x['target'], x['cost'], x['distanceFromTarget']), reverse=True )
        # srted = sorted(allMoves, key = lambda x: (x['moveType'], x['cost'] ), reverse=True )
        srted = sorted(allMoves, key = lambda x: (x['cost'] ), reverse=True)

        # print("\n\tMOVES FROM THIS STATE:")
        # for x in srted:
        #     print("\t%s" % str(x))
        # print("\n" + ("~~")*50)

        return srted


    # Get current available moves from given pod; NOTE the position will either be hallway column or room number; Slot is only used for rooms 'moveType' is (0=room; 1=hallway)
    def getAvailableMoves(self,pod,column,slot=None):
        
        availableMoves = []

        targetColumn = self.getTargetColumn(pod)

        # Check if this node can enter
        canEnter,roomIdx = self.canEnterRoom(pod)

        if canEnter and roomIdx is not None and self.isHallwayClear(column,targetColumn):

            moveObject = {"pod":pod, "moveType": 0, "colStart":column, "colEnd":targetColumn, "roomIdx":roomIdx,  "target":targetColumn, "distanceFromTarget":None, "cost":0 }

            moveObject["distanceFromTarget"] = 0
            moveObject["cost"] = self.calculateCost(pod,column,targetColumn,slot,roomIdx)
            availableMoves.append(moveObject)


        else:

            if slot is not None:
                # Get all the available moves to the hallway from this location
                for spot in self.hallway:
                    
                    moveObject = {"pod":pod, "moveType": 1, "colStart":column, "colEnd":spot, "roomIdx":slot, "target":targetColumn,  "distanceFromTarget":None, "cost":0 }

                    occupant = self.hallway[spot]
                    if occupant is None and self.isHallwayClear(column,spot):
                        moveObject["distanceFromTarget"] = abs(targetColumn - spot)
                        moveObject["cost"] = self.calculateCost(pod, column, spot, slot)
                        availableMoves.append(moveObject)

        return availableMoves
    

    # Calculate cost of move
    def calculateCost(self, pod, start, end, startingSlot, endingSlot=None):

        startSlot = 0 if startingSlot is None else startingSlot+1
        endSlot = 0 if endingSlot is None else endingSlot+1
    
        steps = abs(start-end) + startSlot + endSlot
        cost = steps * self.getEnergyCost(pod)

        # if pod == "B" and start == 6 and end == 3:
        #     print("Start Col = %d" % start)
        #     print("End Col = %d" % end)
        #     print("Start Slot (orig) = %d" % startingSlot)
        #     print("Start Slot = %d" % startSlot)
        #     print("End Slot = %d" % endSlot)
        #     print("Steps = %d" % steps)

        return cost


    # Make a single move
    def makeMove(self, move):

        # Create the new state first; Use copies of the current state's values
        # The action will be taken on the new state
        hallwayCopy = self.hallway.copy()
        roomsCopy = {}
        for x in self.rooms:
            roomsCopy[x] = self.rooms[x][:]

        newState = None

        newState = State(hallwayCopy,roomsCopy, self)

        # Get the details from the move
        pod = move['pod']
        moveType = move['moveType']
        colStart = move['colStart']
        colEnd = move['colEnd']
        roomIdx = move['roomIdx']
        cost = move['cost']

        # Update the new state
        newState.cost = cost + self.cost

        # Type 1 == Move to hallway
        if moveType == 1:

            startingRoom = newState.rooms[ newState.getRoomNumber(colStart) ]

            # Move the pod to the hallway position
            newState.hallway[colEnd] = pod

            # Clear room location
            self.clearPodFromRoom(pod,startingRoom)

        # Type 0 = Move to Room
        elif moveType == 0:

            targetRoom = newState.rooms[ newState.getRoomNumber(colEnd) ]

            # If coming from another room, make the top-most element a None
            if newState.getRoomNumber(colStart) is not None:

                startRoom = newState.rooms[ newState.getRoomNumber(colStart) ]
                self.clearPodFromRoom(pod, startRoom)

            else:
                # Clear the hallway
                newState.hallway[colStart] = None

            # Update the room
            targetRoom[roomIdx] = pod

        
        return newState


    #---------------------------------------------------------------------------------
    #   Helper methods
    #---------------------------------------------------------------------------------

    # Clear pod from room
    def clearPodFromRoom(self,pod,room):

        for x in range(0,len(room)):
            if room[x] == pod:
                room[x] = None
                break


    # Can the pod leave its room?
    def canLeaveRoom(self, pod, room, slot):
        canLeave = False

        if pod is None:
            return canLeave

        else:

            # Check if it can move straight to room
            currRoom = self.rooms[room]

            podsAbove = [ x for x in currRoom[0:slot] if x is not None ]  # Check if the above
            podsBelow = [x for x in currRoom[slot:] if x is not None and x != pod ] # Check if any pods below this one of a different type            

            inTargetRoom = self.getTargetColumn(pod) == self.getColumnNumber(room)

            if len(podsAbove) == 0 and len(podsBelow) >= 0 and not inTargetRoom :
                canLeave = True
            elif inTargetRoom and len(podsBelow) > 0:
                canLeave = True    

        return canLeave

    # Check if a pod can enter a room
    def canEnterRoom(self, pod):
        
        canEnter = False
        roomIdx = None

        targetColumn = self.getTargetColumn(pod)
        targetRoom = self.rooms[ self.getRoomNumber(targetColumn) ]

        for slotIdx in range(len(targetRoom)-1, -1, -1):
            element = targetRoom[slotIdx]

            if type(element) == str and element != pod:
                break
            elif element is None:
                canEnter = True
                roomIdx = slotIdx
                break


        return (canEnter,roomIdx)

    
    # Printout the details of this state
    def printState(self):

        print("\nSTATE: (cost=%d)" % self.cost)
        print("-"*25)
        # Each row to be printed out
        hallIdxRow = [" "]
        topRow = ["#"]
        hallRow = ["#"]
        roomRows = []
        bottomRow = [""]

        totalElements = len(self.rooms[1])
        for i in range(0, totalElements):
            initVal = "#" if i == 0 else " "
            slotRow = [initVal]
            roomRows.append(slotRow)

        wallSep = "#"
        spaceSep = " "
        hallSep = "."
        # Print out the state
        for col in self.hallway:

            # Update the Hall Index
            hallIdxRow.append(str(col))

            # Update the top
            topRow.append(wallSep)

            # Update the hall value
            val = self.hallway[col]
            sep = hallSep if val is None or type(val) == int else val
            hallRow.append(str(sep))

            # Update the rooms
            if type(val) == int:
                room = self.rooms[val]
                for idx in range(0, totalElements):
                    element = room[idx]
                    val = "." if element is None else element
                    roomRows[idx].append(str(val))
            else:
                defaultValue1 = "#"
                defaultValue2 = " " if col < 1 or col > 9 else "#"
                for x in range(0, totalElements):
                    v = defaultValue1 if x == 0 else defaultValue2
                    roomRows[x].append(v)

        # Close the map for some rows
        hallIdxRow.append(" ")
        topRow.append("#")
        hallRow.append("#")
        roomRows[0].append("#")

        print(spaceSep.join(hallIdxRow))
        print(spaceSep.join(topRow))
        print(spaceSep.join(hallRow))
        for row in roomRows:
            print(spaceSep.join(row))

        # Set the bottom row
        bottomRow = []
        for x in roomRows[-1]:
            val = "#" if x in ["#","A", "B", "C", "D", "."] else " "
            bottomRow.append(val)
        print(spaceSep.join(bottomRow))        

        print("\n\n")

    
    # Check if the hallway path is clear for a pod to move
    def isHallwayClear(self, start, target):
     
        direction = -1 if start > target else 1
        startIdx = start+1 if direction > 0 else start-1
        targetIdx = target+1 if direction > 0 else target-1

        isClear = True
        for idx in range(startIdx, targetIdx, direction):

            inHall = self.hallway[idx]

            if type(inHall) == str:
                isClear = False
                break

        return isClear
    

    # Print current state and all previous states -- to see history of moves
    def printStateHistory(self):
        
        # Print the state
        self.printState()
        
        if self.prevState is not None:
            self.prevState.printStateHistory()

    
    # Print current state and all previous states -- to see history of moves
    def getStateHistory(self, prevStates=[]):
                
        if self.getStateIdentifier() == "State: .B1.2.3B4.. | r1:.A | r2:.D | r3:CC | r4:DA":
            self.printState()
        
        if self.prevState is None:
            return prevStates
        else:
            prevStates.append(self.getStateIdentifier())
            return self.prevState.getStateHistory(prevStates)