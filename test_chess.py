import unittest
from board import Board
from pieces import SymbolPiece, Piece 
from king import King
from rook import Rook
from queen import Queen
from knight import Knight
from pawn import Pawn
from bishop import Bishop





class ChessTestBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_king = King("white")
        self.black_king = King("black")

    def assert_invalid_move(self, piece, row, col):
        """Auxiliar para probar movimientos inválidos."""
        with self.assertRaises(ValueError):
            self.board.move_piece(piece, row, col)


class TestBoard(ChessTestBase):
    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        self.assert_invalid_move(self.white_king, 8, 4)

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        self.assert_invalid_move(self.white_king, 9, 4)

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque."""
        self.board.place_piece(self.white_king, 7, 4)
        self.assertFalse(self.board.is_check("white"))

    def test_is_checkmate(self):
        """Prueba si el rey está en jaque mate."""
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 6, 4)  
        self.assertTrue(self.board.is_checkmate("white"))

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza."""
        self.board.place_piece(self.white_king, 7, 4)
        valid_moves = self.white_king.get_moves(self.board.__board__)
        self.assertIn((6, 4), valid_moves)

    def test_move_piece(self):
        """Prueba el movimiento de piezas."""
        self.board.place_piece(self.white_king, 7, 4)
        self.board.move_piece(self.white_king, 6, 4)  
        self.assertIsNone(self.board.__board__[7][4])
        self.assertEqual(self.board.__board__[6][4], self.white_king)
