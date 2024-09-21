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

        
        self.white_king = SymbolPiece("WHITE", 7, 4, "♔", "♚")
        self.black_king = SymbolPiece("BLACK", 0, 4, "♔", "♚")
        self.white_rook = SymbolPiece("WHITE", 7, 0, "♖", "♜")
        self.black_rook = SymbolPiece("BLACK", 0, 0, "♖", "♜")

        
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_rook, 7, 0)
        self.board.place_piece(self.black_rook, 0, 0)

    def test_move_piece(self):
        """Prueba el movimiento de piezas"""
        self.board.move_piece(self.white_rook, 7, 1)
        self.assertEqual(self.board.get_piece(7, 1), self.white_rook)
        self.assertIsNone(self.board.get_piece(7, 0))

    def test_is_check(self):
        """Prueba si el rey está en jaque"""
        self.board.move_piece(self.black_rook, 7, 1)
        self.assertTrue(self.board.is_check('white'))

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque"""
        self.assertFalse(self.board.is_check('white'))

    def test_is_checkmate(self):
        """Prueba si un jugador está en jaque mate"""
        self.board.move_piece(self.black_rook, 7, 1)  
        self.assertTrue(self.board.is_checkmate('white'))

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza"""
        valid_moves = self.white_rook.get_moves(self.board)
        expected_moves = [(7, 1), (7, 2), (7, 3)]
        self.assertEqual(valid_moves, expected_moves)

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza"""
        self.assertFalse(self.white_king.is_valid_move(6, 6, self.board))

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero"""
        self.assertFalse(self.white_king.is_valid_move(-1, 4, self.board))
        self.assertFalse(self.white_king.is_valid_move(8, 4, self.board))

if __name__ == "__main__":
    unittest.main()
