import pytest
from unittest.mock import patch, Mock, call
from source.tictactoe import tic_tac_toe
from source.tictactoe.tic_tac_toe import tic_tac_toe, check_winner, PLAYER_X, PLAYER_O, EMPTY

def test_check_winner_rows():
    # Test winning rows for PLAYER_X
    board = [
        [PLAYER_X, PLAYER_X, PLAYER_X],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    # Test winning rows for PLAYER_O
    board = [
        [PLAYER_O, PLAYER_O, PLAYER_O],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_O) == True
    assert check_winner(board, PLAYER_X) == False

def test_check_winner_columns():
    # Test winning columns for PLAYER_X
    board = [
        [PLAYER_X, EMPTY, EMPTY],
        [PLAYER_X, EMPTY, EMPTY],
        [PLAYER_X, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    # Test winning columns for PLAYER_O
    board = [
        [PLAYER_O, EMPTY, EMPTY],
        [PLAYER_O, EMPTY, EMPTY],
        [PLAYER_O, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_O) == True
    assert check_winner(board, PLAYER_X) == False

def test_check_winner_diagonals():
    # Test winning diagonals for PLAYER_X
    board = [
        [PLAYER_X, EMPTY, EMPTY],
        [EMPTY, PLAYER_X, EMPTY],
        [EMPTY, EMPTY, PLAYER_X]
    ]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    board = [
        [EMPTY, EMPTY, PLAYER_X],
        [EMPTY, PLAYER_X, EMPTY],
        [PLAYER_X, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_X) == True
    assert check_winner(board, PLAYER_O) == False

    # Test winning diagonals for PLAYER_O
    board = [
        [PLAYER_O, EMPTY, EMPTY],
        [EMPTY, PLAYER_O, EMPTY],
        [EMPTY, EMPTY, PLAYER_O]
    ]
    assert check_winner(board, PLAYER_O) == True
    assert check_winner(board, PLAYER_X) == False

    board = [
        [EMPTY, EMPTY, PLAYER_O],
        [EMPTY, PLAYER_O, EMPTY],
        [PLAYER_O, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_O) == True
    assert check_winner(board, PLAYER_X) == False

def test_no_winner():
    board = [
        [PLAYER_X, PLAYER_O, PLAYER_X],
        [PLAYER_X, PLAYER_X, PLAYER_O],
        [PLAYER_O, PLAYER_X, PLAYER_O]
    ]
    assert check_winner(board, PLAYER_X) == False
    assert check_winner(board, PLAYER_O) == False

    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert check_winner(board, PLAYER_X) == False
    assert check_winner(board, PLAYER_O) == False
    
@patch("source.tictactoe.tic_tac_toe.sg.popup", return_value=True) # Mocking the sg.popup method
@patch("builtins.input", side_effect=["0,0", "0,1", "0,2", "1,0", "1,2", "1,1", "2,0", "2,1", "2,2"]) # Mocking the input method
def test_game_play_draw(mock_input, mock_popup):
    tic_tac_toe()
    mock_popup.assert_called_with("It's a draw!") # Check if sg.popup was called with the expected message
