import unittest
from board import Board
from pieces import SymbolPiece
from rook import Rook
from knight import Knight
from bishop import Bishop
from chess import Chess

class TestSymbolPiece(unittest.TestCase):
    def setUp(self):
        
        self.board = Board()
        self.white_piece = Rook("WHITE", 0, 0)
        self.black_piece = Rook("BLACK", 7, 7)
        self.board.__positions__[0][0] = self.white_piece
        self.board.__positions__[7][7] = self.black_piece

    def test_initial_position(self):
        
        self.assertEqual(self.board.get_piece(0, 0), self.white_piece)
        self.assertEqual(self.board.get_piece(7, 7), self.black_piece)

    def test_invalid_move(self):
        
        self.white_piece.move(8, 8, self.board.__positions__)
    
        self.assertEqual(self.board.get_piece(0, 0), self.white_piece)

    def test_move(self):
        
        self.white_piece.move(1, 0, self.board.__positions__)
        
        self.assertEqual(self.board.get_piece(1, 0), self.white_piece)
        self.assertEqual(self.board.get_piece(0, 0), None)

    def test_repr(self):
        
        self.assertEqual(repr(self.white_piece), 'RW')

    def test_str(self):
        
        self.assertEqual(str(self.white_piece), '♖')
        self.assertEqual(str(self.black_piece), '♜')

if __name__ == '__main__':
    unittest.main()

















#class TestRook(unittest.TestCase):

#    def test_str(self):
#        board = Board()
#        rook = Rook ("WHITE")
#        self.assertEqual(str(rook), "♜")

#    def test_str(self):
#        rook = Rook ("BLACK")
#        self.assertEqual(str(rook), "♖")















#class TestBoard(unittest.TestCase):


#    def test_initial_board_state(self):
        
#        expected_str = (
#            "♜♞♝  ♝♞♜\n"
#            "        \n"
#            "        \n"
#            "        \n"
#            "        \n"
#            "        \n"
#            "        \n"
#            "♖♘♗  ♗♘♖\n"
#        )
#        self.assertEqual(str(self.board), expected_str)

#    def test_get_piece(self):
#        
#        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
#        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
#        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
#        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
#        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
#        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        
#        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
#        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
#        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
#        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
#        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
#        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
#        
#        self.assertIsNone(self.board.get_piece(4, 4))  # Asumiendo una celda vacía

#    def test_empty_cell(self):
       
#        self.assertIsNone(self.board.get_piece(4, 4))
