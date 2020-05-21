# Tic-Tac-Toe

#   The tic tac toe board is arranged in a coordinate grid, so that (1,1) is
# the bottom left square of the board and (3,3) is the top right square of the
# board. However, the variable 'board' is a matrix that keeps track of the state
# of the board, and it's indices start at [0][0]. Therefore, a user marking an
# 'X' on coordinate (1,1) will set board[0][0] to 'X'.


def print_board():
    """ Print the current state of the board. """
    print("---------")
    print("| {} {} {} |".format(board[0][2], board[1][2], board[2][2]))
    print("| {} {} {} |".format(board[0][1], board[1][1], board[2][1]))
    print("| {} {} {} |".format(board[0][0], board[1][0], board[2][0]))
    print("---------")


def get_coordinates():
    """ Ask for user input. Make sure the input is a valid coordinate pair. """
    while True:
        try:
            x, y = input("Enter the coordinates: ").split(" ")
        except ValueError:
            print("ValueError")
            continue
        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
        elif x not in "123" or y not in "123":
            print("Coordinates should be from 1 to 3!")
        elif len(x) != 1 or len(y) != 1:
            print("Coordinates should be from 1 to 3!")
        elif board[int(x) - 1][int(y) - 1] != " " \
                and board[int(x) - 1][int(y) - 1] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            break
    x = int(x)
    y = int(y)
    # The coordinate grid starts at (1,1), but the indices of the matrix that
    # keeps track of the board start at board[0][0]. So the coordinates entered
    # must be reduced by one to match the matrix indices.
    x -= 1
    y -= 1
    return x, y


def x_or_o(turn):
    """ Return 'X' if it's X's turn. Return 'O' if it's O's turn. """
    if turn % 2:
        return "X"
    else:
        return "O"


def check_state():
    """ Check the state of the board to see if someone has won the game. """
    # Make a list for every line on the tic-tac-toe board.
    row_1 = [board[x][0] for x in range(3)]
    row_2 = [board[x][1] for x in range(3)]
    row_3 = [board[x][2] for x in range(3)]
    column_1 = [x for x in board[0]]
    column_2 = [x for x in board[1]]
    column_3 = [x for x in board[2]]
    diagonal_1 = [board[x][x] for x in range(3)]
    diagonal_2 = [board[2][0], board[1][1], board[0][2]]
    # three_in_a_row is a list of all the lines on the board.
    three_in_a_row = [row_1, row_2, row_3,
                      column_1, column_2, column_3,
                      diagonal_1, diagonal_2]
    # Check every line to see if there are 3 X's or 3 O's in a row.
    for line in three_in_a_row:
        if line[0] == x_or_o(turn) and \
                line[1] == x_or_o(turn) and \
                line[2] == x_or_o(turn):
            return "{} wins".format(x_or_o(turn))


# Initialize variables for new game.
board = [[" " for i in range(3)] for i in range(3)]  # Board is an empty 3x3 matrix.
turn = 1

# Start of game.
while True:
    print_board()
    x_coordinate, y_coordinate = get_coordinates()
    board[x_coordinate][y_coordinate] = x_or_o(turn)
    game_state = check_state()
    if game_state == "X wins":
        print_board()
        print("X wins")
        break
    elif game_state == "O wins":
        print_board()
        print("O wins")
        break
    elif turn == 9:
        print_board()
        print("Draw")
        break
    else:
        turn += 1
