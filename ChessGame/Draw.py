from Chess import *


def draw_field(field: list):
    for y in range(0, 8):
        for x in range(0, 8):
            if isinstance(field[x][y], Pawn) and field[x][y]._color == Color.WHITE:
                print(white_pieces[Pawn], end='')
            elif isinstance(field[x][y], Pawn) and field[x][y]._color == Color.BLACK:
                print(black_pieces[Pawn], end='')
            else:
                print(empty_field, end='')
        print()


empty_field = '🈴'

white_pieces = {Pawn: "♙"}
black_pieces = {Pawn: "♟"}
