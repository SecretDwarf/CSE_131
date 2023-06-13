# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program is to play and solve a sudoku board
# 4. What was the hardest part? Be as specific as possible.
#      The solver was really frustrating. it only took me a couple hours to figure out the easy solver but everything I've tried today for the medium and hard ones I haven't got to work. nothing like 7 hours of failure to make your day. I was able to learn alot about backtracking, comments, cohesion, and debugging today so luckily it wasn'y all a waste.
# 5. How long did it take for you to complete the assignment?
#      I spent around 10 hours this week but was able to learn alot of things first hand like how to change text color in a terminal, how various techniques of backtracking work, and about how uncmomented code is an abomination.

import json

def get_board():
    board = {}
    while True:
        load_game = input("Do you want to load a saved game? (y/n): ")
        if load_game.lower() in ('y', 'yes'):
            try:
                given_file = input("What is the name of the file? ")
                with open(f"{given_file}.json", "r") as file:
                    board = json.load(file)
                break
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
        elif load_game.lower() in ('n', 'no'):
            difficulty = input("Select difficulty level (easy/medium/hard): ")
            try:
                with open(f"131.05.{difficulty.capitalize()}.json", "r") as file:
                    board_dict = json.load(file)
                board = create_board(board_dict)
                break
            except FileNotFoundError:
                print(f"Invalid difficulty level: {difficulty}. Please enter a valid difficulty level.")
    return board

def save_board(board, game_name):
    board = json.dumps(board)
    with open(f"{game_name}.json", "w") as file:
        file.write(board)

def create_board(board_dict):
    """
    Create a new board based on the given dictionary.
    """
    board = {}
    for row in range(1, 10):
        for col in range(1, 10):
            board[chr(64+col) + str(row)] = 0  # Initialize each cell with a value of 0
            if board_dict["board"][row-1][col-1] != 0:
                board[chr(64+col) + str(row)] = board_dict["board"][row-1][col-1]
    return board

def verify_key(key):
    """
    Verify that the given key is valid for a 9x9 grid.
    """
    # Generate a list of valid keys for a 9x9 grid
    valid_keys = [f"{col}{row}" for col in "ABCDEFGHI" for row in range(1, 10)]
    # Convert the key to uppercase and swap the characters if the first character is a digit
    key = key.upper()
    if key[0].isdigit():
        key = key[1] + key[0]
    # Check if the key is in the list of valid keys
    if key in valid_keys:
        return key
    return False

def is_valid_move(board, key, value):
    """
    Check if the given value is a valid move for the given cell.
    """
    row = int(key[1])
    col = ord(key[0]) - 64

    if board[chr(64+col) + str(row)] > 0:
        return False

    # Check the row
    for c in range(1, 10):
        if c != col and board[chr(64+c) + str(row)] == value:
            return False

    # Check the column
    for r in range(1, 10):
        if r != row and board[chr(64+col) + str(r)] == value:
            return False

    # Check the block
    block_row = (row - 1) // 3 * 3 + 1
    block_col = (col - 1) // 3 * 3 + 1
    for r in range(block_row, block_row+3):
        for c in range(block_col, block_col+3):
            if r != row and c != col and board[chr(64+c) + str(r)] == value:
                return False

    return True

def display_board(board):
    """
    Print the current state of the board.
    """
    # Print the column labels
    print("Current board: ")
    print("  A B C   D E F   G H I")
    print()
    # Loop through each row
    for i in range(1, 10):
        row = f"{i} "
        # Loop through each column
        for j in range(1, 10):
            # Add a vertical separator between blocks
            if j == 4 or j == 7:
                row += '| '
            # If the value is negative (user input), display it in red or green depending on whether it's valid or not
            if board[chr(64+j) + str(i)] < 0:
                if is_valid_move(board, chr(64+j) + str(i), abs(board[chr(64+j) + str(i)])):
                    row += '\033[92m' + str(abs(board[chr(64+j) + str(i)])) + '\033[0m' + ' '
                else:
                    row += '\033[91m' + str(abs(board[chr(64+j) + str(i)])) + '\033[0m' + ' '
            elif board[chr(64+j) + str(i)] == 0:
                row += '.' + ' '
            else:
                row += str(board[chr(64+j) + str(i)]) + ' '
        # Add a horizontal separator between blocks
        if i == 4 or i == 7:
            print('  - - - + - - - + - - -')
        # Print the row
        print(row)

def game_over(board_dict):
    """
    Determine if the game is finished.
    """
    for row in range(1, 10):
        for col in range(1, 10):
            if board_dict[chr(64+col) + str(row)] == 0:
                return False
    return True

