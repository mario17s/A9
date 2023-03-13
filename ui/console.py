from exceptions.ending import GameOverException
import texttable


class Game:
    def __init__(self, operations):
        self.__operations = operations

    def print_board(self):
        table = texttable.Texttable()
        board = self.__operations.get_board()
        for row_index in range(0, self.__operations.board.rows):
            row = []
            for column_index in range(0, self.__operations.board.columns):
                row.append(board[row_index][column_index].symbol)
            table.add_row(row)
        print(table.draw())

    def player_round(self, player_symbol):
        null_elements_found = 0
        matrix = self.__operations.get_board()
        for row_index in range(0, self.__operations.board.rows):
            for column_index in range(0, self.__operations.board.columns):
                if matrix[row_index][column_index].symbol == ' ':
                    null_elements_found = 1
        if null_elements_found == 0:
            raise GameOverException("Game over! COMPUTER WON")
        try:
            row = int(input("give the row "))
            column = int(input("give the column "))
            self.__operations.add_symbol_on_board(row, column, player_symbol)
        except ValueError as ve:
            print(ve)
            return False
        return True


    def begin_game(self):
        print("Welcome to Obstruction Game!")
        print(f'This game has a board of {self.__operations.board.rows} rows and {self.__operations.board.columns} columns')
        option = input("Do you want to play first? yes or no ")
        while option not in ['yes', 'no']:
            option = input("Do you want to play first? yes or no ")
        if option == 'yes':
            player_symbol = 'O'
            computer_symbol = 'X'
        else:
            player_symbol = 'X'
            computer_symbol = 'O'
        while True:
            if option == 'yes':
                try:
                    validator = self.player_round(player_symbol)
                    while validator == False:
                        validator = self.player_round(player_symbol)
                    self.print_board()
                    print("Board after your move!")

                    self.__operations.computer_round(computer_symbol)
                    self.print_board()
                    print("Board after computer move!")
                except GameOverException as goe:
                    print(goe)
                    break
            else:
                try:
                    self.__operations.computer_round(computer_symbol)
                    self.print_board()
                    print("Board after computer move!")

                    validator = self.player_round(player_symbol)
                    while validator == False:
                        validator = self.player_round(player_symbol)
                    self.print_board()
                    print("Board after your move!")
                except GameOverException as goe:
                    print(goe)
                    break