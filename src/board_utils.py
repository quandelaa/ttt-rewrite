class Utils:
    def __init__(self) -> None:
        pass

    @classmethod
    def next_player(cls, player):
        if player == "X":
            return "O"

        return "X"

    @classmethod
    def player(cls, board: list):
        Xs = 0
        Os = 0

        for row in board:
            Xs += row.count("X")
            Os += row.count("O")

        if Xs > Os:
            return "O"

        return "X"

    @classmethod
    def result(cls, action, board: list):
        row = action[0] - 1        
        col = action[1] - 1


        player = cls.player(board)
        new_board = board.copy()

        if new_board[row][col] == "?":
            new_board[row][col] = player
        else:
            return None

        return new_board

    @classmethod
    def winner(cls, board: list):
        length = len(board)

        for i, row in enumerate(board):
            vertical = [board[j][i] for j in range(length)]
            diagonal = [board[j][j] for j in range(length)]

            board_reversed = list(reversed(board))
            diagonal2 = [board_reversed[j][j] for j in range(length)]

            if all(item == "X" for item in vertical) or all(col == "X" for col in row) or all(item == "X" for item in diagonal) or all(item == "X" for item in diagonal2):
                return "X"
            elif all(item == "O" for item in vertical) or all(col == "O" for col in row) or all(item == "O" for item in diagonal) or all(item == "O" for item in diagonal2):
                return "O"

        return None

    @classmethod
    def available_actions(cls, board):
        availables = []

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "?":
                    availables.append((i+1, j+1))

        return availables

    @classmethod
    def terminal(cls, board):
        filled = 0

        for row in board:
            if "?" not in row:
                filled += 1

        if filled == len(board):
            return True
        
        return False

    @classmethod
    def show(cls, board: list):
        print()

        for row in board:
            for item in row:
                print(item, "", end="")
            print()

        print()
