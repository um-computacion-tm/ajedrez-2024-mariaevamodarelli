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
        self.white_king = King("WHITE")
        self.black_king = King("BLACK")
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 8, 4)  

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque."""
        self.assertFalse(self.board.is_check("WHITE"))

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 9, 4)  

    def test_move_piece(self):
        """Prueba el movimiento de piezas."""
        self.board.move_piece(self.white_king, 6, 4)
        self.assertEqual(self.board.__board__[6][4], self.white_king)
        self.assertIsNone(self.board.__board__[7][4])

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza."""
        moves = self.white_king.get_moves(self.board.__board__)
        self.assertIn((6, 4), moves)

if __name__ == "__main__":
    unittest.main()
