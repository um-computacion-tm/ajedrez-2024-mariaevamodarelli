from pieces import SymbolPiece


class Rook(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, "♜", "♖")