from chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):
    try:
        print(chess.show_board())
        print("Turn: ", chess.turn)

        
        from_row = input("From row (0-7): ")
        from_col = input("From col (0-7): ")
        to_row = input("To row (0-7): ")
        to_col = input("To col (0-7): ")

        
        if not (from_row.isdigit() and from_col.isdigit() and to_row.isdigit() and to_col.isdigit()):
            print("Error: Todas las entradas deben ser números enteros.")
            return

        
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)

        
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            print("Error: Row and column must be between 0 and 7.")
            return

        chess.move(from_row, from_col, to_row, to_col)

    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print("Error:", e)



if __name__ == '__main__':
    main()
