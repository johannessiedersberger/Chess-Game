from Chess import *
from termcolor import colored


def draw_field(game: Chess):
    field = game._field
    print(" 0.1.2.3.4.5.6.7")
    for y in range(0, 8):
        print(y,end='')
        for x in range(0, 8):    
            if field[x][y] == 0:
                print(colored(empty_field, 'yellow'), end='')            
            elif field[x][y]._color == Color.WHITE:
              print(white_pieces[type(field[x][y])], end='')   
            elif field[x][y]._color == Color.BLACK:
              print(black_pieces[type(field[x][y])], end='')   
        print()
    print()
     
def show_moves(game: Chess, x, y):
        if game.is_field_empty(x,y):
          raise ValueError('Coordinate is 0, so no moves')
        if game.in_board(x,y) is False:
          raise ValueError('Coordinate not in board')
        field = game._field
        moves = field[x][y].available_moves(x,y)
 
        print(" 0.1.2.3.4.5.6.7")
        for y in range(0, 8):
            print(y,end='')
            for x in range(0, 8):
                if((x,y) in moves):
                    if field[x][y] == 0:
                        print(colored(empty_field, 'blue'), end='')
                    elif field[x][y]._color == Color.WHITE:
                      print(colored(white_pieces[type(field[x][y])], 'blue' ), end='')   
                    elif field[x][y]._color == Color.BLACK:
                      print(colored(black_pieces[type(field[x][y])], 'blue' ), end='')    
                else:
                    if field[x][y] == 0:
                      print(colored(empty_field, 'yellow'), end='')            
                    elif field[x][y]._color == Color.WHITE:
                      print(white_pieces[type(field[x][y])], end='')   
                    elif field[x][y]._color == Color.BLACK:
                      print(black_pieces[type(field[x][y])], end='')                    
            print()
        print()


empty_field = '♋'


white_pieces = {Pawn: '♙',  Rook : '♖', Queen: '♕'}
black_pieces = {Pawn: '♟',  Rook : '♜', Queen: '♛'}

