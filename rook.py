from pieces import SymbolPiece
from board import Board


class Rook(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, "♜", "♖")