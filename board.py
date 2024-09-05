from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

        # Piezas negras
        self.__positions__[0][0] = Rook("BLACK", 0, 0)
        self.__positions__[0][7] = Rook("BLACK", 0, 7)
        self.__positions__[0][1] = Knight("BLACK", 0, 1)
        self.__positions__[0][6] = Knight("BLACK", 0, 6)
        self.__positions__[0][2] = Bishop("BLACK", 0, 2)
        self.__positions__[0][5] = Bishop("BLACK", 0, 5)
        self.__positions__[0][3] = Queen("BLACK", 0, 3)
        self.__positions__[0][4] = King("BLACK", 0, 4)

        # Piezas blancas
        self.__positions__[7][7] = Rook("WHITE", 7, 7)
        self.__positions__[7][0] = Rook("WHITE", 7, 0)
        self.__positions__[7][1] = Knight("WHITE", 7, 1)
        self.__positions__[7][6] = Knight("WHITE", 7, 6)
        self.__positions__[7][2] = Bishop("WHITE", 7, 2)
        self.__positions__[7][5] = Bishop("WHITE", 7, 5)
        self.__positions__[7][3] = Queen("WHITE", 7, 3)
        self.__positions__[7][4] = King("WHITE", 7, 4)

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]
