#import necessary libs
import numpy as np

#create a matrix of 0
ROW_NUM = 6
COL_NUM = 7
game_board = np.zeros((ROW_NUM , COL_NUM))

class Game:
    mat = None # this represents the board matrix
    rows = 0 # this represents the number of rows of the board
    cols = 0 # this represents the number of columns of the board
    turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
    wins = 0 # this represents the number of consecutive disks you need to force in order to win


# class Game:
#     def __init__(self, rows, cols) -> None: 
#         self.rows = rows # this represents the number of rows of the board
#         self.cols = cols # this represents the number of columns of the board
#         self.mat = np.zeros((self.rows, self.cols))
#         self.turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
#         self.wins = 0 # this represents the number of consecutive disks you need to force in order to win

def main():
    my_game = Game()  # my_game is an instance of class Game
    my_game_2 = Game()  # another instance

#rules 
def check_victory(game):
    pass
#for the start index of the winning line
    #check horizontal location: index prior to [COL_NUM-3]: [r][c+0/1/2/3]
    #check vertical loc: index prior to [ROW_NUM-3]: [r+0/1/2/3][c]
    #check diagonals:
        #up-diagonals: [COL_NUM-3][ROW_NUM-3] [r][c],[r+1][c+1],.....
        #down-diagonals: [3,ROW_NUM][COL_NUM-3] [r][c], [r-1][c+1], ....
def apply_move(self,col,pop):
    self.col
    pass

#check wether the highest col still free
def check_move(game,col,pop):
    pass

def computer_move(game,level):
    pass
#change row index of board + print board
def display_board(game):
    pass

def menu():
    pass

if __name__=="__main__":
    main()