from Chess import *
from Draw import *

game = Chess()
draw_field(game)

game.move(1,1,1,3)
game.move(1,3,1,5)
draw_field(game)
moves = game._field[1][5].available_moves(1,5)
moves


