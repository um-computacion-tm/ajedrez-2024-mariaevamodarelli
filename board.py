from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
from pieces import Piece, SymbolPiece




class Board:
    def __init__(self):
        """Inicializa el tablero de ajedrez como una matriz 8x8 vacía."""
        self.__board__ = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        """Coloca una pieza en una posición específica del tablero."""
        piece.move(row, col, self.__board__)  
        self.__board__[row][col] = piece      

    def move_piece(self, piece, dest_row, dest_col):
        """Mueve una pieza a una nueva posición si el movimiento es válido."""
        if piece.is_valid_move(dest_row, dest_col, self.__board__):
            
            self.__board__[piece.get_row()][piece.get_column()] = None
            
            self.__board__[dest_row][dest_col] = piece
            
            piece.move(dest_row, dest_col, self.__board__)
        else:
            raise ValueError(f"Movimiento inválido para {piece}")

    def is_check(self, color):
        """Verifica si el rey del color dado está en jaque."""
        king = self.find_king(color)
        enemy_color = "WHITE" if color == "BLACK" else "BLACK"
        
        
        for row in range(8):
            for col in range(8):
                piece = self.__board__[row][col]
                if piece and piece.get_color() == enemy_color:
                    if piece.is_valid_move(king.get_row(), king.get_column(), self.__board__):
                        return True
        return False

    def is_checkmate(self, color):
        """Verifica si el rey del color dado está en jaque mate."""
        if not self.is_check(color):
            return False

        
        for row in range(8):
            for col in range(8):
                piece = self.__board__[row][col]
                if piece and piece.get_color() == color:
                    valid_moves = piece.get_moves(self.__board__)
                    for move in valid_moves:
                        temp_board = self.copy_board()
                        temp_board.move_piece(piece, move[0], move[1])
                        if not temp_board.is_check(color):
                            return False
        return True

    def find_king(self, color):
        """Encuentra y devuelve el rey del color dado."""
        for row in range(8):
            for col in range(8):
                piece = self.__board__[row][col]
                if piece and piece.get_color() == color and isinstance(piece, SymbolPiece) and str(piece) in ["♔", "♚"]:
                    return piece
        raise ValueError(f"No se encontró el rey de color {color}")

    def copy_board(self):
        """Devuelve una copia del tablero actual para simulaciones."""
        new_board = Board()
        for row in range(8):
            for col in range(8):
                piece = self.__board__[row][col]
                if piece:
                    new_board.place_piece(piece, row, col)
        return new_board

    def print_board(self):
        """Imprime el estado actual del tablero."""
        for row in range(8):
            print([str(piece) if piece else '.' for piece in self.__board__])








