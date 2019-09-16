# Chess-Game
A simple chess-game written in python. It uses just the console and a few unicode-icons to print the game-board. This project was created to improve my python programming skills. 

# Screenshots
![ChessPython](https://user-images.githubusercontent.com/36839962/60382759-0dc80780-9a68-11e9-86ea-3a0a58fd41f9.PNG)

# Technologies and Libaries used
- [Python](https://python.org)
- [unittest](https://docs.python.org/3/library/unittest.html) for testing
- [Chess Unicode Symblos](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) to display the game field
- [Visual Studio 2019](https://visualstudio.microsoft.com/)

# Code Examples
### Draw a Field
```
>>> from Chess import *
>>> from Draw import *
>>> game = Chess()
>>> draw_field(game)
 0.1.2.3.4.5.6.7
0♜♞♝♛♚♝♞♜
1♟♟♟♟♟♟♟♟
2♋♋♋♋♋♋
3♋♋♋♋♋♋
4♋♋♋♋♋♋
5♋♋♋♋♋♋
6♙♙♙♙♙♙♙♙
7♖♘♗♕♔♗♘♖
```
### Show the moves
```
>>> show_moves(game, 3,1)
 0.1.2.3.4.5.6.7
0♜♞♝♛♚♝♞♜
1♟♟♟♟♟♟♟♟
2♋♋♋♋♋♋
3♋♋♋♋♋♋
4♋♋♋♋♋♋
5♋♋♋♋♋♋
6♙♙♙♙♙♙♙♙
7♖♘♗♕♔♗♘♖
```
# Unit Tests
### Check the pawn movement
```
def test_pawn_movement(self):
      #given
      game = Chess()
      #when
      moves = game._field[0][1].available_moves(0,1)
      #then
      self.assertEqual(moves, [(0,3),(0,2)])
```
### Check the queen movement
```
def test_queen_movement(self):
      #given
      game = Chess()
      game.move(3,1,3,3) # move pawn in front of queen
      game.move(3,0,3,1) # move queen
      #when
      moves = game._field[3][1].available_moves(3,1)
      #then
      self.assertEqual(moves, [(3,2),(3,0),(4,2),(5,3),(6,4), (7,5), (2,2), (1,3), (0,4)])
```
