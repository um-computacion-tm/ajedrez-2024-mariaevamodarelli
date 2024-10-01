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
        self.black_rook = Rook("BLACK", 0, 0)
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_rook, 7, 0)
        self.board.place_piece(self.black_rook, 0, 0)

    def move_piece_and_assert(self, piece, dest_row, dest_col, assertion_func, expected_result, message):
        """Helper to move a piece and assert a condition."""
        self.board.move_piece(piece, dest_row, dest_col)
        assertion_func(expected_result, message)

    def test_check_conditions(self):
        """Test both check and checkmate conditions in one place."""
        scenarios = [
            (self.white_rook, 0, 0, self.assertTrue, self.board.is_check("BLACK"), "BLACK is in check"),
            (self.white_rook, 0, 0, self.assertTrue, self.board.is_checkmate("BLACK"), "BLACK is in checkmate")
        ]

        for piece, row, col, assert_func, result, msg in scenarios:
            with self.subTest(piece=piece, row=row, col=col, msg=msg):
                self.move_piece_and_assert(piece, row, col, assert_func, result, msg)

    def test_invalid_moves(self):
        """Test invalid movements for pieces."""
        scenarios = [
            (self.white_king, 8, 4, ValueError, "Invalid move for white king out of board"),
            (self.white_king, 9, 4, ValueError, "Move out of bounds")
        ]

        for piece, row, col, error, msg in scenarios:
            with self.subTest(piece=piece, row=row, col=col, msg=msg):
                with self.assertRaises(error, msg=msg):
                    self.board.move_piece(piece, row, col)


if __name__ == "__main__":
    unittest.main()
