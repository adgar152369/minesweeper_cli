import random

class Game:
    def __init__(self, rows, cols):
        self.game_board = {}
        self.rows = rows
        self.cols = cols
        self.is_ended = False
        self.did_hit_mine = False
        self.mine_count = 0
        self.cleared_cells_count = 0

    def start_game(self):
        self.generate_game_board()
        self.print_game_board()

    def generate_game_board(self):
        for x in range(self.rows):
            current_row = []
            for y in range(self.cols):
                self.game_board[(x, y)] = {'is_mine': False, 'symbol': '[X]'}
        self.place_mines()

    def print_game_board(self):
        for x in range(self.rows):
            current_row = []
            for y in range(self.cols):
                current_row.append(self.game_board[(x, y)]['symbol'])
            print(" ".join(current_row))

    def show_points(self):
        print('Points: {}'.format(self.cleared_cells_count))

    def place_mines(self):
        placed_mines = 0
        while placed_mines < self.rows / 2:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            cell = (row, col)
            # Check if there's already a mine here
            if not self.game_board[cell]['is_mine']:
                self.game_board[cell]['is_mine'] = True
                self.game_board[cell]['symbol'] = '[✸]'
                placed_mines += 1

    def place_coordinates(self):
        coords = self.get_coordinates() # (int, int)
        is_coords_invalid = self.determine_hit(coords)

        if not is_coords_invalid:
            x, y = coords
            if not self.game_board[(x, y)]['symbol'] == '[ ]':
                self.cleared_cells_count += 1
                self.game_board[(x, y)]['symbol'] = '[ ]'
            self.clear_adjacent_cells(x,y)
            self.print_game_board()
        else:
            self.did_hit_mine = True

    def clear_adjacent_cells(self, x, y):
        adjacent_offsets = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dx, dy in adjacent_offsets:
            adj_x = x+dx
            adj_y = y+dy
            if 0 <= adj_x < self.rows and 0 <= adj_y < self.cols:
                if self.game_board[(adj_x, adj_y)]['symbol'] == '[ ]':
                    continue
                elif not self.determine_hit((adj_x, adj_y)):
                    self.game_board[(adj_x, adj_y)]['symbol'] = '[ ]'
                    self.cleared_cells_count += 1
                    self.mark_number_of_adjacent_mines((adj_x, adj_y), adjacent_offsets)
                else:
                    continue

    def get_coordinates(self) -> tuple:
        x = int(input('Enter an x coordinate from 0-{}: '.format(self.rows - 1)))
        y = int(input('Enter an y coordinate from 0-{}: '.format(self.cols - 1)))
        return (x, y)

    def determine_hit(self, coords):
        x, y = coords
        if self.game_board[(x, y)]['is_mine']:
            return True
        else:
            return False

    def mark_number_of_adjacent_mines(self, coords, offsets):
        x, y = coords
        mine_count = 0
        for dx, dy in offsets:
            ax = dx+x
            ay = dy+y
            if 0 <= ax < self.rows and 0 <= ay < self.cols:
                if self.game_board[(ax, ay)]['is_mine']:
                    mine_count += 1
                    self.game_board[(x, y)]['symbol'] = '[{}]'.format(mine_count)

    def end_game(self):
        self.is_ended = True

new_game = Game(12, 12)
new_game.start_game()

while not new_game.is_ended:
    new_game.place_coordinates()
    new_game.show_points()

    if new_game.did_hit_mine:
        new_game.end_game()
        print('kaboom! You lose.')

print('Your points: {}'.format(new_game.cleared_cells_count))
