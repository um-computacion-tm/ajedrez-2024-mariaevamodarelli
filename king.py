from pieces import SymbolPiece

class King(SymbolPiece):
    def get_moves(self, board):
        moves = []
        potential_moves = [
            (self.get_row() + 1, self.get_column()),
            (self.get_row() - 1, self.get_column()),
            (self.get_row(), self.get_column() + 1),
            (self.get_row(), self.get_column() - 1),
            (self.get_row() + 1, self.get_column() + 1),
            (self.get_row() + 1, self.get_column() - 1),
            (self.get_row() - 1, self.get_column() + 1),
            (self.get_row() - 1, self.get_column() - 1),
        ]
        SymbolPiece.add_potential_moves(board, moves, potential_moves, self.get_color())
        return moves
