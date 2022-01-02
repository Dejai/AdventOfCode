from os import stat
import shared
from helper import State
from collections import deque


'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./example2.txt")
goalList = shared.getFileContentAsList("./goal2.txt")

DEBUG = False

'''
***************************************************************
    Functions
***************************************************************
'''

# Create the pods and initialize th emap
def createBurrowMap(inputList):
    # Create the pods
    hallway = {}
    rooms = {}

    # Parse through the input
    for line in inputList:

        podLetters = ["A", "B", "C", "D"]

        if "." in line:
            col = 0
            for c in line:
                if c != '#':
                    hallway[col] = None
                    col += 1

        elif any( char in line for char in podLetters):
            col = -1
            room = 1
            for c in line:
                if c != '#' and c != ' ':
                    
                    if col in hallway:
                        hallway[col] = room

                    if room not in rooms:
                        rooms[room] = []

                    rooms[room].append(c)
                    room += 1
                col += 1                 
        
    return (hallway, rooms)
    

# Depths first search of states
def searchStates(initialState, goalState, maxIterations=500000):

    # Hopefully the states that contain our goal states
    goalStates = []  # Stores the different states that arrived at the goal (along with cost)
    visited = {}
    deadends = [] # Storing the deadends so I can see them later (for troubleshooting)
    theQueue = deque()    # Setup queue, with root node first
    
    # STEP 1: Append the initial state to the list
    theQueue.append(initialState)

    # STEP 2: Store the ID for the goal state; Makes it easy to compare if a reached state is legit
    initialStateId = initialState.getStateIdentifier()
    goalStateId = goalState.getStateIdentifier()

    # Store the best cost discovered so far; If a state has a higher cost than that, then don't bother check along that state
    bestCost = None
    
    # Use DFS to get the left/right digits based on left-side priority of nodes
    iterationCounter = 1
    while theQueue:

        iterationCounter += 1
        # Arbitrary max to stop checking; Just to see if a discovered goal suffices yet
        if iterationCounter > maxIterations:
            break

        # Pop the first state; Get its ID and moves
        state = theQueue.pop()
        stateId = state.getStateIdentifier()
        moves = state.getMovesFromState()

 
        if iterationCounter % 1000000 == 0:
            print("SILL GOING .... Iteration: " + str(iterationCounter))

        # If we found a goal already, and this state is more than that, don't keep going
        if bestCost is not None and state.cost >= bestCost:
            continue

        # Check if state is a goal state:
        elif stateId == goalStateId:
            print("\nIteration: %d\nGOAL STATE: %s at cost = %d\n" % (iterationCounter, str(state), state.cost) )
            goalStates.append( (state.cost, state) )

            if bestCost is None or state.cost < bestCost:
                bestCost = state.cost
            continue

        elif len(moves) == 0:
            deadends.append(stateId)
            continue
        else:
            
            # Add a state as visited
            visited[stateId] = state.cost

            for move in moves:

                # Run the new state
                newState = state.makeMove(move)

                # If we have already made a move from a state, don't do it again
                if (newState.getStateIdentifier() in visited) and (newState.cost > visited[stateId]+1000):
                    continue
                    # print("Cost comparison: %d vs %d" % (newState.cost, visited[stateId]))
                    # continue

                # If that new state is already a deadend, don't bother adding it.
                if newState.getStateIdentifier() in deadends:
                    continue

                theQueue.append(newState)


    # for st in stateFreq:
    #     print("%s == %d" % (st, stateFreq[st]))


    if DEBUG:
        srted = sorted(goalStates, key = lambda x: x[0])
        minimum = srted[0][1]
        print("\n\nTHE MINIMUM EFFORT MOVEMENTS:\n")
        print("-"*90)
        minimum.printStateHistory()


# Test a series of moves
def testMoves(initialState):

    moves = [ 
        {'pod': 'B', 'moveType': 1, 'colStart': 6, 'colEnd': 3, 'roomIdx': 0, 'target': 4, 'distanceFromTarget': 1, 'cost': 40},
        {'pod': 'C', 'moveType': 0, 'colStart': 4, 'colEnd': 6, 'roomIdx': 0, 'target': 6, 'distanceFromTarget': 0, 'cost': 400},
        {'pod': 'D', 'moveType': 1, 'colStart': 4, 'colEnd': 5, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 4, 'cost': 3000},
        {'pod': 'B', 'moveType': 0, 'colStart': 3, 'colEnd': 4, 'roomIdx': 1, 'target': 4, 'distanceFromTarget': 0, 'cost': 30},
        {'pod': 'B', 'moveType': 0, 'colStart': 2, 'colEnd': 4, 'roomIdx': 0, 'target': 4, 'distanceFromTarget': 0, 'cost': 40},
        {'pod': 'D', 'moveType': 1, 'colStart': 8, 'colEnd': 7, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 1, 'cost': 2000},
        {'pod': 'A', 'moveType': 1, 'colStart': 8, 'colEnd': 9, 'roomIdx': 0, 'target': 2, 'distanceFromTarget': 7, 'cost': 3},
        {'pod': 'D', 'moveType': 0, 'colStart': 7, 'colEnd': 8, 'roomIdx': 1, 'target': 8, 'distanceFromTarget': 0, 'cost': 3000},
        {'pod': 'D', 'moveType': 0, 'colStart': 5, 'colEnd': 8, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 0, 'cost': 4000},
        {'pod': 'A', 'moveType': 0, 'colStart': 9, 'colEnd': 2, 'roomIdx': 0, 'target': 2, 'distanceFromTarget': 0, 'cost': 8}
    ]

    theState = initialState
    print("START:")
    initialState.printState()
    initialState.getMovesFromState()

    print('-'*25)
    print('\n')

    c = 1
    for move in moves[:1]:

        print("%d) Making move: %s" % (c,str(move)) )
        c+=1
        newState = theState.makeMove(move)
        newState.printState()
        newState.getMovesFromState()
        theState = newState

        if theState.isGoal():
            print("GOAL!")


