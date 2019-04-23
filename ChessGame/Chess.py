from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Chess:

    def __init__(self):
        self._field = [[0 for x in range(8)] for y in range(8)]
        self.place_piece()

    def place_piece(self):
        for y in range(len(self._field)):
            for x in range(len(self._field)):
                if y == 0 or y == 1:
                    self._field[x][y] = Pawn(Color.WHITE)
                if y == 6 or y == 7:
                    self._field[x][y] = Pawn(Color.BLACK)


class Pawn:
    def __init__(self, color: Color):
        self._color = color


        

