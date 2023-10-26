import pytest
import io
import sys
from unittest.mock import patch
from source.tictactoe.tic_tac_toe import tic_tac_toe
from source.tictactoe.tic_tac_toe import create_board, display_board, check_winner, is_draw, PLAYER_X, PLAYER_O, EMPTY
from source.tictactoe.tic_tac_toe import display_board, tic_tac_toe

def test_check_winner():
    board = [PLAYER_X, PLAYER_X, PLAYER_X,
             EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    board = [PLAYER_X, EMPTY, EMPTY,
             PLAYER_X, EMPTY, EMPTY,
             PLAYER_X, EMPTY, EMPTY]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    board = [PLAYER_X, EMPTY, EMPTY,
             EMPTY, PLAYER_X, EMPTY,
             EMPTY, EMPTY, PLAYER_X]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    board = [EMPTY, EMPTY, PLAYER_O,
             EMPTY, PLAYER_O, EMPTY,
             PLAYER_O, EMPTY, EMPTY]
    assert check_winner(board, PLAYER_O) == True
    assert check_winner(board, PLAYER_X) == False

def test_is_draw():
    board = [PLAYER_X, PLAYER_O, PLAYER_X,
             PLAYER_X, PLAYER_X, PLAYER_O,
             PLAYER_O, PLAYER_X, PLAYER_O]
    assert is_draw(board) == True

    board = [EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY]
    assert is_draw(board) == False

    board = [PLAYER_X, PLAYER_X, PLAYER_X,
             EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY]
    assert is_draw(board) == False
    

# This will test for invalid inputs. Here, '10' is invalid because the board positions are 1-9. After '10', '1' is provided as a valid input.
@patch('builtins.input', side_effect=['10', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_tic_tac_toe_invalid_input(mock_input):
    with patch('builtins.print') as mock_print:  # This will mock the print function so the game progress won't print during testing
        tic_tac_toe()
        mock_print.assert_any_call("Invalid move. Try again.")
        
def test_display_board():
    board = [PLAYER_X, PLAYER_O, PLAYER_X,
             PLAYER_X, PLAYER_X, PLAYER_O,
             PLAYER_O, PLAYER_X, PLAYER_O]

    # Redirect stdout to capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    display_board(board)

    sys.stdout = sys.__stdout__

    expected_output = "X | O | X\n-----\nX | X | O\n-----\nO | X | O\n"

    assert captured_output.getvalue() == expected_output

@patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_tic_tac_toe_full_game(mock_input):
    # This will simulate a full game where the players just fill up the board in order
    # This should end in a draw
    tic_tac_toe()

    # You might want to capture print statements using a similar approach as the display_board test to ensure the game progressed correctly