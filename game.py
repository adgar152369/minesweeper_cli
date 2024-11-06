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
        print(mines[0], mines[1], mines[2])
        self.game_board[0][mines[0]] = '[B]'
        self.game_board[1][mines[1]] = '[B]'
        self.game_board[2][mines[2]] = '[B]'
        self.game_board[3][mines[3]] = '[B]'
        self.game_board[4][mines[4]] = '[B]'
        self.game_board[5][mines[5]] = '[B]'
        self.game_board[6][mines[6]] = '[B]'
        self.game_board[7][mines[7]] = '[B]'


    def print_board(self):
        # self.clear_board()
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
        # print(board_half_length)
        for i in range(board_half_length):
            random_index = random.randint(0, 7)
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
