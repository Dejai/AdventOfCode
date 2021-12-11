
# Class to represent a single game board
class GameBoard:

    def __init__(self, boardName):
        self.name = boardName
        self.cols = [0, 0, 0, 0, 0]
        self.rows = [0, 0, 0, 0, 0]
        self.numberMap = {}
        self.numbers = []
        self.board = []
        self.hasWon = False # added for Part 2; To not count a board again

    def addNumberToBoard(self, number, row, col):
        self.numberMap[number] = (row,col)

    def addRow(self, row, rowIdx):
        rowVals = row.split(" ")
        rowNums = []
        colIdx = 0

        # Loop through column values in row
        for val in rowVals:
            # Skip if empty
            if(val ==  ""):
                continue
            # Convert to number
            num = int(val)
            # Add to complete list of numbers
            self.numbers.append(num)
            rowNums.append(num)
            self.addNumberToBoard(num, rowIdx, colIdx)
            colIdx += 1

        self.board.append(rowNums)
        
    # Update mapping when a number is called
    def numberCalled(self, num):
        row = self.numberMap[num][0]
        self.rows[row] += 1

        col = self.numberMap[num][1]
        self.cols[col] += 1

        return self.hasBingo()

    # Check if this board contains a number
    def hasNumber(self, num):
        if(self.hasWon):
            return False
        return num in self.numbers

    # Check if this board has achieved bingo
    def hasBingo(self):
        maxCol = max(self.cols)
        maxRow = max(self.rows)

        isBingo = True if ((maxRow == 5) or (maxCol == 5)) else False
        self.hasWon = isBingo

        return isBingo

    # Print out the board
    def printBoard(self):
        for row in self.board:
            print(row)

    # Calculate the final score
    def calculateScore(self, numbersCalled, lastNumCalled):
        totalScore = 0
        for num in self.numbers:
            if num not in numbersCalled:
                totalScore += num
        
        totalScore *= lastNumCalled

        return totalScore