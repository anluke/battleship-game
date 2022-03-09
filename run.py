# LEGEND

# O - appears on board if guess is a miss
# X - appears on board if guess is a hit and exits the game

import colorama  # imported colorama to color code some of the text printed to console
from colorama import Fore # Fore used from colorama to add color to print content
from random import randint # imported random to randomize numbers used for computer ship

colorama.init(autoreset=True)


board = [[" "] * 8 for i in range(8)]

"""
This function creates a playboard consisting of rows and columns ranging from 0 to 7.
"""
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    print("  ---------------")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


print("----------------------")
print(" ")
print(Fore.MAGENTA + "  BATTLESHIP GAME  ")
print(" ")
print(Fore.MAGENTA + "   LET'S PLAY !")
print(" ")
print("----------------------")
print(" ")
print_board(board)


"""
Function that puts a computer ship at the random row number
"""
def create_random_row(board):
    return randint(0, len(board)-1)


"""
Function that puts a computer ship at the random column number
"""
def create_random_column(board):
    return randint(0, len(board[0])-1)


random_ship_row = create_random_row(board) 
random_ship_column = create_random_column(board)
print(random_ship_row)
print(random_ship_column)

for turn in range(8): # created a rule for turn of 8 attempts
    print(" ")
    print(Fore.YELLOW + "TURN", turn + 1)
    print(" ")
    while True:
        # if a user inputs an invalid value such as (empty string, text, letters) this prevents our game from crashing
        try:
            guess_row = int(input("Guess Row: "))
            guess_column = int(input("Guess Column: "))
            break
        except ValueError:
            print(" ")
            print(Fore.RED + "Number needed! Please enter a valid input!")
            print(" ")
    
    if guess_row == random_ship_row and guess_column == random_ship_column:
        board[guess_row][guess_column] = 'X'
        print_board(board)
        print(board[guess_row][guess_column])
        print(" ")
        print("---------------------")
        print(Fore.GREEN + "      CONGRATZ")
        print(Fore.GREEN + "***  IT'S A HIT  ***")
        print(Fore.RED + f'Enemy ship was located in row: {random_ship_row} and column: {random_ship_column}')
        print(Fore.GREEN + "***    YOU WIN  ***")
        print("---------------------")
        print(" ")
        break
    elif (guess_row < 0 or guess_row > 7) or (guess_column < 0 or guess_column > 7):
        print(" ")
        print("----------------------------")
        print(Fore.RED + "** OUT OF BOUNDS **")
        print(Fore.YELLOW + f'Your input row was: {guess_row} & column: {guess_column}')
        print(Fore.RED + "PLEASE CHOOSE A NUMBER BETWEEN 0 and 7")
        print("----------------------------")
        print(" ")
    elif board[guess_row][guess_column] == 'O':
        print(" ")
        print("----------------------------")
        print(Fore.RED + "** YOU USED THESE COORDINATES ALREADY **")
        print("----------------------------")
        print(" ")
    else:
        print(" ")
        print("----------------------------")
        print(Fore.CYAN + "YOU MISSED THE BATTLESHIP")
        print("----------------------------")
        print(" ")
        board[guess_row][guess_column] = "O"
    if turn == 7:
        print(" ")
        print(" ")
        print("-----------------------------------------------")
        print(" ")
        print(Fore.RED + "        NO MORE ATTEMPTS")
        print(Fore.RED + "YOU DID NOT HIT COMPUTER BATTLESHIP")
        print(" ")
        print(Fore.RED + "      ***  GAME OVER  ***")
        print(Fore.RED + "      ***  YOU LOSE  ***")
        print(" ")
        print("-----------------------------------------------")
        print(" ")
    turn = turn + 1
    print_board(board)
    print(" ")
