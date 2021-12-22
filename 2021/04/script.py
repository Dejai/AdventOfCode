from helper import GameBoard

# Get the file input as a list of rows
inputFile = open("./input.txt", "r+")
content = inputFile.read()
inputFile.close()
inputList = [x for x in content.split("\n") if x != '']

# Split up the input into the two groups
numbersToCall = [int(x) for x in inputList[0].split(",")]
gameBoards = inputList[1:]

# Store all boards created in a dictionary based on name
ALL_BOARDS = dict()

# Loop through and create all the boards
row_idx = 0
board_idx = 0
for line in gameBoards:

    boardName = "Board #" + str(board_idx)

    # If board not created yet, make it
    if boardName not in ALL_BOARDS:
        board = GameBoard(boardName)
        ALL_BOARDS[boardName] = board

    # Get the current board being worked on
    theBoard = ALL_BOARDS[boardName]
    theBoard.addRow(line, row_idx)
    row_idx += 1

    # If we've reached the end of a board's row, start index over
    if( row_idx != 0 and row_idx % 5 == 0):
        board_idx += 1
        row_idx = 0

    
# Finally, check for BINGO based on numbers being callsed
isBingo = False
numbersCalled = []
winningBoards = []
for num in numbersToCall:
    numbersCalled.append(num)

    boardsWithNum = [ x for x in ALL_BOARDS.values() if x.hasNumber(num)]
    for board in boardsWithNum:
        isBingo = board.numberCalled(num)

        if(isBingo):
            score = board.calculateScore(numbersCalled,num)
            winningBoards.append( {"board": board.name, "score":score})
                

# Get the first and last winning boards
firstToWin = winningBoards[0]
lastToWin = winningBoards[-1]

print("First board to win == %s ; Score == %d " % (firstToWin["board"], firstToWin["score"]))
print("*"*50)

print("Last to win == %s ; Score == %d " % (lastToWin["board"], lastToWin["score"]))
print("*"*50)