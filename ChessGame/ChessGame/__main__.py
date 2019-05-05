from Chess import *
from Draw import *

game = Chess()
draw_field(game)

moves = game._field[7][6].available_moves(7,6)
show_moves(game,7,6)


