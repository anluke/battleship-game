# O - appears on board if guess is a miss
# X - appears on board if guess is a hit and exits the game

from random import randint

board = [[" "] * 8 for i in range(8)]


def print_board(board):
    """
    This function creates a playboard
    consisting of rows and columns ranging from 0 to 7.
    """
    print("  0 1 2 3 4 5 6 7")
    print("  ---------------")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


print("-----------------------------------------------")
print("BATTLESHIP GAME")
print("BOARD SIZE: 5, NUMBER OF SHIPS: 1")
print("TOP LEFT CORNER IS ROW:0, COL:0")
print("USE NUMBERS FROM 0 TO 7")
print("-----------------------------------------------")
print_board(board)


def create_random_row(board):
    """
    Function that puts a computer ship at the random row number
    """
    return randint(0, len(board)-1)


def create_random_column(board):
    """
    Function that puts a computer ship at the random column number
    """
    return randint(0, len(board[0])-1)


random_ship_row = create_random_row(board)
random_ship_column = create_random_column(board)
print(random_ship_row)
print(random_ship_column)


for turn in range(8):  # created a rule for turn of 5 attempts
    print(" ")
    print("TURN", turn + 1)
    print(" ")
    while True:
        # if a user inputs an invalid value such as
        # (empty string, text, letters) this prevents our game from crashing
        try:
            guess_row = int(input("Guess Row: "))
            guess_column = int(input("Guess Column: "))
            break
        except ValueError:
            print(" ")
            print("Number needed! Please enter a valid input!")
            print(" ")

    if guess_row == random_ship_row and guess_column == random_ship_column:
        print(board[guess_row][guess_column])
        print("-----------------------------------------------")
        print("      CONGRATZ")
        print("***  IT'S A HIT  ***")
        print(f'       Row: {random_ship_row}')
        print(f'      Column: {random_ship_column}')
        print("***   YOU WIN  ***")
        print("-----------------------------------------------")
        print_board(board)
        break
    elif (guess_row < 0 or guess_row > 7) or \
         (guess_column < 0 or guess_column > 7):
        print("-----------------------------------------------")
        print("** OUT OF BOUNDS **")
        print(f'Your input row was: {guess_row} & column: {guess_column}')
        print("PLEASE CHOOSE A NUMBER BETWEEN 0 and 7")
        print("-----------------------------------------------")
    elif board[guess_row][guess_column] == 'O':
        print("-----------------------------------------------")
        print("** YOU USED THESE COORDINATES ALREADY **")
        print("-----------------------------------------------")
    else:
        print("-----------------------------------------------")
        print("YOU MISSED THE BATTLESHIP")
        print("-----------------------------------------------")
        board[guess_row][guess_column] = "O"
    if turn == 7:
        print(" ")
        print("-----------------------------------------------")
        print("        NO MORE ATTEMPTS")
        print("YOU DID NOT HIT COMPUTER BATTLESHIP")
        print(" ")
        print("      ***  GAME OVER  ***")
        print("      ***  YOU LOSE  ***")
        print("-----------------------------------------------")
        print(" ")
    turn = turn + 1
    print_board(board)
    print(" ")
