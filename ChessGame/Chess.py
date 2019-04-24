from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Chess:

    def __init__(self):
        self._field = [[0 for x in range(8)] for y in range(8)]
        self.place_piece()

    def place_piece(self):
        self.place_pawns()

    def place_pawns(self):
        for y in range(len(self._field)):
            for x in range(len(self._field)):
                if y == 0 or y == 1:
                    self._field[x][y] = Pawn(Color.BLACK, self._field)
                if y == 6 or y == 7:
                    self._field[x][y] = Pawn(Color.WHITE, self._field)


class Piece:
    def __init__(self,color: Color, game_board: list):
        if game_board is None or color is None:
            raise ValueError
        self._game_board = game_board
        self._color = color

    def available_moves(self, x, y):
        print('Not available in base class')

    def valid_turn(self, x, y):
        return self.in_board(x, y) and self.same_color(x, y) is False

    def same_color(self, x, y):
        return self._game_board[x][y] != 0 and self._game_board[x][y]._color == self._color

    def in_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8


class Pawn(Piece):

    def available_moves(self, x, y):
        moves = []
        if self.valid_turn(x, y+self.get_direction()): moves.append((x, y+self.get_direction()))
        if self.valid_turn(x+1, y+self.get_direction()): moves.append((x+1, y + self.get_direction()))
        if self.valid_turn(x-1, y+self.get_direction()): moves.append((x-1, y + self.get_direction()))
        return moves

    def get_direction(self):
        if self._color == Color.WHITE:
            return -1
        else:  # black
            return 1


