from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and piece.__color__ == self.__turn__:
            piece.move(to_row, to_col, self.__board__.__positions__)
            self.change_turn()
        else:
            print("Invalid move or no piece at the source position.")

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
