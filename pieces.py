class Piece:
    def __init__(self, color, row, col):
        self.__color__ = color
        self.__row__ = row
        self.__column__ = col


    def __repr__(self):
        return f"{self.__class__.__name__[0]}{self.color[0]}"

    def get_moves(self, board):
        raise NotImplementedError

    def is_valid_move(self, dest_row, dest_col, board):
        moves = self.get_moves(board)
        return (dest_row, dest_col) in moves

    def move(self, dest_row, dest_col, board):
        if self.is_valid_move(dest_row, dest_col, board):
            board[dest_row][dest_col] = self
            board[self.__row__][self.__column__] = None
            self.__row__ = dest_row
            self.__column__ = dest_col
        else:
            print(f"Invalid move for {self}")


class SymbolPiece(Piece):
    def __init__(self, color, row, col, white_symbol, black_symbol):
        super().__init__(color, row, col)
        self.white_symbol = white_symbol
        self.black_symbol = black_symbol

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_symbol
        else:
            return self.black_symbol
