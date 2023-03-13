import unittest


class Cell:
    def __init__(self, symbol):
        self.__symbol = symbol

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    def __str__(self):
        return str(self.__symbol)

class TestCell(unittest.TestCase):
    def test(self):
        new_cell = Cell(' ')
        self.assertEqual(new_cell.symbol, ' ')
        