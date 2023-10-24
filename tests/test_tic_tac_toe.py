import pytest
from source.tictactoe.tic_tac_toe import create_board, check_winner, is_draw, PLAYER_X, PLAYER_O, EMPTY
from source.tictactoe.tic_tac_toe import display_board, tic_tac_toe
from io import StringIO
import sys

def test_display_board():
    board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]
    expected_output = "X | O | X\n---------\nO |   |  \n---------\n  |   |  \n"
    
    # Capturing printed output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    display_board(board)

    sys.stdout = old_stdout

    output = mystdout.getvalue().strip()
    assert output == expected_output


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["1", "2", "3", "4", "5", "6", "7", "8", "9"], "\nIt's a draw!\n")
        # You can add more scenarios here
    ]
)
def test_tic_tac_toe(inputs, expected_output):
    # Mock input function to simulate a series of user inputs
    input_values = iter(inputs)
    old_input = __builtins__.input
    __builtins__.input = lambda _: next(input_values)

    # Capturing printed output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    tic_tac_toe()

    sys.stdout = old_stdout
    __builtins__.input = old_input

    output = mystdout.getvalue().strip().split("\n")[-1]
    assert output == expected_output