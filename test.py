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

    def test_place_piece(self):
        """Test placing a piece on the board."""
        rook = Rook("WHITE", 0, 0)
        self.board.place_piece(rook)
        self.assertEqual(self.board.get_piece(0, 0), rook)

    def test_move_piece(self):
        """Test moving a piece on the board."""
        rook = Rook("WHITE", 0, 0)
        self.board.place_piece(rook)
        self.board.move_piece(rook, 0, 3)
        self.assertEqual(self.board.get_piece(0, 3), rook)
        self.assertIsNone(self.board.get_piece(0, 0))

  
    def test_blocked_moves(self):
        """Test if a piece cannot move when blocked."""
        white_rook = Rook("WHITE", 0, 0)
        white_knight = Knight("WHITE", 0, 1)
        self.board.place_piece(white_rook)
        self.board.place_piece(white_knight)

        self.assertNotIn((0, 1), white_rook.get_moves(self.board.board))

    def test_clear_path(self):
        """Test if a piece can move when there's no obstacle in its path."""
        white_rook = Rook("WHITE", 0, 0)
        black_bishop = Bishop("BLACK", 4, 4)
        self.board.place_piece(white_rook)
        self.board.place_piece(black_bishop)

        moves = white_rook.get_moves(self.board.board)
        self.assertIn((0, 7), moves)
        self.assertNotIn((4, 4), moves)  # Bishop blocks the move

if __name__ == "__main__":
    unittest.main()


