from pieces import Pieces, SymbolPiece

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
            Pieces.add_moves_in_direction(self, board, moves, direction)
        return moves
