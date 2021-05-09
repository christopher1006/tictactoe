# TODO Function - take player input
def takePlayerInput():
    print("Select column: ")
    col = input()

    print("Select row: ")
    row = input()
    return col, row

def checkGameOver():
    print("reached checkGameOver")
    return True


# Define game board

Board = [   ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

# Allow shape choice for player one.

print("What shape is player 1?\n")
playerChoice = input()
playerOneShape = playerChoice

print("What shape is player 2?\n")
playerChoice = input()
playerTwoShape = playerChoice

# TODO Run game round loop that goes until end-game conditions are met.
isGameOver = False
playerOneTurn = True

while (isGameOver is False):

    if playerOneTurn is True:
        print("Player 1")
        col, row = takePlayerInput()
        Board[col][row] = playerOneShape
    elif playerOneTurn is False:
        print("Player 1")
        col, row = takePlayerInput()
        Board[col][row] = playerTwoShape
    else:
        print ("Error bA31")

    isGameOver = checkGameOver()

print("Game is over. Goodbye")

# Take user input to change game board state
# Run player input function assigning alternately to player one or two depending on the turn.



# TODO Determine end-game conditions

# TODO Let player opt to exit or rematch.
