
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True


current_player = "X"


winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner is None:
        print("Tie.")

def handle_turn(current_player):

    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = current_player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global board, winner, current_player, game_still_going
    if (board[0] == current_player and board[3] == current_player and board[6] == current_player) \
            or (board[1] == current_player and board[4] == current_player and board[7] == current_player) \
            or (board[2] == current_player and board[5] == current_player and board[8] == current_player) \
            or (board[0] == current_player and board[1] == current_player and board[2] == current_player) \
            or (board[3] == current_player and board[4] == current_player and board[5] == current_player) \
            or (board[6] == current_player and board[7] == current_player and board[8] == current_player) \
            or (board[0] == current_player and board[4] == current_player and board[8] == current_player) \
            or (board[2] == current_player and board[4] == current_player and board[6] == current_player):
        winner = current_player
        game_still_going = False

    return


def check_if_tie():
  global game_still_going

  if "-" not in board:
    game_still_going = False
    return True

  else:
    return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


play_game()


