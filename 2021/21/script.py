import shared
from collections import deque


'''
***************************************************************
    Input
***************************************************************
'''

inputList = shared.getFileContentAsList("./example.txt")


'''
***************************************************************
    Functions
***************************************************************
'''

# Deterministic game
def deterministicDice(playerMap):

    map = dict(playerMap)

    names = list(playerMap.keys())

    firstRoll = 1
    turn = -1
    while True:

        turn = turn+1 if turn < len(names)-1 else 0

        currPlayer = names[turn]

        pos,score = map[currPlayer]

        secondRoll = firstRoll+1
        thirdRoll = firstRoll+2
        rolls = firstRoll + secondRoll + thirdRoll
        # Increase first roll die by 3
        firstRoll += 3

        # Calculate the new position on board
        newPos = pos + (rolls % 10)

        if(newPos > 10):
            newPos  = newPos - 10
        
        newScore = score + newPos

        map[currPlayer] = (newPos, newScore)

        # Get final value
        if(newScore >= 1000):
            print(map)

            mapValues= map.values()
            scores = [ x[1] for x in mapValues ]
            lowestScore = min(scores)
            answer = lowestScore * thirdRoll
            shared.printAnswer(answer)
            break
    



'''
    PLAN: 
        Make a queue of universes to proces

            One a roll (single, not all 3)
                Create universe of 2 players
                    With positionu updated for current player (by 1)
                    Position for other player is the same
                Create 2nd universe for 2 players
                    With positions updated for current player (by 2)
                    Position for other player is still the same
                Create 3rd universe for 2 players
                    With positiosn updtaed for current player (by 3)
                    Position for other player is still the same
                
            Continue this for the current game until one player wins (to 21)

            Whoever wins, add a tally for that player to the list of games won by that player

            NOTE: Will need to check if the player has already won BEFORE getting started on a game!
                > After a long while, the new games will be created with winners automatically.


    UPDATE:
        After checking reddit thread, there is lots of mention of memoization
        Key things to try:
            > Understanding all possible dice roll outcomes
            > Setting up memoization based on dice roll and player tunr
'''


# Create a new game to be played in one of the universe splits
def createUniverse(posScore, univNumber, currPlayer, sourceGame):

    game = {"Player 1": (), "Player 2": () }

    #print(sourceGame)

    new_pos = posScore[0] + univNumber % 10
    if(new_pos > 10):
        new_pos = new_pos-10
    
    new_score = posScore[1] + new_pos

    otherPlayer = "Player 2" if currPlayer == "Player 1" else "Player 1"
    #print("Other player == " + str(otherPlayer))

    game[currPlayer] = (new_pos, new_score)
    game[otherPlayer] = sourceGame[otherPlayer]

    print(game)
    # print('\n')
    return game


# Dirac dice
def diracDice(playerMap):
    map = dict(playerMap)

    gamesWon = {}

    for key in playerMap:
        if key not in gamesWon:
            gamesWon[key] = 0

    universes = deque()
    universes.append(playerMap)

    # While there are universes left to process
    while universes:

        game = universes.popleft()
        names = list(game.keys())


        turn = -1
        while True:

            turn = turn+1 if turn < len(names)-1 else 0

            currPlayer = names[turn]
            #print("Current Player = " + str(currPlayer))

            pos,score = game[currPlayer]

            if score >= 21:
                break

            newPos = pos
            newScore = score

            for roll in range(1,4):
                # Create the universes
                #if(roll == 1):

                univ = createUniverse( (pos,score), roll, currPlayer, game)
                universes.append(univ)
                
                newPos = pos + roll
                if(newPos > 10):
                    newPos = newPos-10
                newScore = newScore + newPos

                game[currPlayer] = (newPos, newScore)

            # Get final value
            if(newScore >= 21):
                
                break

        #print("\n\nGAME WON!")
        #print(game)
        winner = ""
        highestScore = 0
        for key in game:
            pos,score = game[key]
            if(score) > highestScore:
                highestScore = score
                winner = key
            if(winner != ""):
                gamesWon[winner] += 1
        #print(gamesWon)

    


    # while True:

    #     turn = turn+1 if turn < len(names)-1 else 0

    #     currPlayer = names[turn]

    #     pos,score = map[currPlayer]

    #     secondRoll = firstRoll+1
    #     thirdRoll = firstRoll+2
    #     rolls = firstRoll + secondRoll + thirdRoll
    #     # Increase first roll die by 3
    #     firstRoll += 3

    #     # Calculate the new position on board
    #     newPos = pos + (rolls % 10)

    #     if(newPos > 10):
    #         newPos  = newPos - 10
        
    #     newScore = score + newPos

    #     map[currPlayer] = (newPos, newScore)

    #     # Get final value
    #     if(newScore >= 1000):
    #         print(map)

    #         mapValues= map.values()
    #         scores = [ x[1] for x in mapValues ]
    #         lowestScore = min(scores)
    #         answer = lowestScore * thirdRoll
    #         shared.printAnswer(answer)
    #         break

        

'''
***************************************************************
    Run
***************************************************************
'''


map = {}

for player in inputList:
    splits = player.split(" starting position: ")
    playerName = splits[0]
    startingPos = int(splits[1])

    map[playerName] = (startingPos, 0)  # position and current score

# Part 1 - get deterministic game results
deterministicDice(map)

# Part 2
diracDice(map)



