import unittest
from board import Board
from pieces import SymbolPiece, Piece 
from king import King
from rook import Rook
from queen import Queen
from knight import Knight
from pawn import Pawn
from bishop import Bishop



class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.white_rook = Rook("WHITE", 0, 0)
        self.black_king = King("BLACK", 7, 4)
        self.board.place_piece(self.white_rook, 0, 0)
        self.board.place_piece(self.black_king, 7, 4)

    def move_and_check(self, piece, row, col, check_method, *args):
        """Mueve una pieza y verifica una condición en el tablero."""
        self.board.move_piece(piece, row, col)
        check_method(*args)

    def test_is_check(self):
        """Test para verificar si el rey está en jaque."""
        self.move_and_check(self.white_rook, 7, 4, self.assertTrue, self.board.is_check("BLACK"))

    def test_is_checkmate(self):
        """Test para verificar si el rey está en jaque mate."""
        self.move_and_check(self.white_rook, 7, 3, self.assertTrue, self.board.is_checkmate("BLACK"))

    def test_invalid_move(self):
        """Test para un movimiento inválido."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_rook, 8, 4)  
            
    def test_move_out_of_bounds(self):
        """Test para mover una pieza fuera de los límites."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_rook, 9, 4)  


if __name__ == "__main__":
    unittest.main()
