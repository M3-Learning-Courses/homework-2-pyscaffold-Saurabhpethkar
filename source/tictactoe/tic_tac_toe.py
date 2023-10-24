import pyfiglet

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def create_board():
    """Initialize a new Tic Tac Toe board."""
    return [EMPTY] * 9

def display_board(board):
    """Display the board using pyfiglet for fancy fonts."""
    display_string = ""
    for i in range(0, 9, 3):
        display_string += f"{board[i]} | {board[i+1]} | {board[i+2]}\n"
        if i < 6:
            display_string += "-" * 9 + "\n"
    print(display_string)

def check_winner(board, player):
    """Checks if the given player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combination in winning_combinations:
        if all([board[i] == player for i in combination]):
            return True
    return False

def is_draw(board):
    """Check if the game has ended in a draw."""
    return EMPTY not in board

def get_user_move(board, current_player):
    """Get the user's move."""
    while True:
        try:
            position = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == EMPTY:
                return position
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a valid number between 1 and 9.")

def play_single_turn(board, current_player):
    """Plays a single turn of Tic Tac Toe."""
    position = get_user_move(board, current_player)
    board[position] = current_player
    
    display_board(board)
                
    if check_winner(board, current_player):
        print(f"\nPlayer {current_player} wins!\n")
        return True
    elif is_draw(board):
        print("\nIt's a draw!\n")
        return True

    return False

def tic_tac_toe():
    """The main Tic Tac Toe game function."""
    board = create_board()
    current_player = PLAYER_X
    display_board(board)

    game_over = False
    while not game_over:
        game_over = play_single_turn(board, current_player)
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    welcome_msg = pyfiglet.figlet_format("Welcome to Tic Tac Toe!")
    print(welcome_msg)
    
    while True:
        tic_tac_toe()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
