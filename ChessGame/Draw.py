from Chess import *
from termcolor import colored


def draw_field(game: Chess):
    field = game._field
    for y in range(0, 8):
        for x in range(0, 8):
            if isinstance(field[x][y], Pawn) and field[x][y]._color == Color.WHITE:
                print(white_pieces[Pawn], end='')
                #print((x, y), end='')
            elif isinstance(field[x][y], Pawn) and field[x][y]._color == Color.BLACK:
                print(black_pieces[Pawn], end='')
                #print((x, y))
            elif field[x][y] == 0:
                print(colored(empty_field, 'yellow'), end='')
        print()
    print()


def show_moves(game: Chess, x, y):
        field = game._field
        moves = field[x][y].available_moves(x,y)
        print(moves)
        for y in range(0, 8):
            for x in range(0, 8):
                if((x,y) in moves):
                    if isinstance(field[x][y], Pawn) and field[x][y]._color == Color.WHITE:
                        print(colored(white_pieces[Pawn], 'blue'), end='')
                    elif isinstance(field[x][y], Pawn) and field[x][y]._color == Color.BLACK:
                        print(colored(white_pieces[Pawn], 'blue'), end='')
                    elif field[x][y] == 0:
                        print(colored(empty_field, 'blue'), end='')
                else:
                    if isinstance(field[x][y], Pawn) and field[x][y]._color == Color.WHITE:
                        print(white_pieces[Pawn], end='')
                    elif isinstance(field[x][y], Pawn) and field[x][y]._color == Color.BLACK:
                        print(white_pieces[Pawn], end='')
                    elif field[x][y] == 0:
                        print(colored(empty_field, 'red'), end='')
            print()
        print()








empty_field = '🈴'

white_pieces = {Pawn: '♙'}
black_pieces = {Pawn: '♟'}
