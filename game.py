import random

class GameBoard:
    def __init__(self):
        self.game_board = []
        self.mines = [Mine() for mine in range(0, random.randint(0, 4))]
        self.cleared_blocks = 8 * 8

    def generate_game_board(self) -> None:
        self.clear_board()
        mines_locations = self.generate_mines()
        # place mines
        self.place_mines(mines_locations)
        self.print_board()

    def place_mines(self, mines):
        for row in range(len(self.game_board)):
            self.game_board[row][mines[row]] = '[B]'

    def print_board(self):
        for row in self.game_board:
            print("".join(row))

    def clear_board(self):
        self.game_board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                current_row.append('[ ]')
            self.game_board.append(current_row)

    def generate_mines(self):
        random_indeces = []
        # generate random indexes for mines
        board_length = len(self.game_board) * len(self.game_board[0])
        board_half_length = int(board_length / 2)
        for i in range(board_half_length):
            random_index = random.randint(0, 8)
            if not random_index in random_indeces:
                random_indeces.append(random_index)
        return random_indeces

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