'''
***************************************************************
    Run

    THE COMBO THAT WORKED:
    Pods:
        0 == (A at r2.)
        1 == (D at r1.s1)
        2 == (B at r1.)
        3 == (D at r2.)
        4 == (B at r2.s2)
        5 == (C at r1.s2)
        6 == (A at r1.)
        7 == (C at r2.s2)

    ['2 h 3', '6 h 10', '3 h 9', '7 r 2', '1 r 2', '5 r 1', '3 r 1', '2 r 2', '0 h 1', '4 r 1', '6 r 2', '0 r 1', 'done']
    Cost = 12,240

    {'pod': 'B', 'moveType': 1, 'colStart': 6, 'colEnd': 3, 'roomIdx': 0, 'target': 4, 'distanceFromTarget': 1, 'cost': 40}
    {'pod': 'C', 'moveType': 0, 'colStart': 4, 'colEnd': 6, 'roomIdx': 0, 'target': 6, 'distanceFromTarget': 0, 'cost': 400}
    {'pod': 'D', 'moveType': 1, 'colStart': 4, 'colEnd': 5, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 4, 'cost': 3000}
    {'pod': 'B', 'moveType': 0, 'colStart': 3, 'colEnd': 4, 'roomIdx': 1, 'target': 4, 'distanceFromTarget': 0, 'cost': 30}
    {'pod': 'B', 'moveType': 0, 'colStart': 2, 'colEnd': 4, 'roomIdx': 0, 'target': 4, 'distanceFromTarget': 0, 'cost': 40}
    {'pod': 'D', 'moveType': 1, 'colStart': 8, 'colEnd': 7, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 1, 'cost': 2000}
    {'pod': 'A', 'moveType': 1, 'colStart': 8, 'colEnd': 9, 'roomIdx': 0, 'target': 2, 'distanceFromTarget': 7, 'cost': 3}
    {'pod': 'D', 'moveType': 0, 'colStart': 7, 'colEnd': 8, 'roomIdx': 1, 'target': 8, 'distanceFromTarget': 0, 'cost': 3000}
    {'pod': 'D', 'moveType': 0, 'colStart': 5, 'colEnd': 8, 'roomIdx': 0, 'target': 8, 'distanceFromTarget': 0, 'cost': 4000}
    {'pod': 'A', 'moveType': 0, 'colStart': 9, 'colEnd': 2, 'roomIdx': 0, 'target': 2, 'distanceFromTarget': 0, 'cost': 8}


    NOTES:
        4 types of amphipods:
            (A) Amber
            (B) Bronze
            (C) Copper
            (D) Desert
        
        1 hallway
        4 side rooms

        side rooms initially = FULL
        hallway initially = EMPTY


        target:  
            Organize the amphipods into side rooms
            Each side room contains one type
            Types are sorted A-D (left to right)

            Find a way to organize using LEAST TOTAL ENERGY

        MOVEMENT:
            Up, down, left, right
            Must move into UNOCCUPIED space

            Each type requires different amount of energy to move ONE step

                (A) = 1 per step
                (B) = 10 per step
                (C) = 100 per step
                (D) = 1000 per step
        
        EXTRA RULES
            > They NEVER stop on the open space immediately outside any room
                .. so they can move through it, but never stop in it
            > They will NEVER move from hallway into a room unless:
                ... It is empty
                ... OR it has other amphipods of the same type
            > Once amphiods stop moving in the hallway, it will STAY until it can move into a room
                ... So they go from hallway directly into room (but with restriction in rule #2)

***************************************************************
'''

# Get burrow state
# burrowMap = createBurrowMap(inputList)
hallway,rooms = createBurrowMap(inputList)
hallway2,rooms2 = createBurrowMap(goalList)
initialState = State(hallway,rooms)
goalState = State(hallway2,rooms2)

# initialState.printState()
# print(initialState.getStateIdentifier())
# goalState.printState()
# print(goalState.getStateIdentifier())

searchStates(initialState,goalState)


#testMoves(initialState,moves)


