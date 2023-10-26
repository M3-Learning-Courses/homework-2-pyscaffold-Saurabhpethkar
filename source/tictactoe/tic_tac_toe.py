import pyfiglet


PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def create_board():
    """Initialize a new Tic Tac Toe board."""
    return [EMPTY] * 9

def display_board(board):
    """Display the board."""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def is_draw(board):
    """Check if the game has ended in a draw."""
    return EMPTY not in board

def tic_tac_toe():
    """Main Tic Tac Toe game function."""
    board = create_board()
    current_player = PLAYER_X
    while True:
        display_board(board)
        try:
            position = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == EMPTY:
                board[position] = current_player
                if check_winner(board, current_player):
                    display_board(board)
                    print(f"\nPlayer {current_player} wins!\n")
                    return
                elif is_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    return
                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Enter a number between 1 and 9.")

if __name__ == "__main__":
    welcome_msg = pyfiglet.figlet_format("Tic Tac Toe!")
    print(welcome_msg)
    tic_tac_toe()
