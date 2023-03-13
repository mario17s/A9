import random

from exceptions.ending import GameOverException
from repo.repository import Board


class Operations:
    def __init__(self, board):
        self.__board = board

    def get_board(self):
        return self.__board.get_board()

    def add_symbol_on_board(self, row, column, symbol):
        if row < 0 or row >= self.__board.rows:
            raise ValueError("invalid row")
        if column < 0 or column >= self.__board.columns:
            raise ValueError("invalid column")
        if symbol not in ['X', 'O']:
            raise ValueError("invalid symbol")
        self.__board.add_symbol_on_board(row, column, symbol)

    def computer_round(self, computer_symbol):
        null_elements_found = 0
        matrix = self.get_board()
        for row_index in range(0, self.__board.rows):
            for column_index in range(0, self.__board.columns):
                if matrix[row_index][column_index].symbol == ' ':
                    null_elements_found = 1
        if null_elements_found == 0:
            raise GameOverException("Game over! YOU WON")

        row = random.randint(0, self.__board.rows - 1)
        column = random.randint(0, self.__board.columns - 1)
        while matrix[row][column].symbol != ' ':
            row = random.randint(0, self.__board.rows - 1)
            column = random.randint(0, self.__board.columns - 1)
        self.add_symbol_on_board(row, column, computer_symbol)

    @property
    def board(self):
        return self.__board

