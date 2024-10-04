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
        self.white_rook = Rook("WHITE", 0, 0)
        self.black_king = King("BLACK", 7, 4)
        self.white_king = King("WHITE", 0, 4)
        
        # Colocar las piezas en el tablero
        self.board.place_piece(self.white_rook, 0, 0)
        self.board.place_piece(self.white_king, 0, 4)
        self.board.place_piece(self.black_king, 7, 4)

    def test_place_piece(self):
        """Test para verificar que se coloca correctamente una pieza."""
        piece = self.board._Board__board[0][0]
        self.assertEqual(piece, self.white_rook)
    
    def test_move_piece_valid(self):
        """Test para un movimiento válido de una pieza."""
        self.board.move_piece(self.white_rook, 0, 3)
        self.assertEqual(self.board._Board__board[0][3], self.white_rook)
        self.assertIsNone(self.board._Board__board[0][0])

    def test_move_piece_invalid(self):
        """Test para un movimiento inválido de una pieza."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_rook, 7, 7)

    def test_is_check(self):
        """Test para verificar si el rey está en jaque."""
        self.board.move_piece(self.white_rook, 7, 4)  # Coloca la torre en posición de jaque
        self.assertTrue(self.board.is_check("BLACK"))

    def test_is_not_check(self):
        """Test para verificar que el rey no está en jaque."""
        self.assertFalse(self.board.is_check("BLACK"))

    def test_is_checkmate(self):
        """Test para verificar si el rey está en jaque mate."""
        self.board.move_piece(self.white_rook, 7, 3)  # Coloca la torre cerca del rey negro
        self.assertTrue(self.board.is_checkmate("BLACK"))

    def test_is_not_checkmate(self):
        """Test para verificar que el rey no está en jaque mate."""
        self.assertFalse(self.board.is_checkmate("BLACK"))

    def test_copy_board(self):
        """Test para verificar la copia del tablero."""
        new_board = self.board.copy_board()
        self.assertEqual(new_board._Board__board[0][0], self.white_rook)
        self.assertEqual(new_board._Board__board[7][4], self.black_king)
        self.assertNotEqual(id(new_board), id(self.board))  # Asegura que son instancias diferentes

if __name__ == "__main__":
    unittest.main()
