import unittest
from board import Board
from pieces import SymbolPiece, Piece 
from king import King
from rook import Rook
from queen import Queen
from knight import Knight
from pawn import Pawn


class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Crea un tablero y algunas piezas para las pruebas."""
        self.board = Board()
        self.white_king = King(7, 4, 'white')
        self.black_king = King(0, 4, 'black')
        self.white_rook = Rook(7, 0, 'white')
        self.black_rook = Rook(0, 0, 'black')
        self.white_pawn = Pawn(6, 4, 'white')
        self.black_pawn = Pawn(1, 4, 'black')
        self.board.place_piece(self.white_king)
        self.board.place_piece(self.black_king)
        self.board.place_piece(self.white_rook)
        self.board.place_piece(self.black_rook)
        self.board.place_piece(self.white_pawn)
        self.board.place_piece(self.black_pawn)

    def test_place_piece(self):
        """Prueba que las piezas se coloquen correctamente en el tablero."""
        self.assertEqual(self.board.get_piece(7, 4), self.white_king)
        self.assertEqual(self.board.get_piece(0, 4), self.black_king)

    def test_move_piece(self):
        """Prueba mover una pieza a una posición válida."""
        self.board.move_piece(self.white_pawn, 5, 4)
        self.assertEqual(self.board.get_piece(5, 4), self.white_pawn)
        self.assertIsNone(self.board.get_piece(6, 4))

    def test_invalid_move(self):
        """Prueba mover una pieza a una posición inválida."""
        with self.assertRaises(ValueError):
            self.board.move_piece(self.white_pawn, 8, 4)  

    def test_is_check(self):
        """Prueba si el rey está en jaque."""
        
        self.board.move_piece(self.black_rook, 7, 1)
        self.assertTrue(self.board.is_check('white'))

    def test_is_checkmate(self):
        """Prueba si un jugador está en jaque mate."""
        
        self.board.move_piece(self.black_rook, 7, 1)  
        self.assertTrue(self.board.is_checkmate('white'))

    def test_no_checkmate(self):
        """Prueba que no hay jaque mate cuando es posible salir del jaque."""
        self.board.move_piece(self.black_rook, 7, 1)  
        self.board.move_piece(self.white_king, 7, 3)  
        self.assertFalse(self.board.is_checkmate('white'))

    def test_is_stalemate(self):
        """Prueba si el juego está en tablas (stalemate)."""
        self.board.clear_board()
        self.board.place_piece(self.white_king)
        self.board.place_piece(King(5, 5, 'black'))
        self.board.place_piece(Rook(7, 7, 'black'))
        self.assertTrue(self.board.is_stalemate('white'))

    def test_pawn_promotion(self):
        """Prueba la promoción del peón."""
        self.board.move_piece(self.white_pawn, 0, 4)  
        self.board.promote_pawn(self.white_pawn, Queen(0, 4, 'white'))  
        self.assertIsInstance(self.board.get_piece(0, 4), Queen)

    def test_en_passant(self):
        """Prueba la captura al paso (en passant)."""
        
        self.board.move_piece(self.black_pawn, 3, 4)  
        self.board.move_piece(self.white_pawn, 4, 3)  
        self.board.en_passant(self.white_pawn, (3, 4))  
        self.assertIsNone(self.board.get_piece(3, 4))  
        self.assertEqual(self.board.get_piece(3, 3), self.white_pawn)  

if __name__ == '__main__':
    unittest.main()
