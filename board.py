from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn


class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__pieces__ = []

    def place_piece(self, piece, row, col):
        """Coloca una pieza en una posición específica del tablero."""
        piece.move(row, col, self.board)  
        self.board[row][col] = piece  

    def add_piece(self, piece):
        """Agrega una pieza al tablero y actualiza la lista de piezas."""
        self.__pieces__.append(piece)
        self.__positions__[piece.row][piece.col] = piece

    def is_checkmate(self, color):
        """Determina si el rey del color dado está en jaque mate."""
        if not self.is_check(color):
            return False
        return self.no_legal_moves(color)

    def no_legal_moves(self, color):
        """Verifica si no hay movimientos legales para escapar del jaque."""
        king_position = self.find_king(color)
        if not king_position:
            return False

        for piece in self.get_pieces(color):
            if self.piece_has_legal_moves(piece):
                return False
        return True

    def piece_has_legal_moves(self, piece):
        """Verifica si una pieza tiene algún movimiento legal."""
        for move in piece.get_legal_moves(self):
            if not self.is_check_after_move(piece, move):
                return True
        return False

    def find_king(self, color):
        """Encuentra la posición del rey del color especificado."""
        for piece in self.__pieces__:
            if piece.__class__.__name__ == "King" and piece.__color__ == color:
                return (piece.row, piece.col)
        return None

    def is_check(self, color):
        """Determina si el rey del color especificado está en jaque."""
        king_position = self.find_king(color)
        if not king_position:
            return False
        return self.is_square_attacked(king_position, color)

    def is_check_after_move(self, piece, move):
        """Verifica si el rey del color de la pieza está en jaque después de un movimiento."""
        original_position = (piece.row, piece.col)
        target_piece = self.__positions__[move[0]][move[1]]

        self.__positions__[piece.row][piece.col] = None
        piece.row, piece.col = move
        self.__positions__[move[0]][move[1]] = piece

        check = self.is_check(piece.__color__)

        self.__positions__[piece.row][piece.col] = target_piece
        piece.row, piece.col = original_position
        if target_piece:
            self.__positions__[target_piece.row][target_piece.col] = target_piece

        return check

    def is_square_attacked(self, position, color):
        """Verifica si una casilla está siendo atacada por una pieza enemiga."""
        for piece in self.get_pieces(self.opposite_color(color)):
            if position in piece.get_legal_moves(self):
                return True
        return False

    def get_pieces(self, color):
        """Obtiene todas las piezas de un color específico en el tablero."""
        return [piece for piece in self.__pieces__ if piece.__color__ == color]

    def opposite_color(self, color):
        """Devuelve el color opuesto."""
        return "BLACK" if color == "WHITE" else "WHITE"

