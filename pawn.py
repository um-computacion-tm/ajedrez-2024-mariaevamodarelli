from pieces import SymbolPiece


class Pawn(SymbolPiece):
    def __init__(self, color, x, y, white_symbol='♙', black_symbol='♟'):
        super().__init__(color, x, y, white_symbol, black_symbol)

    def get_moves(self, board):
        moves = []
        direction = -1 if self.__color__ == "WHITE" else 1
        start_row = 6 if self.__color__ == "WHITE" else 1
        
        
        forward_row = self.__row__ + direction
        if 0 <= forward_row < 8 and board[forward_row][self.__column__] is None:
            moves.append((forward_row, self.__column__))
            
            if self.__row__ == start_row:
                double_forward_row = self.__row__ + 2 * direction
                if board[double_forward_row][self.__column__] is None:
                    moves.append((double_forward_row, self.__column__))

        
        for dc in [-1, 1]:
            capture_row = self.__row__ + direction
            capture_col = self.__column__ + dc
            if 0 <= capture_row < 8 and 0 <= capture_col < 8:
                target_piece = board[capture_row][capture_col]
                if target_piece is not None and target_piece.__color__ != self.__color__:
                    moves.append((capture_row, capture_col))

        return moves
