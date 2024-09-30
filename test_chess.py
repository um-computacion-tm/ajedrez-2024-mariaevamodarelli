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

        self.white_king = King("WHITE", 7, 4)
        self.black_king = King("BLACK", 0, 4)
        self.white_rook = Rook("WHITE", 7, 0)
        self.black_bishop = Bishop("BLACK", 0, 2)

        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_rook, 7, 0)
        self.board.place_piece(self.black_bishop, 0, 2)

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 8, 4)  

    def test_is_check(self):
        """Prueba si el rey blanco está en jaque."""
        self.board.move_piece(self.white_rook, 0, 0)
        self.assertTrue(self.board.is_check("BLACK"))

    def test_is_checkmate(self):
        """Prueba si el rey blanco está en jaque mate."""
        self.board.move_piece(self.white_rook, 0, 0)
        self.assertTrue(self.board.is_checkmate("BLACK"))

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque."""
        self.assertFalse(self.board.is_check("WHITE"))

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 9, 4)  

    def test_move_piece(self):
        """Prueba el movimiento de una pieza a una posición válida."""
        self.board.move_piece(self.white_king, 6, 4)  
        self.assertEqual(self.board.get_piece(6, 4), self.white_king)

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza."""
        valid_moves = self.white_rook.get_moves(self.board)
        expected_moves = [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]  
        self.assertEqual(valid_moves, expected_moves)

if __name__ == "__main__":
    unittest.main()
