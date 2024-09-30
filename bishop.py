from pieces import Piece, SymbolPiece


class Bishop(SymbolPiece):
    def get_moves(self, board):
        """Obtiene todos los movimientos posibles para el alfil."""
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
        for direction in directions:
            
            self.add_moves_in_direction(board, moves, direction, self.color)
        return moves
