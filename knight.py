from pieces import SymbolPiece

class Knight(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, '♘', '♞')
    
    def get_moves(self, board):
        # Implementación específica para Knight
        moves = []
        # Lógica para los movimientos válidos del Knight
        return moves
