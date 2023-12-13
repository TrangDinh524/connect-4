#add them nay:
#1.neu check_move ma false thi sao -> print nho user chon lai column 
#2. input la chu?3

#import necessary libs
import numpy as np

ROW_NUM = 6
COL_NUM = 7

# class Game:
#     def __init__(self, rows, cols) -> None: 
#         self.rows = rows # this represents the number of rows of the board
#         self.cols = cols # this represents the number of columns of the board
#         self.mat = np.zeros((self.rows, self.cols))
#         self.turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
#         self.wins = 0 # this represents the number of consecutive disks you need to force in order to win

class Game:
    rows = ROW_NUM # this represents the number of rows of the board
    cols = COL_NUM # this represents the number of columns of the board
    mat = np.zeros((rows, cols))
    turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
    wins = 0 # this represents the number of consecutive disks you need to force in order to win

def main():
    game = Game()  # my_game is an instance of class Game
    # my_game_2 = Game()  # another instance
    print(np.flip(game.mat,0))
    playing=True
    turn = 0 
    
    while playing:
        #Ask for Player 1 input
        if turn == 0:
            col = int(input("Player 1 please pick a column (0-6): "))
            while not is_valid_input(col):
                col = int(input("Player 1 please pick a column again (0-6): "))
            if check_move(game.mat, col):
                row = apply_move(game.mat, col, 1)
                if check_victory(game.mat, 1):
                    print("Congrats! Player 1 win")
                    playing = False

        #Ask for Player 2 input
        else:
            col =  int(input("Player 2 please pick a column (0-6): "))
            while not is_valid_input(col):
                col = int(input("Player 2 please pick a column again (0-6): "))
            if check_move(game.mat, col):
                row = apply_move(game.mat, col, 2)
                if check_victory(game.mat, 2):
                    print("Congrats! Player 2 win")
                    playing = False

        display_board(game.mat)
        turn += 1 
        turn = turn % 2

def is_valid_input(col):
    if col not in range(COL_NUM):
        print("Invalid input. Try again.")
        return False
    else:
        return True 

#check wether the highest col still free
def check_move(mat,col):
    return mat[ROW_NUM-1][col] == 0

def apply_move(mat, col, player):
    for r in range(ROW_NUM):
        if mat[r][col] == 0:
            mat[r][col] = player
            return r

#rules 
def check_victory(mat, player):
#for the start index of the winning line
    #check horizontal location: 
    for c in range(COL_NUM-3):
        for r in range(ROW_NUM):
            if mat[r][c] == mat[r][c+1] == mat[r][c+2] == mat[r][c+3] and mat[r][c] == player:
                return True

    #check vertical loc: 
    for c in range(COL_NUM):
        for r in range(ROW_NUM-3):
            if mat[r][c] == mat[r+1][c] == mat[r+2][c] == mat[r+3][c] and mat[r][c] == player:
                return True

    #check up-diagonals: [COL_NUM-3][ROW_NUM-3] [r][c],[r+1][c+1],.....
    for c in range(COL_NUM-3):
        for r in range(ROW_NUM-3):
            if mat[r][c] == mat[r+1][c+1] == mat[r+2][c+2] == mat[r+3][c+3] and mat[r][c] == player:
                return True

    #check down-diagonals: [3,ROW_NUM][COL_NUM-3] [r][c], [r-1][c+1], ....
    for c in range(COL_NUM-3):
        for r in range(3, ROW_NUM):
            if mat[r][c] == mat[r-1][c+1] == mat[r-2][c+2] == mat[r-3][c+3] and mat[r][c] == player:
                return True

def computer_move(game,level):
    pass
#change row index of board + print board
def display_board(mat):
    print(np.flip(mat, 0))

def menu():
    pass

if __name__=="__main__":
    main()