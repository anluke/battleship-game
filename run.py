from random import randint



"""
In here we are creating 5 lists, filled in with 5 interpunct symbols. Since Python can't import it directly I used unicode command.
"""



board = [[" "] * 8 for i in range(8)]

# def print_board(board):
#     for row in board:
#         print(" ".join(row))

def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    print("  *-*-*-*-*-*-*-*")
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
    return randint(0, len(board) -1)


def create_random_column(board):
    return randint(0, len(board[0]) -1)

random_ship_row = create_random_row(board)
random_ship_column = create_random_column(board)

print(random_ship_row)
print(random_ship_column)

for turn in range(4):
    print(" ")
    print("Turn", turn + 1)
    print(" ")
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    # try:
    #     int(input(''))
    # except ValueError:
    #     pass
    if guess_row == random_ship_row and guess_col == random_ship_column:
        print(" ")
        print("---------------------")
        print("    CONGRATZ")
        print("***  IT'S A HIT  ***")
        print(f'Enemy ship was located in row: {random_ship_row} and column: {random_ship_column}')
        print("***  YOU WIN  ***")
        print("---------------------")
        print(" ")
        break

    elif (guess_row < 0 or guess_row > 7) or (guess_col < 0 or guess_col > 7):
        print(" ")
        print("Out of bounds. Please choose a number between 0 and 7")
        print(" ")
    elif board[guess_row][guess_col] == 'X':
        print(" ")
        print("You guessed that one already")
        print(" ")
    else:
        print(" ")
        print("You missed my battleship")
        print(" ")
        board[guess_row][guess_col] = "X"
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