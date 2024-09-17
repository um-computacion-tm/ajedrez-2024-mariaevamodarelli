from pieces import Pieces, SymbolPiece

class Knight(SymbolPiece):
    def __init__(self, color, x, y, white_symbol='♘', black_symbol='♞'):
        super().__init__(color, x, y, white_symbol, black_symbol)

    def get_moves(self, board):
        moves = []
        potential_moves = [
            (self.__row__ + 2, self.__column__ + 1), (self.__row__ + 2, self.__column__ - 1),
            (self.__row__ - 2, self.__column__ + 1), (self.__row__ - 2, self.__column__ - 1),
            (self.__row__ + 1, self.__column__ + 2), (self.__row__ + 1, self.__column__ - 2),
            (self.__row__ - 1, self.__column__ + 2), (self.__row__ - 1, self.__column__ - 2)
        ]
        for r, c in potential_moves:
            if Pieces.is_valid_position(r, c) and (board[r][c] is None or board[r][c].__color__ != self.__color__):
                moves.append((r, c))
        return moves
