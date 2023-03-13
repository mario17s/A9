import unittest

from domain.entities import Cell


class Board:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = [[Cell(' ') for index1 in range(0, self.__columns)] for index2 in range(0, self.__rows)]

    def add_symbol_on_board(self, row, column, symbol):
        if self.__matrix[row][column].symbol in ['O', 'X', '/']:
            raise ValueError("You cannot move there")
        self.__matrix[row][column].symbol = symbol
        for row_index in range(0, self.__rows):
            for column_index in range(0, self.__columns):
                if (row_index == row or row_index == row - 1 or row_index == row + 1) and (column_index == column or column_index == column - 1 or column_index == column + 1) and (row_index != row or column_index != column):
                    self.__matrix[row_index][column_index].symbol = '/'

    def get_board(self):
        return self.__matrix

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns





