import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to initialize the board
def initialize_board():
    board = []
    for _ in range(4):
        board.append([0] * 4)
    return board

# Function to print the board
def print_board(board, players):
    print("Current Board:")
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                print(" - ", end="")
            else:
                print(" " + players[cell - 1] + " ", end="")
        print()

# Function to move the token
def move_token(board, player, steps):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == player:
                if i == 0 and j + steps < 4:
                    board[i][j] = 0
                    board[i][j + steps] = player
                    return
                elif i + steps < 4:
                    board[i][j] = 0
                    board[i + steps][j] = player
                    return

# Main function to play the game
def play_ludo(players):
    board = initialize_board()
    player_count = len(players)
    current_player = 0

    while True:
        print_board(board, players)

        input(f"{players[current_player]}, press Enter to roll the dice.")
        dice_roll = roll_dice()
        print(f"{players[current_player]} rolled a {dice_roll}.")

        move_token(board, current_player + 1, dice_roll)

        if current_player == player_count - 1:
            current_player = 0
        else:
            current_player += 1

# Main program
if __name__ == "__main__":
    player_names = []
    num_players = int(input("Enter the number of players (2-4): "))
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        player_names.append(name)

    print("Starting Ludo Game!")
    play_ludo(player_names)
