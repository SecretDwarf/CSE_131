import json

def get_board():
    load_game = input("Do you want to load a saved game? (y/n): ")
    board = {}

    if load_game.lower() == 'y' or load_game.lower() == 'yes':
        try:
            given_file = input("What is the name of the file? ")
            with open(f"{given_file}.json", "r") as file:
                board = json.load(file)
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
    elif load_game.lower() == 'n' or load_game.lower() == 'no':
        board = create_board()
        difficulty = input("Select difficulty level (easy/medium/hard): ")
        if difficulty.lower() == 'easy':
            with open("131.05.Easy.json", "r") as file:
                board_dict = json.load(file)
            board.update(board_dict)
        elif difficulty.lower() == 'medium':
            with open("131.05.Medium.json", "r") as file:
                board_dict = json.load(file)
            board.update(board_dict)
        elif difficulty.lower() == 'hard':
            with open("131.05.Hard.json", "r") as file:
                board_dict = json.load(file)
            board.update(board_dict)
        else:
            print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
        board = verify_keys(board)
    else:
        print("Invalid input. Please enter 'y/yes' or 'n/no'.")

    return board

game = None
def save_board(board):
    global game
    if not game:
        game = input("Enter the name of the file to save changes to: ")
    board = json.dumps(board)
    with open(f"{game}.json", "w") as file:
        file.write(board)

def create_board():
    board = {}
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for column in columns:
        for row in rows:
            key = column + row
            board[key] = 0
    return board

def verify_keys(board):
    updated_board = {}
    for key, value in board.items():
        key = key.upper()  # Convert key to uppercase for consistency
        if len(key) != 2 or not key[0].isalpha() or not key[1].isdigit():
            # If the key is not in the correct format, skip it
            print(f"Ignoring invalid key: {key}")
            continue
        updated_board[key] = value
    return updated_board

def display_board(board):
    print("     A B C   D E F   G H I")
    print("   +-------+-------+-------+")
    for row in range(1, 10):
        row_str = f"{row}  | "
        for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            key = col + str(row)
            value = board[key]
            if value == 0:
                value = " "
            row_str += str(value) + " "
            if col in ['C', 'F']:
                row_str += "| "
        print(row_str + "|")
        if row in [3, 6]:
            print("   +-------+-------+-------+")
    print("   +-------+-------+-------+")

def play_game(board):
    while not game_done(board):
        display_board(board)
        cell = input("Enter cell position (e.g., A1), or type 'q' to quit: ")
        if cell.lower() == 'q':
            save_board(board)
            print("Game saved. Exiting...")
            return
        cell = cell.upper()  # Convert cell to uppercase for consistency
        if cell in board.keys():
            number = input("Enter a number (1-9): ")
            if number.isdigit() and 1 <= int(number) <= 9:
                board[cell] = int(number)
                display_board(board)
            else:
                print("Invalid number. Please enter a digit between 1 and 9.")
        else:
            print("Invalid cell position. Please enter a valid position (e.g., A1).")
    save_board(board)
    print("Congratulations! You have completed the game.")

def game_done(board):
    return all(value != 0 for value in board.values())

board = get_board()
play_game(board)