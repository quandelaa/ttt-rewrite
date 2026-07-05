from board import Board
from q_algos import Bot
from board_utils import Utils

def train(n):
    bot = Bot()

    for i in range(n):
        if (i+1) % 50000 == 0:
            print("training match", i+1)

        board = Board()

        last = {
            "X": {"state": None, "action": None},
            "O": {"state": None, "action": None}
        }

        while True:
            current_board = board.state
            current_state = Utils.flatten(current_board)

            action = bot.choose_action(current_board, True)

            current_plr = Utils.player(current_board)
            next_plr = Utils.next_player(current_plr)

            last[current_plr]["state"] = current_state
            last[current_plr]["action"] = action

            new_board = Utils.result(action, current_board)
            new_state = Utils.flatten(new_board)
            
            board.update_state(new_board)

            if Utils.winner(new_board) is None:
                if Utils.terminal(new_board):
                    bot.update(
                        last[next_plr]["state"],
                        last[next_plr]["action"],
                        new_state,
                        0
                    )

                    break

            if Utils.winner(new_board) is not None:
                bot.update(current_state, action, new_state, 1)
                
                bot.update(        
                    last[next_plr]["state"],
                    last[next_plr]["action"],
                    new_state,
                    -1
                )

                break
            elif last[next_plr]["state"] is not None:
                bot.update(
                    last[next_plr]["state"],
                    last[next_plr]["action"],
                    new_state,
                    0
                )

    print("done training")
    return bot

def play(bot):
    board = Board()

    while True:
        plr = input("You are X/O: ").upper()

        if plr in ("X", "O"):
            break

    print()
    
    while True:
        winner = Utils.winner(board.state)
        if winner is not None:
            break

        if Utils.terminal(board.state):
            break

        current_plr = Utils.player(board.state)
        print(f"{current_plr}'s turn")

        if current_plr == plr:
            while True:
                try:
                    row = int(input("row: "))
                    col = int(input("col: "))
                except ValueError as e:
                    print(e, "\n")
                    continue

                if col > 3 or row > 3 or row <= 0 or col <= 0:
                    print()
                    continue

                break
        else:
            row, col = bot.choose_action(board.state)

        action = (row, col)
        new_board = Utils.result(action, board.state)

        if new_board is not None:
            board.update_state(new_board)
        else:
            print("\nspot already played\n")
            continue

        Utils.show(board.state)

    if winner is not None:
        print(f"{winner} won")
    else:
        print("tie")

def main():
    bot = train(1000000)
    
    play(bot)

if __name__ == "__main__":
    main()
