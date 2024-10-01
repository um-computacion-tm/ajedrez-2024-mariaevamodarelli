from pieces import Piece, SymbolPiece


class Rook(SymbolPiece):
    def __init__(self, color, x, y, white_symbol='♖', black_symbol='♜'):
        super().__init__(color, x, y, white_symbol, black_symbol)


    def get_moves(self, board):
        moves = []
        row, col = self.__row__, self.__column__

        
        def add_moves_in_direction(dr, dc):
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].__color__ != self.__color__:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc

        
        add_moves_in_direction(-1, 0)  
        add_moves_in_direction(1, 0)   
        add_moves_in_direction(0, -1)  
        add_moves_in_direction(0, 1)   

        return moves
