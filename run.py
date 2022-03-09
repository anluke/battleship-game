import colorama
from colorama import Back, Fore, Style
from random import randint

colorama.init(autoreset=True)


board = [[" "] * 8 for i in range(8)]


def print_board(board):
    print(Fore.RED + "  0 1 2 3 4 5 6 7")
    print(Fore.RED + "  ---------------")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


print("----------------------")
print(" ")
print("Let's play Battleship!")
print(" ")
print("----------------------")
print(" ")
print_board(board)


def create_random_row(board):
    return randint(0, len(board)-1)


def create_random_column(board):
    return randint(0, len(board[0])-1)


random_ship_row = create_random_row(board)
random_ship_column = create_random_column(board)
print(" ")
print(" ")
print("Computer result: (TEMPORARY ONLY)")
print(random_ship_row)
print(random_ship_column)

for turn in range(4):
    print(" ")
    print("Turn", turn + 1)
    print(" ")
    while True:
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Column: "))
            break
        except ValueError:
            print("please enter a valid input")
    
    if guess_row == random_ship_row and guess_col == random_ship_column:
        board[guess_row][guess_col] = 'X'
        print_board(board)
        print(" ")
        print("---------------------")
        print("    CONGRATZ")
        print("***  IT'S A HIT  ***")
        print(Fore.RED + f'Enemy ship was located in row: {random_ship_row} and column: {random_ship_column}')
        print("***  YOU WIN  ***")
        print("---------------------")
        print(" ")
        break
    elif (guess_row < 0 or guess_row > 7) or (guess_col < 0 or guess_col > 7):
        print(" ")
        print("Out of bounds. Please choose a number between 0 and 7")
        print(" ")
    elif board[guess_row][guess_col] == '0':
        print(" ")
        print("You guessed that one already")
        print(" ")
    else:
        print(" ")
        print("You missed my battleship")
        print(" ")
        board[guess_row][guess_col] = "0"
    if turn == 3:
        print("--------------------")
        print("NO MORE ATTEMPTS")
        print("***  GAME OVER  ***")
        print("--------------------")
        print("***  YOU LOSE  ***")
        print(" ")
        print(" ")
    turn = turn + 1
    print_board(board)