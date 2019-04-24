from Chess import *
from Draw import *

game = Chess()
draw_field(game)

moves = game._field[1][1].available_moves(1,1)


show_moves(game,3,1)



