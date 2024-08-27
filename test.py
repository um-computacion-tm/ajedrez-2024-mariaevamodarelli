
import unittest
from board import Board
from rook import Rook
from knight import Knight
from bishop import Bishop



class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook ("WHITE")
        self.assertEqual(str(rook), "♜")

#    def test_str(self):
#        rook = Rook ("BLACK")
#        self.assertEqual(str(rook), "♖")

if __name__ == "__main__":
     unittest.main()
















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
