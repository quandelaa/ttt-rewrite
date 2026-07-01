from board import Board
from board_utils import Utils

def play():
    utils = Utils()
    board = Board()

    while True:
        winner = utils.winner(board.state)
        if winner is not None:
            break

        if utils.terminal(board.state):
            break

        while True:
            print(utils.player(board.state), "'s turn", "\n", sep="")

            try:
                row = int(input("row: "))
                col = int(input("col: "))

            except ValueError as e:
                print(e, "\n")
                continue

            if col > 3 or row > 3 or row <= 0 or col <= 0:
                continue

            break

        action = (row, col)
        new_board = utils.result(action, board.state)

        if new_board is not None:
            board.update_state(new_board)
        else:
            continue

        utils.show(board.state)

    if winner is not None:
        print(winner)
    else:
        print("Tie")

if __name__ == "__main__":
    play()
