#add them nay:
#4 neu full bang --> end game 

#import necessary libs
import numpy as np

ROW_NUM = 6
COL_NUM = 7

class Game:
    def __init__(self, rows, cols) -> None: 
        self.rows = rows # this represents the number of rows of the board
        self.cols = cols # this represents the number of columns of the board
        self.mat = np.zeros((self.rows, self.cols))
        self.turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
        self.wins = 0 # this represents the number of consecutive disks you need to force in order to win
        self.playing = True

def main():
    game = Game(ROW_NUM, COL_NUM)  # my_game is an instance of class Game
    # my_game_2 = Game()  # another instance
    print(np.flip(game.mat,0))
    turn = 0 
    
    while game.playing:
        #Ask for Player 1 input
        if turn == 0:
            start(game, 1)

        #Ask for Player 2 input
        else:
           start(game, 2)

        display_board(game.mat)
        turn += 1 
        turn = turn % 2

def start(game, player):
    action, col = check_input(game.mat, player)
    if check_move(game.mat, action, col, player):
        apply_move(game.mat, action, col, player)
        if check_victory(game.mat, player):
            print(f"Congrats! Player {player} win")
            game.playing = False

def check_input(mat, player):
    while True:
        try: 
            print(f"Player {player}, which mode you want to choose?")
            action = input(f"\"a\" for add-in, \"r\" for remove: ").lower()
            if action == "a" or action == "r":
                while True:
                    try: 
                        col = int(input(f"Player {player} please pick a column to add-in (0-6): "))
                        if col not in range(COL_NUM):
                            print("Invalid input. Try again.")
                        elif not check_move(mat, action, col, player):
                            print("No available position in this column. Please try another col!")    
                        else:
                            return action, col
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
            else:
                print("Invalid input. Try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


#check wether the highest col still free
def check_move(mat, action, col, player):
    if action == "a":
        return mat[ROW_NUM-1][col] == 0
    else:
        return mat[0][col] == player

def apply_move(mat, action, col, player):
    if action == "a":
        for r in range(ROW_NUM):
            if mat[r][col] == 0:
                mat[r][col] = player
                return r
    else:
        for r in range(ROW_NUM-1):
            mat[r][col] = mat[r+1][col]
        
        mat[ROW_NUM-1][col] = 0

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