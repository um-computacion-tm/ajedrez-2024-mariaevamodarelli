from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn

class Board:

    
    
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.turn = "WHITE"
        self.setup_pieces()

    def setup_pieces(self):
        # Posicionando piezas negras
        self.__positions__[0][0] = Rook("BLACK", 0, 0)
        self.__positions__[0][7] = Rook("BLACK", 0, 7)
        self.__positions__[0][1] = Knight("BLACK", 0, 1)
        self.__positions__[0][6] = Knight("BLACK", 0, 6)
        self.__positions__[0][2] = Bishop("BLACK", 0, 2)
        self.__positions__[0][5] = Bishop("BLACK", 0, 5)
        self.__positions__[0][3] = Queen("BLACK", 0, 3)
        self.__positions__[0][4] = King("BLACK", 0, 4)

        # Posicionando peones negros
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", 1, col)

        # Posicionando piezas blancas
        self.__positions__[7][7] = Rook("WHITE", 7, 7)
        self.__positions__[7][0] = Rook("WHITE", 7, 0)
        self.__positions__[7][1] = Knight("WHITE", 7, 1)
        self.__positions__[7][6] = Knight("WHITE", 7, 6)
        self.__positions__[7][2] = Bishop("WHITE", 7, 2)
        self.__positions__[7][5] = Bishop("WHITE", 7, 5)
        self.__positions__[7][3] = Queen("WHITE", 7, 3)
        self.__positions__[7][4] = King("WHITE", 7, 4)

        # Posicionando peones blancos
        for col in range(8):
            self.__positions__[6][col] = Pawn("WHITE", 6, col)

    def get_turn(self):
        
        return self.turn

    def switch_turn(self):
        
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                board_str += str(cell) if cell else " . "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.__positions__[row][col]
                if isinstance(piece, King) and piece.get_color() == color:
                    return (row, col)
        return None

    def is_check(self, color):
        king_position = self.find_king(color)
        if not king_position:
            return False
        opponent_color = "BLACK" if color == "WHITE" else "WHITE"
        for row in range(8):
            for col in range(8):
                piece = self.__positions__[row][col]
                if piece and piece.get_color() == opponent_color:
                    if king_position in piece.get_moves(self.__positions__):
                        return True
        return False

    def is_checkmate(self, color):
        if not self.is_check(color):
            return False

        king_position = self.find_king(color)
        if not king_position:
            return True

        for row in range(8):
            for col in range(8):
                piece = self.__positions__[row][col]
                if piece and piece.get_color() == color:
                    for move in piece.get_moves(self.__positions__):
                        target_piece = self.get_piece(*move)
                        self.move_piece(piece, *move)
                        if not self.is_check(color):
                            self.move_piece(piece, piece.get_row(), piece.get_column())
                            self.__positions__[move[0]][move[1]] = target_piece
                            return False
                        self.move_piece(piece, piece.get_row(), piece.get_column())
                        self.__positions__[move[0]][move[1]] = target_piece
        return True
    
    def move_piece(self, piece, row, col):
        # Verifica si es el turno correcto antes de mover
        if piece.get_color() != self.get_turn():
            raise ValueError("No es el turno de este jugador.")

        # Obtén la pieza que está en la posición destino
        target_piece = self.get_piece(row, col)

        # Verifica si hay una pieza del oponente en la posición de destino
        if target_piece and target_piece.get_color() == piece.get_color():
            raise ValueError("No puedes capturar tus propias piezas.")

        # Captura la pieza enemiga si está presente
        if target_piece and target_piece.get_color() != piece.get_color():
            self.__positions__[row][col] = None  # Remueve la pieza capturada

        # Mueve la pieza a la nueva posición
        self.__positions__[piece.get_row()][piece.get_column()] = None
        self.__positions__[row][col] = piece
        piece.move(row, col, self.__positions__)

        # Cambia el turno después del movimiento
        self.switch_turn()


