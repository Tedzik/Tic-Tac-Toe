# ---- Global Variables ----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going

game_still_going = True

# whos turn is it?

current_player = "X"

# who won? or tie?

winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + "Won.")
    elif winner is None:
        print("Tie.")


def handle_turn(player):
    position = input("Choose position from 1-9: ")
    position = int(position) - 1

    board[position] = current_player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global board, winner, current_player, game_still_going
    if (board[0] == current_player and board[3] == current_player and board[6] == current_player) \
            or (board[1] == current_player and board[4] == current_player and board[7] == current_player) \
            or (board[2] == current_player and board[5] == current_player and board[8] == current_player):
        winner = current_player
        game_still_going = False
    # check columns
    # check rows
    # check diagonals
    return


def check_if_tie():
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


play_game()

# board
# display board
# play game
# handle turn
# check win
# check columns
# check rows
# check diagonals
# check ties
# flip players
