import unittest
from board import Board
from pieces import SymbolPiece
from rook import Rook
from knight import Knight
from bishop import Bishop
from chess import Chess
from queen import Queen
from king import King
from pawn import Pawn

    #test torre
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

    #test reina

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_queen = Queen("WHITE", 0, 3)
        self.black_queen = Queen("BLACK", 7, 3)
        self.board.__positions__[0][3] = self.white_queen
        self.board.__positions__[7][3] = self.black_queen

    def test_initial_position(self):
        self.assertEqual(self.board.get_piece(0, 3), self.white_queen)
        self.assertEqual(self.board.get_piece(7, 3), self.black_queen)

    def test_invalid_move(self):
        self.white_queen.move(8, 3, self.board.__positions__)
        self.assertEqual(self.board.get_piece(0, 3), self.white_queen)


    def test_repr(self):
        self.assertEqual(repr(self.white_queen), 'QW')

    def test_str(self):
        self.assertEqual(str(self.white_queen), '♕')
        self.assertEqual(str(self.black_queen), '♛')




    #test rey 

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_king = King("WHITE", 0, 4)
        self.black_king = King("BLACK", 7, 4)
        self.board.__positions__[0][4] = self.white_king
        self.board.__positions__[7][4] = self.black_king

    def test_initial_position(self):
        self.assertEqual(self.board.get_piece(0, 4), self.white_king)
        self.assertEqual(self.board.get_piece(7, 4), self.black_king)

    def test_invalid_move(self):
        self.white_king.move(8, 4, self.board.__positions__)
        self.assertEqual(self.board.get_piece(0, 4), self.white_king)

    def test_valid_moves(self):
        valid_moves = self.white_king.get_moves(self.board.__positions__)
        expected_moves = [
            (0, 3), (0, 5), (1, 3), (1, 4), (1, 5)
        ]
        self.assertTrue(set(expected_moves).issubset(set(valid_moves)))

    def test_move(self):
        self.white_king.move(1, 4, self.board.__positions__)
        self.assertEqual(self.board.get_piece(1, 4), self.white_king)
        self.assertEqual(self.board.get_piece(0, 4), None)

    def test_repr(self):
        self.assertEqual(repr(self.white_king), 'KW')

    def test_str(self):
        self.assertEqual(str(self.white_king), '♔')
        self.assertEqual(str(self.black_king), '♚')

#test alfil

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_bishop = Bishop("WHITE", 4, 4)
        self.board.__positions__[4][4] = self.white_bishop

    def test_initial_position(self):
        self.assertEqual(self.board.get_piece(4, 4), self.white_bishop)

    def test_invalid_move(self):
        
        self.white_bishop.move(7, 7, self.board.__positions__)
        self.assertEqual(self.board.get_piece(4, 4), self.white_bishop)


    def test_move(self):
        self.white_bishop.move(5, 5, self.board.__positions__)
        self.assertEqual(self.board.get_piece(5, 5), self.white_bishop)
        self.assertEqual(self.board.get_piece(4, 4), None)

    def test_repr(self):
        self.assertEqual(repr(self.white_bishop), 'BW')

    def test_str(self):
        self.assertEqual(str(self.white_bishop), '♗')


#test peon 
 

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        
        self.white_pawn = Pawn("WHITE", 6, 4)
        self.black_pawn = Pawn("BLACK", 1, 4)
        
        self.board.__positions__[6][4] = self.white_pawn
        self.board.__positions__[1][4] = self.black_pawn

    def test_initial_position(self):
        
        self.assertEqual(self.board.get_piece(6, 4), self.white_pawn)
        self.assertEqual(self.board.get_piece(1, 4), self.black_pawn)

    def test_invalid_move(self):
        
        self.white_pawn.move(8, 4, self.board.__positions__)
        
        self.assertEqual(self.board.get_piece(6, 4), self.white_pawn)

    def test_valid_moves_white(self):
        
        valid_moves = self.white_pawn.get_moves(self.board.__positions__)
        expected_moves = [(5, 4), (4, 4)]  
        self.assertTrue(set(expected_moves).issubset(set(valid_moves)))

    def test_valid_moves_black(self):
        
        valid_moves = self.black_pawn.get_moves(self.board.__positions__)
        expected_moves = [(2, 4), (3, 4)]  
        self.assertTrue(set(expected_moves).issubset(set(valid_moves)))

    def test_move(self):
        
        self.white_pawn.move(5, 4, self.board.__positions__)
        
        self.assertEqual(self.board.get_piece(5, 4), self.white_pawn)
        self.assertEqual(self.board.get_piece(6, 4), None)

    def test_repr(self):
        
        self.assertEqual(repr(self.white_pawn), 'PW')
        self.assertEqual(repr(self.black_pawn), 'PB')

    def test_str(self):
        
        self.assertEqual(str(self.white_pawn), '♙')
        self.assertEqual(str(self.black_pawn), '♟')

#testjaquemate
import unittest
from board import Board
from king import King
from rook import Rook

class TestCheckAndCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_king = King("WHITE", 0, 4)
        self.black_king = King("BLACK", 7, 4)
        self.white_rook = Rook("WHITE", 1, 4)
        self.black_rook = Rook("BLACK", 6, 4)
        self.board.__positions__[0][4] = self.white_king
        self.board.__positions__[7][4] = self.black_king
        self.board.__positions__[1][4] = self.white_rook
        self.board.__positions__[6][4] = self.black_rook

    def test_is_check(self):
        # Mueve la torre negra para poner al rey blanco en jaque
        self.board.__positions__[1][4] = None
        self.board.__positions__[5][4] = self.black_rook
        self.assertTrue(self.board.is_check("WHITE"))







if __name__ == '__main__':
    unittest.main()
