from Chess import *
from Draw import *

game = Chess()
draw_field(game)

game.move(0,1, 0, 3)
game.move(0,0, 0, 2)

draw_field(game)


