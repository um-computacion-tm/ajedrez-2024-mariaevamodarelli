from pieces import SymbolPiece

class Bishop(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, '♗', '♝')

    def get_moves(self, board):
        moves = []
        directions = [
            (1, 1),  
            (-1, -1),  
            (1, -1),  
            (-1, 1)  
        ]

        for dr, dc in directions:
            r, c = self.__row__, self.__column__
            while True:
                r += dr
                c += dc
                if 0 <= r < 8 and 0 <= c < 8:
                    destination = board[r][c]
                    if destination is None:
                        moves.append((r, c))
                    elif destination.__color__ != self.__color__:
                        moves.append((r, c))
                        break  
                    else:
                        break  
                else:
                    break  

        return moves

    def move(self, dest_row, dest_col, board):
        if (dest_row, dest_col) in self.get_moves(board):
            board[dest_row][dest_col] = self
            board[self.__row__][self.__column__] = None
            self.__row__ = dest_row
            self.__column__ = dest_col
        else:
            print(f"Invalid move for {self}")
