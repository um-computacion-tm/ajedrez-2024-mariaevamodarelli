import unittest
from board import Board
from pieces import SymbolPiece, Piece 
from king import King
from rook import Rook
from queen import Queen
from knight import Knight
from pawn import Pawn
from bishop import Bishop

import unittest
from board import Board
from pieces import King, Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.white_king = King("WHITE", 7, 4)
        self.black_king = King("BLACK", 0, 4)
        self.white_rook = Rook("WHITE", 7, 0)
        self.black_rook = Rook("BLACK", 0, 0)
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_rook, 7, 0)
        self.board.place_piece(self.black_rook, 0, 0)

    def move_and_check(self, piece, dest_row, dest_col, check_function, *args):
        """Helper function to move a piece and check a condition."""
        self.board.move_piece(piece, dest_row, dest_col)
        check_function(*args)

    def test_is_check(self):
        """Prueba si el rey blanco está en jaque."""
        self.move_and_check(self.white_rook, 0, 0, self.assertTrue, self.board.is_check("BLACK"))

    def test_is_checkmate(self):
        """Prueba si el rey blanco está en jaque mate."""
        self.move_and_check(self.white_rook, 0, 0, self.assertTrue, self.board.is_checkmate("BLACK"))

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 8, 4)

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 9, 4)
