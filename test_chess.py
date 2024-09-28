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
        """Prepara el tablero y las piezas antes de cada prueba."""
        self.board = Board()
        self.white_king = King("white", 7, 4, "♔", "♚")
        self.black_king = King("black", 0, 4, "♔", "♚")
        self.white_rook = Rook("white", 7, 7, "♖", "♜")
        self.black_bishop = Bishop("black", 0, 2, "♗", "♝")

        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_rook, 7, 7)
        self.board.place_piece(self.black_bishop, 0, 2)

    def assert_invalid_move(self, piece, row, col):
        """Auxiliar para verificar movimientos inválidos o fuera del tablero."""
        with self.assertRaises(ValueError):
            self.board.move_piece(piece, row, col)

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        self.assert_invalid_move(self.white_king, 8, 4)

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        self.assert_invalid_move(self.white_king, 9, 4)

    def test_move_piece(self):
        """Prueba el movimiento de una pieza a una posición válida."""
        self.board.move_piece(self.white_rook, 7, 5)
        self.assertEqual(self.board.get_piece(7, 5), self.white_rook)
        self.assertIsNone(self.board.get_piece(7, 7))

    def test_is_check(self):
        """Prueba si el rey blanco está en jaque."""
        self.board.move_piece(self.black_bishop, 5, 6)  
        self.assertTrue(self.board.is_check("white"))

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque."""
        self.assertFalse(self.board.is_check("white"))

    def test_is_checkmate(self):
        """Prueba si el rey blanco está en jaque mate."""
        self.board.move_piece(self.black_bishop, 1, 5)
        self.board.move_piece(self.black_bishop, 2, 4)  
        self.assertTrue(self.board.is_checkmate("white"))

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza."""
        moves = self.white_king.get_valid_moves(self.board)
        expected_moves = [(6, 4), (6, 5), (7, 5)]
        self.assertCountEqual(moves, expected_moves)


if __name__ == "__main__":
    unittest.main()
