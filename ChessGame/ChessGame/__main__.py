from Chess import *
from Draw import *

game = Chess()
draw_field(game)

moves = game._field[7][7].available_moves(7,7)
show_moves(game,7,7)


