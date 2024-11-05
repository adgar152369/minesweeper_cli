import random

class GameBoard:
    def __init__(self):
        self.game_board = []
        self.mines = [Mine() for mine in range(0, random.randint(0, 4))]
        self.cleared_blocks = 8 * 8

    def generate_game_board(self) -> None:
        for row in range(8):
            current_row = []
            for col in range(8):
                current_row.append('[]')
            self.game_board.append(current_row)
        for row in self.game_board:
            print("".join(row))

class ClearedBlock:
    def __init__(self):
        self.space = ""
        self.adjacent_mines = 0

    def determine_adjacent_mines(self):
        pass

class Mine:
    name = 'mine'

    def __repr__(self) -> str:
        return 'a mine'

game_board = GameBoard()
game_board.generate_game_board()
