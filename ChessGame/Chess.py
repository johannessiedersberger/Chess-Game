from enum import Enum


class Player(Enum):
    PLAYER1 = 1
    PLayer2 = 2


class Chess:

    def __init__(self):
        self._field = [8][8]
        self.positionPawns()

    def position_pawns(self):
        for x in range(len(self._field)):
            for y in range(len(self._field)):
                if x == 1:
                    self._field[x, y] = Pawn(Player.PLAYER1)
                if x == 7:
                    self._field[x, y] = Pawn(Player.PLayer2)


class Pawn:
    def __init__(self, player: Player):
        self._player = player

