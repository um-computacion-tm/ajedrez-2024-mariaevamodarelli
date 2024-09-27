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
        """Configura un tablero inicial para las pruebas."""
        self.board = Board()
        
        self.white_king = King(7, 4, "♔", "♚", "white")
        self.black_king = King(0, 4, "♔", "♚", "black")
        self.white_queen = Queen(7, 3, "♕", "♛", "white")
        self.black_queen = Queen(0, 3, "♕", "♛", "black")

    def test_invalid_move(self):
        """Prueba un movimiento inválido para una pieza."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 8, 4)  

    def test_is_checkmate(self):
        """Prueba si el rey está en jaque mate."""
        self.board.place_piece(self.black_king, 0, 4)
        self.board.place_piece(self.white_queen, 1, 4)
        self.board.place_piece(self.white_king, 7, 4)
        self.assertTrue(self.board.is_checkmate("black"))

    def test_is_not_check(self):
        """Prueba si el rey no está en jaque."""
        self.board.place_piece(self.white_king, 7, 4)
        self.board.place_piece(self.black_king, 0, 4)
        self.assertFalse(self.board.is_check("white"))

    def test_move_out_of_bounds(self):
        """Prueba que una pieza no se puede mover fuera del tablero."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_king, 9, 4)  

    def test_move_piece(self):
        """Prueba el movimiento de piezas."""
        self.board.place_piece(self.white_king, 7, 4)
        self.board.move_piece(self.white_king, 6, 4)  
        self.assertEqual(self.white_king.row, 6)
        self.assertEqual(self.white_king.col, 4)

    def test_valid_moves(self):
        """Prueba obtener movimientos válidos para una pieza."""
        self.board.place_piece(self.white_queen, 7, 3)
        valid_moves = self.white_queen.get_moves(self.board)
        self.assertIn((6, 3), valid_moves)
        self.assertIn((7, 4), valid_moves)

if __name__ == "__main__":
    unittest.main()
