# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Code to play the game of Tic-Tac-Toe.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this lab was handling the Dictionary data. I have more expirence with lists but after a while I learned about the .values() method. I also learned about how try except blocks and the ecept valueError proporty. 
# 5. How long did it take for you to complete the assignment?
#      This project took me about 3.5 hours to complete.
#sources:
    # I used this site to help fix a problem with my board
        # https://www.geeksforgeeks.org/python-program-to-change-values-in-a-dictionary/#
    # I used this source to better understand try except blocks and add the value error
        # https://www.pythontutorial.net/python-basics/python-try-except/

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
            1: BLANK, 2: BLANK, 3: BLANK,
            4: BLANK, 5: BLANK, 6: BLANK,
            7: BLANK, 8: BLANK, 9: BLANK 
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

def save_board(positions):
    '''Save the current game to a file.'''
    new_board = {1: positions[0],2:positions[1],3: positions[2],4: positions[3],5: positions[4],6: positions[5],7: positions[6],8: positions[7],9: positions[8]}
    board = json.dumps(new_board)
    with open("TickTacToe.json", "w") as file:
        file.write(board)

def display_board(positions):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print("The current board is: \n")
    print(f" {positions[0]} | {positions[1]} | {positions[2]} ")
    print("---+---+---")
    print(f" {positions[3]} | {positions[4]} | {positions[5]} ")
    print(f"---+---+---")
    print(f" {positions[6]} | {positions[7]} | {positions[8]} ")

def is_x_turn(turn):
    '''Determine whose turn it is.'''
    if turn == 1 or (turn % 2) == 0:
        return True
    else:
        return False    

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    turn = 1
    positions = list(board.values())
    display_board(positions)
    while game_done(positions) == False:
        turn += 1
        if is_x_turn(turn) == True:
            user_turn = X
        else: 
            user_turn = O
        try:
            keypress = int(input(f"{user_turn}, input a number bettween 1 and 9: "))
            position = keypress
            positions[position-1] = user_turn
        except ValueError: 
            save_board(positions)
            break 
        display_board(positions)

    return False

def game_done(positions, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == Tr4
       ue, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if positions[row * 3] != BLANK and positions[row * 3] == positions[row * 3 + 1] == positions[row * 3 + 2]:
            if message:
                print("The game was won by", positions[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if positions[col] != BLANK and positions[col] == positions[3 + col] == positions[6 + col]:
            if message:
                print("The game was won by", positions[col])
            return True

    # Game is finished if someone has a diagonal.
    if positions[4] != BLANK and (positions[0] == positions[4] == positions[8] or
                              positions[2] == positions[4] == positions[6]):
        if message:
            print("The game was won by", positions[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in positions:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True
    positions = (BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK)
    save_board(positions)


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
read_board()
play_game(read_board())