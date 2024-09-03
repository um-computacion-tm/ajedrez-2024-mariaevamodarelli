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

#test caballo 



class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_knight = Knight("WHITE", 1, 0)
        self.black_knight = Knight("BLACK", 6, 5)
        self.board.__positions__[1][0] = self.white_knight
        self.board.__positions__[6][5] = self.black_knight

    def test_initial_position(self):
        self.assertEqual(self.board.get_piece(1, 0), self.white_knight)
        self.assertEqual(self.board.get_piece(6, 5), self.black_knight)

    def test_invalid_move(self):
        
        self.white_knight.move(8, 8, self.board.__positions__)
        self.assertEqual(self.board.get_piece(1, 0), self.white_knight)

    def test_valid_moves(self):
        valid_moves = self.white_knight.get_moves(self.board.__positions__)
        
        expected_moves = [(3, 1), (2, 2)]  
        self.assertTrue(set(expected_moves).issubset(set(valid_moves)))

    def test_move(self):
        
        self.white_knight.move(3, 1, self.board.__positions__)
        self.assertEqual(self.board.get_piece(3, 1), self.white_knight)
        self.assertEqual(self.board.get_piece(1, 0), None)

    def test_repr(self):
        self.assertEqual(repr(self.white_knight), 'KW')

    def test_str(self):
        self.assertEqual(str(self.white_knight), '♘')
        self.assertEqual(str(self.black_knight), '♞')




if __name__ == '__main__':
    unittest.main()