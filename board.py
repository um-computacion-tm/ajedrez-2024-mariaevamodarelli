from rook import Rook
from knight import Knight
from bishop import Bishop


class Board:
    def __init__(self):
            self.__positions__ = []
            for _ in range(8):
                col = []
                for _ in range(8):
                    col.append(None)
                self.__positions__.append(col)
            self.__positions__[0][0] = Rook("BLACK") # Black
            self.__positions__[0][7] = Rook("BLACK") # Black
            self.__positions__[0][1] = Knight("BLACK") # Black
            self.__positions__[0][6] = Knight("BLACK") # Black
            self.__positions__[0][2] = Bishop("BLACK") # Black
            self.__positions__[0][5] = Bishop("BLACK") # Black







            self.__positions__[7][7] = Rook("WHITE") # White
            self.__positions__[7][0] = Rook("WHITE") # White
            self.__positions__[7][1] = Knight("WHITE") # White
            self.__positions__[7][6] = Knight("WHITE") # White
            self.__positions__[7][2] = Bishop("WHITE") # White
            self.__positions__[7][5] = Bishop("WHITE") # White

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