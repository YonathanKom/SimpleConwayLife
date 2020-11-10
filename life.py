from random import getrandbits
from copy import deepcopy
from time import sleep

class Board:

    def __init__(self, my_board):
        self.height = len(my_board)
        self.width = len(my_board[0])
        self.board = deepcopy(my_board)

    @classmethod
    def blank_state(cls, width, height):
        b_state = [[0] * width for i in range(height)]
        return cls(b_state)

    @classmethod
    def random_state(cls, width, height):
        state = [[0] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                state[i][j] = getrandbits(1)
        return cls(state)

    @classmethod
    def from_file(cls, file_name):
        fhand = None
        try:
            fhand = open(file_name)
        except:
            print("Couldn't Open File")
            exit(1)

        state = list()
        for line in fhand:
            state.append(list())
            for char in line:
                if char == '0':
                    state[-1].append(0)
                elif char == '1':
                    state[-1].append(1)

        return cls(state)

    def next_state(self):
        next_state_board = deepcopy(self.board)
        adj_matrix = [[0] * self.width for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    continue
                if i > 0:
                    if j > 0:
                        adj_matrix[i-1][j-1] += 1
                    adj_matrix[i-1][j] += 1
                    if j < self.width - 1:
                        adj_matrix[i-1][j+1] += 1
                if j > 0:
                    adj_matrix[i][j-1] += 1
                if j < self.width - 1:
                    adj_matrix[i][j+1] += 1
                if i < self.height - 1:
                    if j > 0:
                        adj_matrix[i+1][j-1] += 1
                    adj_matrix[i+1][j] += 1
                    if j < self.width - 1:
                        adj_matrix[i+1][j+1] += 1

        for i in range(self.height):
            for j in range(self.width):
                if adj_matrix[i][j] == 3 and self.board[i][j] == 0:
                    next_state_board[i][j] = 1
                elif (adj_matrix[i][j] != 2 and adj_matrix[i][j] != 3) and self.board[i][j] == 1:
                    next_state_board[i][j] = 0

        return Board(next_state_board)

    def __str__(self):
        board_str = ('-' * (len(self.board[0]) + 2)) + '\n'
        for row in self.board:
            board_str += '|'
            for elem in row:
                if elem == 0:
                    board_str += ' '
                else:
                    board_str += '#'
            board_str += '|\n'
        board_str += ('-' * (len(self.board[0]) + 2)) + '\n'
        return board_str

board = Board.random_state(110, 25)

while True:
    print(board)
    board = board.next_state()
    sleep(0.03)
