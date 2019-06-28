import unittest
from Chess import *

class TestMovement(unittest.TestCase):
    
    def test_pawn_movement(self):
      game = Chess()
      moves = game._field[0][1].available_moves(0,1)
      self.assertEqual(moves, [(0,3),(0,2)])

    def main():
      unittest.main()

    if __name__ == "__main__":
      main()

