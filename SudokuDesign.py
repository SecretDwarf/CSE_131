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

def save_board(positions):
    """
    Save the current state of the board to a file.
    """
    new_board = {}
    positions = list(positions)
    for i in range(1, 10):
        row = positions[(i-1)*9:i*9]
        new_board[i] = row
    board = json.dumps(new_board)
    game = input("What do you want your file to be saved as? ") + ".json"
    with open(game, "w") as file:
        file.write(board)

def create_board(board_dict):
    """
    Create a new board based on the given dictionary.
    """
    board = {}
    for row in range(1, 10):
        for col in range(1, 10):
            board[str(row) + str(col)] = board_dict["board"][row-1][col-1]
    return board


def verify_key(key):
    """
    Verify that the given key is valid for a 9x9 grid.
    """
    # Generate a list of valid keys for a 9x9 grid
    valid_keys = [f"{col}{row}" for col in "ABCDEFGHI" for row in range(1, 10)]
    # Convert the key to uppercase and swap the characters if the first character is a digit
    key = key.upper()
    if keyas.isdigit():
        key = key[1] + key[0]
    # Check if the key is in the list of valid keys
    if key in valid_keys:
        return key
    return False

def display_board(board):
    """
    Print the current state of the board.
    """
    # Print the column labels
    print("\tA B C \tD E F \tG H I")
    print()
    # Loop through each row
    for i in range(1, 10):
        row = ''
        # Loop through each column
        for j in range(1, 10):
            # Add a vertical separator between blocks
            if j == 4 or j == 7:
                row += '| '
            # If the value is negative (user input), display it in red
            if board[str(i) + str(j)] < 0:
                row += '\033[91m' + str(abs(board[str(i) + str(j)])) + '\033[0m' + ' '
            else:
                row += str(board[str(i) + str(j)]) + ' '
        # Add a horizontal separator between blocks
        if i == 3 or i == 6:
            print('- - - + - - - + - - -')
        # Print the row
        print(row)

def game_over(board_dict):
    """
    Determine if the game is finished.
    """
    for row in range(1, 10):
        for col in range(1, 10):
            if board_dict[str(row) + str(col)] == 0:
                return False
    return True

def play_game():
    """
    Play a game of Sudoku.
    """
    board = get_board()
    while not game_over(board):
        display_board(board)
        valid_input = False
        while not valid_input:
            key = input("Enter a key (ex. A1) to add a number: ")
            if verify_key(key):
                valid_input = True
            else:
                print("Invalid input. Try again.")
        num = int(input("Enter a number to add to the board: "))
        if num >=1 and num <=9:
            board[key] = -num
        else:
            print("Invalid input. Try again.")
        save_board(board.values())
    display_board(board)
    print("Congratulations! You finished the game!")

play_game()
