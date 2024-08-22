
import unittest
from board import Board
from rook import Rook
from knight import Knight
from bishop import Bishop



class TestBoard(unittest.TestCase):

    def setUp(self):
        """Configura el tablero para las pruebas."""
        self.board = Board()

    def test_initial_board_state(self):
        """Prueba el estado inicial del tablero con las piezas específicas."""
        expected_str = (
            "♜♞♝  ♝♞♜\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♖♘♗  ♗♘♖\n"
        )
        self.assertEqual(str(self.board), expected_str)

    def test_get_piece(self):
        """Prueba que el método get_piece devuelve la pieza correcta."""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        
        self.assertIsNone(self.board.get_piece(4, 4))  # Asumiendo una celda vacía

    def test_empty_cell(self):
        """Prueba que una celda vacía devuelve None."""
        self.assertIsNone(self.board.get_piece(4, 4))

if __name__ == "__main__":
    unittest.main()
