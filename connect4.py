#add them nay:
#4 neu full bang --> end game 
#5 neu input la a 2' --> valueerror --> in lai dong "welcome connect 4...." :( fix it plz

#import necessary libs
import numpy as np
import random

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
    game = Game(ROW_NUM, COL_NUM) 
    print(np.flip(game.mat,0))
    
    while game.playing: 
        try: 
            print("Welcome to Connect 4! Let's play together!")
            mode = int(input("How many player? (1 or 2): "))
            if mode == 1:
                computer_mode(game)
            elif mode == 2:
                two_player_mode(game)
            else: 
                print("Invalid input. Try again!")
        except ValueError:
            print("Invalid input. Please enter a valid integer (1-2).")

def two_player_mode(game):
    turn = 0 
    while game.playing:
        #Ask for Player 1 input
        if turn == 0:
            mutual_flow(game, 1)

        #Ask for Player 2 input
        else:
            mutual_flow(game, 2)

        display_board(game.mat)
        turn += 1 
        turn = turn % 2

def computer_mode(game):
    print("Welcome to AI mode ahihihihi. Which level you wanna play? (1-3)")
    level = 0
    turn = 0 
    while True: 
        try: 
            level = int(input("(1)Easy (2)Medium (3)Hard: "))
            if level not in range(1, 4):
                print("Invalid input for level. Try again!")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer (1-3).")

    while game.playing:
        #Ask for Player 1 input
        if turn == 0:
            mutual_flow(game, 1)

        #AI input, with only "add" action 
        else:
            player = 2
            print("AI takes turn")
            if level == 1:
                #random move
                while game.playing:
                    action = random.choice(["a", "r"])
                    # action = "a"
                    col = random.randint(0, COL_NUM-1)
                    if check_input(game.mat, player, action, col):
                        if check_move(game.mat, action, col, player):
                            apply_move(game.mat, action, col, player)
                            if check_victory(game.mat, player):
                                print(f"Yay!!! AI wins")
                                game.playing = False  
                        break    
                    else: 
                        print("Co len AI oi/Invalid input. Try again.")  
            elif level == 2:
                # best_move()
                print("level 2")
            elif level == 3:
                # minimax()
                print("level 3")
            else: 
                print("Invalid input. Try again!")
            #mutual_flow(game, 2)

        display_board(game.mat)
        turn += 1 
        turn = turn % 2

def mutual_flow(game, player):
    while True:
        action, col = get_input(game, player)
        if check_input(game.mat, player, action, col):
            if check_move(game.mat, action, col, player):
                apply_move(game.mat, action, col, player)
                if check_victory(game.mat, player):
                    print(f"Congrats! Player {player} win")
                    game.playing = False  
            break 
        else: 
            print("Co len dinh oi/Invalid input. Try again.")       

def get_input(mat, player):
    while True: 
        print(f"Player {player}, which action you want to take?")
        ask = input(f"\"a\" for add-in, \"r\" for remove and (0-6) for col, seperate by ' ': ").lower().split()
        if not len(ask) == 2:
            print("Wrong format. Try again")
            continue
        else:
            return ask[0], int(ask[1])

def check_input(mat, player, action, col):
    if not (action == 'a' or action == 'r'):
        print("Invalid input letter. Try again.")
        return False
    elif col not in range(COL_NUM):
        print("Invalid input col. Try again.")
        return False
    elif not check_move(mat, action, col, player):
        print("No available position in this column. Please try another col!")  
        return False  
    else:
        return True

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

#change row index of board + print board
def display_board(mat):
    print(np.flip(mat, 0))

def menu():
    pass

if __name__=="__main__":
    main()