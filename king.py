# king.py

from pieces import SymbolPiece

class King(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, white_symbol='♔', black_symbol='♚')

    def get_moves(self, board):
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for direction in directions:
            new_row = self.get_row() + direction[0]
            new_col = self.get_column() + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board[new_row][new_col]
                if piece is None or piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))
        return moves
