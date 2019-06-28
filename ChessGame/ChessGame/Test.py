import unittest
from Chess import *

class TestMovement(unittest.TestCase):
    
    def test_pawn_movement(self):
      #given
      game = Chess()
      #when
      moves = game._field[0][1].available_moves(0,1)
      #then
      self.assertEqual(moves, [(0,3),(0,2)])

    def test_rook_movement(self):
      #given
      game = Chess()
      game.move(0,1,0,3)
      #when
      moves = game._field[0][0].available_moves(0,0)
      #then
      self.assertEqual(moves, [(0,1), (0,2)])
      
    def test_queen_movement(self):
      #given
      game = Chess()
      game.move(3,1,3,3) # move pawn in front of queen
      game.move(3,0,3,1) # move queen
      #when
      moves = game._field[3][1].available_moves(3,1)
      #then
      self.assertEqual(moves, [(3,2),(3,0),(4,2),(5,3),(6,4), (7,5), (2,2), (1,3), (0,4)])

    def main():
      unittest.main()

    if __name__ == "__main__":
      main()











