from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
from pieces import Piece, SymbolPiece




class Board:
    def __init__(self):
        self.__board__ = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        """Coloca una pieza en una posición específica del tablero."""
        self.__board__[row][col] = piece
        piece.move(row, col, self.__board__)

    def move_piece(self, piece, row, col):
        """Mueve una pieza a una nueva posición si es válido."""
        if not piece.is_valid_move(row, col, self.__board__):
            raise ValueError(f"Movimiento inválido de {piece} a la posición {row}, {col}")
        self.__board__[piece.row][piece.col] = None  
        self.place_piece(piece, row, col)  

    def is_check(self, color):
        """Verifica si el rey del color dado está en jaque."""
      
        king = None
        for row in self.__board__:
            for piece in row:
                if piece is not None and piece.get_type() == 'king' and piece.get_color() == color:
                    king = piece
                    break
        if not king:
            raise ValueError(f"No se encontró al rey del color {color} en el tablero.")
        
      
        for row in self.__board__:
            for piece in row:
                if piece is not None and piece.get_color() != color:
                    if (king.row, king.col) in piece.get_moves(self.__board__):
                        return True
        return False

    def is_checkmate(self, color):
        """Verifica si el rey del color dado está en jaque mate."""
        if not self.is_check(color):
            return False

        
        return not self.can_escape_check(color)

    def can_escape_check(self, color):
        """Verifica si una pieza del color dado puede hacer un movimiento para escapar del jaque."""
        for row in range(8):
            for col in range(8):
                piece = self.__board__[row][col]
                if piece and piece.get_color() == color:
                    if self.can_piece_escape(piece, color):
                        return True
        return False

    def can_piece_escape(self, piece, color):
        """Verifica si una pieza puede moverse a una posición donde el rey no esté en jaque."""
        valid_moves = piece.get_moves(self.__board__)
        for move in valid_moves:
            temp_board = self.copy_board()
            temp_board.move_piece(piece, move[0], move[1])
            if not temp_board.is_check(color):
                return True
        return False

    def copy_board(self):
        """Crea una copia del tablero para verificar futuros movimientos."""
        new_board = Board()
        for row in range(8):
            for col in range(8):
                new_board.__board__[row][col] = self.__board__[row][col]
        return new_board
