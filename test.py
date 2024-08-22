#TEST CLI
#   import unittest
#from unittest.mock import patch
#from chess import Chess
#from cli import play
 


import unittest
from board import Board
from pieces import Piece 
from pieces import SymbolPiece
from rook import Rook
from knight import Knight


class TestBoard(unittest.TestCase):

    def setUp(self):
        """Set up the board for testing."""
        self.board = Board()

    def test_initial_board_state(self):
        """Test the initial state of the board with specific pieces."""
        expected_str = (
            "♜        ♖\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♖        ♜\n"
        )
        self.assertEqual(str(self.board), expected_str)

    def test_get_piece(self):
        """Test that the get_piece method returns the correct piece."""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
   

    def test_empty_cell(self):
        """Test that an empty cell returns None."""
        self.assertIsNone(self.board.get_piece(4, 4))

if __name__ == "__main__":
    unittest.main()







































#class TestCli(unittest.TestCase):
#    @patch(  
#        'builtins.input',
#        side_effect=['1', '1', '2', '2'], 
#    )
#    @patch('builtins.print') 
#    @patch.object(Chess, 'move')
#    def test_happy_path(
#        self,
#        mock_chess_move,
#        mock_print,
#        mock_input,
#    ): 
#        chess = Chess()
#        play(chess)
#        self.assertEqual(mock_input.call_count, 4)
#        self.assertEqual(mock_print.call_count, 2)
#        self.assertEqual(mock_chess_move.call_count, 1)
#unittest.main()
#    @patch(  
#        'builtins.input',
#        side_effect=['hola', '1', '2', '2'], 
#    )
#    @patch('builtins.print') 
#    @patch.object(Chess, 'move')
#    def test_not_happy_path(
#        self,
#        mock_chess_move,
#        mock_print,
#        mock_input,
#    ): 
#        chess = Chess()
#        play(chess)
#        self.assertEqual(mock_input.call_count, 1)
#        self.assertEqual(mock_print.call_count, 3)
#        self.assertEqual(mock_chess_move.call_count, 0)
#
#    @patch(  
#        'builtins.input',
#        side_effect=['1', '1', '2', 'hola'], 
#    )
#    @patch('builtins.print') 
#    @patch.object(Chess, 'move')
#    def test_more_not_happy_path(
#        self,
#        mock_chess_move,
#        mock_print,
#        mock_input,
#    ): 
#        chess = Chess()
#        play(chess)
#        self.assertEqual(mock_input.call_count, 4)
#        self.assertEqual(mock_print.call_count, 3)
#        self.assertEqual(mock_chess_move.call_count, 0)

#TESTBOARD
#import unittest
#from board import Board

#class TestBoard(unittest.TestCase):
#    def test_str_board(self):
#        board = Board()
#        self.assertEqual(
#            str(board),
#            (
#                "♖      ♖\n"
#                "        \n"
#                "        \n"
#                "        \n"
#                "        \n"
#                "        \n"
#                "        \n"
#                "♜      ♜\n"
#            )
#        )