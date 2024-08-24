from pieces import SymbolPiece


class Knight(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, "♞", "♘")