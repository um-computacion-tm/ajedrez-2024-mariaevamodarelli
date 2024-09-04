from pieces import SymbolPiece

class King(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, '♔', '♚')

    def get_moves(self, board):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        for dr, dc in directions:
            new_row = self.__row__ + dr
            new_col = self.__column__ + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                destination = board[new_row][new_col]
                if destination is None or destination.__color__ != self.__color__:
                    moves.append((new_row, new_col))
        return moves

    def move(self, dest_row, dest_col, board):
        if (dest_row, dest_col) in self.get_moves(board):
            board[dest_row][dest_col] = self
            board[self.__row__][self.__column__] = None
            self.__row__ = dest_row
            self.__column__ = dest_col
        else:
            print(f"Invalid move for {self}")
