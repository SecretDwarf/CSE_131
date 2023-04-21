# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Code to play the game of Tic-Tac-Toe.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }
def read_board():
    '''Read the previously existing board from the file if it exists.'''
    board_read = False
    try:
        with open("TickTacToe.json", "r") as file:
            board = json.load(file)
    except:
        board = blank_board
    return board

def save_board(board):
    '''Save the current game to a file.'''
    board = json.dumps(board)
    with open("TickTacToe.json", "w") as file:
        file.write(board)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # I had to google the list operator but lost the resource link
    positions = list(board.values())

    print(positions)
    print("The current board is: \n")

    positionOne = positions[0]
    positionTwo = positions[1]
    positionThree = positions[2]
    positionFour = positions[3]
    positionFive = positions[4]
    positionSix = positions[5]
    positionSeven = positions[6]
    positionEight = positions[7]
    positionNine = positions[8]
    print(f" {positionOne} | {positionTwo} | {positionThree} ")
    print("---+---+---")
    print(f" {positionFour} | {positionFive} | {positionSix} ")
    print(f"---+---+---")
    print(f" {positionSeven} | {positionEight} | {positionNine} \n")

def is_x_turn(turn):
    '''Determine whose turn it is.'''
    if turn == 1 or (turn % 2) == 0:
        return True
    else:
        return False    

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    turn = 1
    is_playing = True
    while is_playing == True:
        display_board(board)
        turn += 1
        if is_x_turn(turn) == True:
            user_turn = X
        else: 
            user_turn = O
        keypress = input(f"{user_turn}, input a number bettween 1 and 9: ")
        try:
            if type(keypress) == int:
                position = int(keypress) - 1
                board[position] = user_turn
                display_board()
        except:
            display_board()
            if type(keypress) == "string":
                save_board(board)
                break
        print(type(keypress))

    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")

# The file read code, game loop code, and file close code goes here.
play_game(read_board())