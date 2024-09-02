from pieces import SymbolPiece

class Rook(SymbolPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col, '♖', '♜')
    
    def get_moves(self, board):
        moves = []
        row, col = self.__row__, self.__column__
        # Moves horizontally
        for c in range(col + 1, 8):
            if board[row][c] is None:
                moves.append((row, c))
            else:
                if board[row][c].__color__ != self.__color__:
                    moves.append((row, c))
                break
        
        for c in range(col - 1, -1, -1):
            if board[row][c] is None:
                moves.append((row, c))
            else:
                if board[row][c].__color__ != self.__color__:
                    moves.append((row, c))
                break
        
        # Moves vertically
        for r in range(row + 1, 8):
            if board[r][col] is None:
                moves.append((r, col))
            else:
                if board[r][col].__color__ != self.__color__:
                    moves.append((r, col))
                break
        
        for r in range(row - 1, -1, -1):
            if board[r][col] is None:
                moves.append((r, col))
            else:
                if board[r][col].__color__ != self.__color__:
                    moves.append((r, col))
                break
        
        return moves
