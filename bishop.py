from pieces import Piece


class Bishop(Piece):
     def __init__(self, color, row, col):
        super().__init__(color, row, col, "♝", "♗")
    