def get_possibilities(board):
    """
    Get the list of possibilities for each cell on the board.
    """
    # Initialize the list of possibilities for each cell
    possibilities = {}
    for row in range(1, 10):
        for col in range(1, 10):
            if board[chr(64+col) + str(row)] == 0:
                possibilities[chr(64+col) + str(row)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                possibilities[chr(64+col) + str(row)] = [board[chr(64+col) + str(row)]]

    # Eliminate possibilities based on the current state of the board
    for row in range(1, 10):
        for col in range(1, 10):
            if len(possibilities[chr(64+col) + str(row)]) > 1:
                # Check the row
                for c in range(1, 10):
                    if c != col and len(possibilities[chr(64+c) + str(row)]) == 1:
                        if possibilities[chr(64+c) + str(row)][0] in possibilities[chr(64+col) + str(row)]:
                            possibilities[chr(64+col) + str(row)].remove(possibilities[chr(64+c) + str(row)][0])
                # Check the column
                for r in range(1, 10):
                    if r != row and len(possibilities[chr(64+col) + str(r)]) == 1:
                        if possibilities[chr(64+col) + str(r)][0] in possibilities[chr(64+col) + str(row)]:
                            possibilities[chr(64+col) + str(row)].remove(possibilities[chr(64+col) + str(r)][0])
                # Check the block
                block_row = (row - 1) // 3 * 3 + 1
                block_col = (col - 1) // 3 * 3 + 1
                for r in range(block_row, block_row+3):
                    for c in range(block_col, block_col+3):
                        if r != row and c != col and len(possibilities[chr(64+c) + str(r)]) == 1:
                            if possibilities[chr(64+c) + str(r)][0] in possibilities[chr(64+col) + str(row)]:
                                possibilities[chr(64+col) + str(row)].remove(possibilities[chr(64+c) + str(r)][0])

    return possibilities

def display_possibilities(possibilities):
    """
    Print the list of possibilities for each cell on the board.
    """
    # Print the possibilities for each cell
    for key in sorted(possibilities.keys()):
        if len(possibilities[key]) > 1:
            print(f"{key}: {possibilities[key]}")


def solve_board(board, possibilities):
    """
    Solve the given Sudoku board using a list of possibilities for each cell.
    """
    # Iterate until the board is solved or no more progress can be made
    while not game_over(board):
        progress = False
        # Eliminate possibilities based on the current state of the board
        for row in range(1, 10):
            for col in range(1, 10):
                key = chr(64+col) + str(row)
                if len(possibilities[key]) > 1:
                    # Check the row
                    for c in range(1, 10):
                        if c != col and len(possibilities[chr(64+c) + str(row)]) == 1:
                            if possibilities[chr(64+c) + str(row)][0] in possibilities[key]:
                                possibilities[key].remove(possibilities[chr(64+c) + str(row)][0])
                                progress = True
                    # Check the column
                    for r in range(1, 10):
                        if r != row and len(possibilities[chr(64+col) + str(r)]) == 1:
                            if possibilities[chr(64+col) + str(r)][0] in possibilities[key]:
                                possibilities[key].remove(possibilities[chr(64+col) + str(r)][0])
                                progress = True
                    # Check the block
                    block_row = (row - 1) // 3 * 3 + 1
                    block_col = (col - 1) // 3 * 3 + 1
                    for r in range(block_row, block_row+3):
                        for c in range(block_col, block_col+3):
                            if r != row and c != col and len(possibilities[chr(64+c) + str(r)]) == 1:
                                if possibilities[chr(64+c) + str(r)][0] in possibilities[key]:
                                    possibilities[key].remove(possibilities[chr(64+c) + str(r)][0])
                                    progress = True

        # If no progress was made during this iteration, try guessing a value for a cell with the fewest number of possibilities
        if not progress:
            min_possibilities = min([len(v) for v in possibilities.values() if len(v) > 1], default=0)
            if min_possibilities == 0:
                return None
            for key in possibilities.keys():
                if len(possibilities[key]) == min_possibilities:
                    for value in possibilities[key]:
                        new_board = board.copy()
                        new_board[key] = value
                        new_possibilities = get_possibilities(new_board)
                        result = solve_board(new_board, new_possibilities)
                        if result is not None:
                            return result
                    return None

        # Update the board with any cells that have only one possibility left
        for key in possibilities.keys():
            if len(possibilities[key]) == 1:
                board[key] = possibilities[key][0]

    return board

def menu(board, possibilities):
    """
    Display a menu with options to make a guess, see possibilities, and save and quit.
    """
    while True:
        print("Menu:")
        print("1. Make a guess")
        print("2. See possibilities")
        print("3. Save and quit")
        print("4. See Solution")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_board(board)
            valid_input = False
            while not valid_input:
                key = input("Enter a key (ex. A1) to add a number: ")
                key = verify_key(key)
                if key:
                    if board[key] <= 0:
                        valid_input = True
                    else:
                        print("This cell already has a given value. Try again.")
                else:
                    print("Invalid input. Try again.")
            num = int(input("Enter a number to add to the board: "))
            if num >= 1 and num <= 9:
                board[key] = -num
            else:
                print("Invalid input. Try again.")
            save_board(board, game_name)
            display_board(board)
        elif choice == '2':
            display_possibilities(possibilities)
        elif choice == '3':
            save_board(board, game_name)
            return True
            break
        elif choice == '4':
            solve_board(board, get_possibilities(board))
            display_board(board)
            # display_board(board, get_possibilities(board))
            break
def play_game():
    """
    Play a game of Sudoku.
    """
    board = get_board()
    global game_name
    game_name = input("What would you like this game saved as? ")
    display_board(board)
    while not game_over(board):   
        if menu(board, get_possibilities(board)) == True:
            break
    print("Thank you for playing. Please come again soon.")

play_game()