from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn


class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def is_checkmate(self, color):
        if not self.is_check(color):
            return False

        king_position = self.find_king(color)
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.__color__ == color:
                    for move in piece.get_moves(self):
                        if self.is_check_after_move(piece, move):
                            return False
        return True

    
    def is_check_after_move(self, piece, move):
        
        pass

    def find_king(self, color):
        
        pass

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def move_piece(self, piece, row, col):
        
        pass
