from pieces import SymbolPiece

class Bishop(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, '♗', '♝')
    
    def get_moves(self, board):
       
        moves = []
       
        return moves
