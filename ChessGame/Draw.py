from Chess import *


def draw_field(field: list):
    for y in range(0, 8):
        for x in range(0, 8):
            if field[x, y] == type(Pawn):
                print(pawnFigure)


pawnFigure = "♙"
