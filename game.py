import random

class Game:
    def __init__(self):
        self.game_board = {}
        self.mines = [Mine() for mine in range(0, random.randint(0, 4))]
        self.cleared_blocks = 8 * 8

    def start_game(self):
        self.generate_game_board()

    def generate_game_board(self):
        self.clear_board()
        self.place_mines()
        self.print_board()

    def print_board(self):
        for row in range(8):
            row_display = []
            for col in range(8):
                row_display.append(self.game_board[(row, col)]["display"])
            print(" ".join(row_display))

    def clear_board(self):
        self.game_board = {}
        for row in range(8):
            for col in range(8):
                self.game_board[(row, col)] = {"is_mine": False, "display": "[ ]"}

    def place_mines(self):
        for row in range(8):
            random_row = random.randint(0, 7)
            random_col = random.randint(0, 7)
            self.game_board[(random_row, random_col)]["is_mine"] = True
            if self.game_board[(random_row, random_col)]["is_mine"] == True:
                self.game_board[(random_row, random_col)]["display"] = '[B]'

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

minesweeper_game = Game()
minesweeper_game.start_game()
