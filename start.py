from repo.repository import Board
from serv.services import Operations
from ui.console import Game

if __name__ == "__main__":
    board = Board(6,6)
    operations = Operations(board)
    game = Game(operations)
    game.begin_game()