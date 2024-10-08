class Piece:
    def __init__(self, color, row, col):
        self.__color__ = color
        self.__row__ = row
        self.__column__ = col

    def __repr__(self):
        return f"{self.__class__.__name__[0]}{self.__color__[0]}"

    def get_moves(self, board):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")
    
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

    def get_row(self):
        return self.__row__

    def get_column(self):
        return self.__column__

    def get_color(self):
        return self.__color__

    def add_moves_in_direction(self, board, row, col, direction, moves):
        d_row, d_col = direction
        r, c = row + d_row, col + d_col
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] is None:
                moves.append((r, c))
            else:
                if board[r][c].get_color() != self.__color__:
                    moves.append((r, c))
                break
            r += d_row
            c += d_col

    def add_potential_moves(self, board, moves, potential_moves):
        for r, c in potential_moves:
            if Piece.is_valid_position(r, c) and (board[r][c] is None or board[r][c].get_color() != self.__color__):
                moves.append((r, c))

    
    def is_valid_position(row, col):
        return 0 <= row < 8 and 0 <= col < 8


class SymbolPiece(Piece):
    def __init__(self, color, row, col, white_symbol, black_symbol):
        super().__init__(color, row, col)
        self.white_symbol = white_symbol
        self.black_symbol = black_symbol

    def __str__(self):
        return self.white_symbol if self.get_color() == "WHITE" else self.black_symbol
