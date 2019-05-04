from Chess import *
from Draw import *

game = Chess()
draw_field(game)

moves = game._field[0][0].available_moves(0,0)


show_moves(game,0,0)

game.move(0,0,1,1)


