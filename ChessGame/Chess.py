from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Chess:

    def __init__(self):
        self._field = [[0 for x in range(8)] for y in range(8)]
        self.place_piece()

    def place_piece(self):
        for x in range(len(self._field)):
            for y in range(len(self._field)):
                if x == 0 or x == 1 or x == 6 or x == 7:
                    self._field[x][y] = Pawn(Color.WHITE)


class Pawn:
    def __init__(self, color: Color):
        self.__player = color


        

