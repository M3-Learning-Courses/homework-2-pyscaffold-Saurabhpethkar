import PySimpleGUI as sg
import pyfiglet

# Constants for the game
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def draw_board(board):
    """
    Creates the Tic Tac Toe board using PySimpleGUI.
    """
    title = pyfiglet.figlet_format("Tic Tac Toe")
    layout = [[sg.Text(title, font=("Any", 10), justification='center')]]

    for i, row in enumerate(board):
        row_list = []
        for j, cell in enumerate(row):
            row_list.append(sg.Button(cell, size=(5, 2), key=(i, j), font=("Any", 24)))
        layout.append(row_list)

    layout.append([sg.Button("Restart", size=(15, 2), key="Restart", font=("Any", 18))])

    return sg.Window("Tic Tac Toe", layout, finalize=True)

def tic_tac_toe():
    ...
    
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = PLAYER_X
    window = draw_board(board)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        if event == "Restart":
            board = [[EMPTY] * 3 for _ in range(3)]
            current_player = PLAYER_X
            window.close()
            window = draw_board(board)
            continue
        
        if board[event[0]][event[1]] == EMPTY:
            board[event[0]][event[1]] = current_player
            window[event].update(current_player)
            if check_winner(board, current_player):
                sg.popup(f"Player {current_player} wins!")
                board = [[EMPTY] * 3 for _ in range(3)]
                current_player = PLAYER_X
                window.close()
                window = draw_board(board)
            else:
                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    window.close()

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

if __name__ == "__main__":
    tic_tac_toe()

