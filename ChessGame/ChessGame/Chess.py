from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1

class FieldState(Enum):
    WHITE_PIECE = 0
    BLACK_PIECE = 1
    EMTPTY = 2


class Chess:

    def __init__(self):
        self._field = [[0 for x in range(8)] for y in range(8)]
        self._place_piece()

    def _place_piece(self):
        self._place_pawns()

    def _place_pawns(self):
        for y in range(len(self._field)):
            for x in range(len(self._field)):
                if y == 0 or y == 1:
                    self._field[x][y] = Pawn(Color.BLACK, self)
                if y == 6 or y == 7:
                    self._field[x][y] = Pawn(Color.WHITE, self)


    def move(self, x_start,y_start,x_dest,y_dest):
        if self.in_board(x_dest, y_dest) is False:
          raise ValueError('Destionation not in Board')
        if self.in_board(x_start, y_start) is False:
          raise ValueError('Start not in Board')
        if self._field[x_start][y_start] == 0:
          raise ValueError('Start Field Empty')       
        if self._field[x_start][y_start].same_color(x_dest,y_dest):
          raise ValueError('Same Color')
        
            
        figure_to_move = self._field[x_start][y_start]
        self._field[x_start][y_start] = 0
        self._field[x_dest][y_dest] = figure_to_move

    def in_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def is_field_empty(self, x ,y):
      return self._field[x][y] == 0
    

class Piece:
    def __init__(self,color: Color, game: Chess):
        if game is None or color is None:
            raise ValueError
        self._game = game
        self._color = color

    def available_moves(self, x, y):
        print('Not available in base class')

    def valid_turn(self, x_start, y_start, x_dest, y_dest):
        var =  self.in_board(x_dest, y_dest) and self.same_color(x_dest, y_dest) is False and self.piece_in_way(x_start, y_start, x_dest, y_dest) is False
        return var

    def in_board(self, x, y):
        var =  0 <= x < 8 and 0 <= y < 8
        return var

    def same_color(self, x_dest, y_dest):
        var= self._game._field[x_dest][y_dest] != 0 and self._game._field[x_dest][y_dest]._color == self._color
        return var

    def get_field_state(self, x, y):
      if self._game._field[x][y] == 0:
        return FieldState.EMTPTY
      elif self._game._field[x][y]._color == Color.WHITE:
        return FieldState.WHITE_PIECE
      else:
        return FieldState.BLACK_PIECE

    def get_enemy_state(self):
      if self._color == Color.WHITE:
        return FieldState.BLACK_PIECE
      else:
        return FieldState.WHITE_PIECE

    def piece_in_way(self, x_start, y_start, x_dest, y_dest):
      way = self.straight_way(x_start, y_start, x_dest, y_dest)
      for piece in range(1, len(way)):
        if way[piece] != 0 and piece != len(way)-1:
          return True
      return False

    def straight_way(self, x_start, y_start, x_dest, y_dest):
      way = []
      if x_start == x_dest:
        min_y = min(y_start, y_dest)
        max_y = max(y_start, y_dest)
        for y in range(min_y, max_y+1):
          way.append(self._game._field[x_start][y])
      elif y_start == y_dest:
        min_x = min(x_start, x_dest)
        max_x = max(x_start, x_dest)
        for x in range(min_x, max_x+1):
          way.append(self._game._field[x][y_start])
      return way
          
    def field_empty(self, x, y):
      return self._game._field[x][y] == 0


    
class Pawn(Piece):

    def available_moves(self, x, y):
        moves = []
        if self.valid_turn(x, y, x, y+self.get_direction()*2) : moves.append((x, y + self.get_direction()*2))
        if self.valid_turn(x, y, x, y+self.get_direction()) and self.field_empty(x, y+self.get_direction()) : moves.append((x, y + self.get_direction()))
        if self.valid_turn(x, y, x+1, y+self.get_direction()) and self.get_field_state(x+1, y+self.get_direction()) == self.get_enemy_state() : moves.append((x+1, y + self.get_direction()))
        if self.valid_turn(x, y, x-1, y+self.get_direction()) and self.get_field_state(x-1, y+self.get_direction()) == self.get_enemy_state() : moves.append((x-1, y + self.get_direction()))
        return moves

    def get_direction(self):
        if self._color == Color.WHITE:
            return -1
        else:  # black
            return 1