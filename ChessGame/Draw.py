from Chess import *


def draw_field(field: list):
    for y in range(0, 8):
        for x in range(0, 8):
            if field[x][y] != 0:
                print(pawn_figure, end='')
            else:
                print(empty_field, end='')
        print()


pawn_figure = '♙'
empty_field = '🈴'