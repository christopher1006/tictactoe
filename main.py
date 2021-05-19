def takePlayerInput():
    print("Select column: ")
    col = input()

    print("Select row: ")
    row = input()
    return col, row

def checkGameOver(Board, pOneSymbol, pTwoSymbol):
    pOne = ord(pOneSymbol)
    pTwo = ord(pTwoSymbol)
    winOne = pOne*3
    winTwo = pTwo*3

    for row in range(0, 3):
        # Currently just prints board
        # TODO Go through each row FIRST to check for non-zero value. Only check 'col' if True
        for col in range(0, 3):
            print(Board[row][col], end="")
        print("")

    playerSum = 0
    for row in range(0,3): #Check rows for horizontal victory
        if ord(Board[row][0]) is pOne or ord(Board[row][0]) is pTwo:
            print("player piece on first row")
            playerSum += ord(Board[row][0])
        elif ord(Board[row][1]) is pOne or ord(Board[row][1]) is pTwo:
            print("player piece on second row")
            playerSum += ord(Board[row][1])            
        elif ord(Board[row][2]) is pOne or ord(Board[row][2]) is pTwo:
            print("player piece on third row")
            playerSum += ord(Board[row][2])

        print("-----------DEBUG BLOCK-----------")
        print("playerSum = " + str(playerSum))
        print("pOne = " + str(pOne))
        print("pTwo = " + str(pTwo))
        print("Board[row][0] = " + str(ord(Board[row][0])))
        print("Board[row][1] = " + str(ord(Board[row][1])))
        print("Board[row][2] = " + str(ord(Board[row][2])))
        print("-----------DEBUG BLOCK-----------")

        if playerSum is winOne:
            print("Player 1 wins!")
            return True
        elif playerSum is winTwo:
            print("Player 2 wins!")
            return True
        else:
            print("No winner yet, keep going!")
            return False

# Define game board

Board = [   ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

# Allow shape choice for player one. Defines playpiece token


# TODO Ensure that input is only one character for each play piece.
print("What shape is player 1?\n")
playerChoice = input()
playerOneShape = playerChoice

print("What shape is player 2?\n")
playerChoice = input()
playerTwoShape = playerChoice

# TODO Run game round loop that goes until end-game conditions are met.
isGameOver = False
playerOneTurn = True

while (isGameOver is False): # Initiate game loop

    if playerOneTurn is True: #Players select their next placement
        print("Player 1")
        col, row = takePlayerInput() #TODO Ensure valid number entry
        Board[int(col)][int(row)] = playerOneShape
    else:
        print("Player 2")
        col, row = takePlayerInput()
        Board[int(col)][int(row)] = playerTwoShape

    isGameOver = checkGameOver(Board, playerOneShape, playerTwoShape)

print("Game is over. Goodbye")

# Take user input to change game board state
# Run player input function assigning alternately to player one or two depending on the turn.



# TODO Determine end-game conditions

# TODO Let player opt to exit or rematch.
