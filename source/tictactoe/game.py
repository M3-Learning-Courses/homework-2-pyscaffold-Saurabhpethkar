import os
import time
from pyfiglet import Figlet


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
                return True
            return False
        return False

    def check_winner(self, square, letter):
        row_idx = square // 3
        row = self.board[row_idx*3 : (row_idx+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_idx = square % 3
        col = [self.board[col_idx+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            left_diag = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in left_diag]):
                return True
            right_diag = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in right_diag]):
                return True

        return False

    def is_draw(self):
        return ' ' not in self.board and not self.current_winner


def play(game):
    game.print_board()

    letter = 'X'
    while game.board.count(' ') > 0 and not game.current_winner:
        move = int(input(f"'{letter}' Enter your move (0-8): "))
        if move in game.available_moves():
            game.make_move(move, letter)
            game.print_board()
            if game.current_winner:
                print(f"Player '{letter}' wins!")
                return
            elif game.is_draw():
                print("It's a tie!")
                return
            letter = 'O' if letter == 'X' else 'X'
        else:
            print("Invalid move! Try again.")


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('TIC TAC TOE'))
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    game = TicTacToe()
    play(game)
