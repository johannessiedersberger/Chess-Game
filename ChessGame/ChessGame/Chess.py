from enum import Enum
import doctest


class Color(Enum):
    WHITE = 0
    BLACK = 1

class FieldState(Enum):
    WHITE_PIECE = 0
    BLACK_PIECE = 1
    EMTPTY = 2


class Chess():

    #initialization
    def __init__(self):
        self._field = [[0 for x in range(8)] for y in range(8)]
        self._place_piece()
    

    def _place_piece(self):
      self._place_pawns()
      self._place_rooks()
      self._place_queens()

    def _place_pawns(self):
        for i in range(0,8):
            self._field[i][1] = Pawn(Color.BLACK, self)
            self._field[i][6] = Pawn(Color.WHITE, self)
            
    def _place_rooks(self):
      for y in range(len(self._field)):
            for x in range(len(self._field)):
              if y == 0 and (x == 0 or x == 7):
                self._field[x][y] = Rook(Color.BLACK, self)
              if y == 7 and (x == 0 or x == 7):
                self._field[x][y] = Rook(Color.WHITE, self)

    def _place_queens(self):
      for y in range(len(self._field)):
            for x in range(len(self._field)):
              if y == 0 and x == 3:
                self._field[x][y] = Queen(Color.BLACK, self)
              if y == 7 and x == 3:
                self._field[x][y] = Queen(Color.WHITE, self)


    def move(self, x_start,y_start,x_dest,y_dest):
        if self.in_board(x_dest, y_dest) is False:
          raise ValueError('Destionation not in Board')
        if self.in_board(x_start, y_start) is False:
          raise ValueError('Start not in Board')
        if self._field[x_start][y_start] == 0:
          raise ValueError('Start Field Empty')       
        if self._field[x_start][y_start].same_color(x_dest,y_dest):
          raise ValueError('Same Color')
        if (x_dest,y_dest) not in self._field[x_start][y_start].available_moves(x_start, y_start):
          raise ValueError('Not an available move')
        
            
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
        var =  self.in_board(x_dest, y_dest) and self.same_color(x_dest, y_dest) is False 
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
          
    def field_empty(self, x, y):
      return self._game._field[x][y] == 0

    straigt_directions = [(1,0), (0,1), (-1,0), (0,-1)]
    diagonal_directions = [(1,1), (-1,1), (1,-1), (-1,-1)]

    def get_way(self, x_pos, y_pos, directions):
      way = []
      for x_dir, y_dir in directions:
        x_temp,y_temp = x_pos + x_dir, y_pos + y_dir
        while self.in_board(x_temp, y_temp):
          target = self._game._field[x_temp][y_temp]

          if target is 0: way.append((x_temp, y_temp))
          elif target._color != self._color:
            way.append((x_temp, y_temp))
            break
          else:
            break
          x_temp,y_temp = x_temp + x_dir, y_temp + y_dir

      return way

    
class Pawn(Piece):

    def available_moves(self, x, y):
        moves = []
        if self.valid_turn(x, y, x, y+self.get_direction()*2) and self.first_turn(x,y) : moves.append((x, y + self.get_direction()*2))
        if self.valid_turn(x, y, x, y+self.get_direction()) and self.field_empty(x, y+self.get_direction()) : moves.append((x, y + self.get_direction()))
        if self.valid_turn(x, y, x+1, y+self.get_direction()) and self.get_field_state(x+1, y+self.get_direction()) == self.get_enemy_state() : moves.append((x+1, y + self.get_direction()))
        if self.valid_turn(x, y, x-1, y+self.get_direction()) and self.get_field_state(x-1, y+self.get_direction()) == self.get_enemy_state() : moves.append((x-1, y + self.get_direction()))
        return moves

    def get_direction(self):
        if self._color == Color.WHITE:
            return -1
        else:  
            return 1

    def first_turn(self, x_start, y_start):
      if y_start == 1 or y_start == 6:
        return True
      else:
        return False

class Rook(Piece):
  def available_moves(self, x, y):
    moves = self.get_way(x,y,self.straigt_directions)
    return moves

class Queen(Piece):
  def available_moves(self, x, y):
    moves = self.get_way(x,y,self.straigt_directions+self.diagonal_directions)
    return moves

class King(Piece):
    def availableMoves(self,x_start,y_start,gameboard, Color = None):
      return [(x_dest,y_dest) for x_dest,y_dest in kingList(x_start,y_start) if self.valid_turn(x_start,y_start,x_dest,y_dest)]
    def kingList(x,y):
      return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]
    
    