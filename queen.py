from pieces import SymbolPiece


class Queen(SymbolPiece):
    def __init__(self, color, x, y, white_symbol='♕', black_symbol='♛'):
        super().__init__(color, x, y, white_symbol, black_symbol)


    def get_moves(self, board):
        moves = []
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1), 
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        for direction in directions:
            self.add_moves_in_direction(board, moves, direction)
        return moves

    def add_moves_in_direction(self, board, moves, direction):
        row, col = self.__row__, self.__column__
        d_row, d_col = direction
        r, c = row + d_row, col + d_col

        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] is None:
                moves.append((r, c))
            else:
                if board[r][c].__color__ != self.__color__:
                    moves.append((r, c))
                break
            r += d_row
            c += d_col
