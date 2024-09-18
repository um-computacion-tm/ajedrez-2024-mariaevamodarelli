from pieces import SymbolPiece

class Knight(SymbolPiece):
    def get_moves(self, board):
        moves = []
        potential_moves = [
            (self.get_row() + 2, self.get_column() + 1),
            (self.get_row() + 2, self.get_column() - 1),
            (self.get_row() - 2, self.get_column() + 1),
            (self.get_row() - 2, self.get_column() - 1),
            (self.get_row() + 1, self.get_column() + 2),
            (self.get_row() + 1, self.get_column() - 2),
            (self.get_row() - 1, self.get_column() + 2),
            (self.get_row() - 1, self.get_column() - 2),
        ]
        SymbolPiece.add_potential_moves(board, moves, potential_moves, self.get_color())
        return moves
