import random

# constants

BOARD_DIMENSION = 3


def new_board():
    board = []
    for _ in range(0, BOARD_DIMENSION):
        column = []
        for _ in range(BOARD_DIMENSION):
            column.append(None)
        board.append(column)
    return board


def render(board):
    rows = []
    for x in range(BOARD_DIMENSION):
        row = []
        for y in range(BOARD_DIMENSION):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    print("  0 1 2 ")
    print("  -----")
    for row in rows:
        output_row = ""
        for cell in row:
            if cell is None:
                output_row += " "
            else:
                output_row += cell
        print("%d|%s|" % (row_num, " ".join(output_row)))
        row_num += 1
    print("  -----")


def get_move():
    while True:
        try:
            x = int(input("Please input your move's X coordinate position?: "))
            y = int(input("Please input your move's Y coordinate position?: "))
            if 0 <= x < BOARD_DIMENSION and 0 <= y < BOARD_DIMENSION:
                return x, y
            else:
                print("Coordinates must be between 0 and 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")


def make_move(board, x_coord, y_coord, player):
    if board[x_coord][y_coord] is None:
        board[x_coord][y_coord] = player
        return True
    else:
        print("Cell is already occupied. Please try again.")
        return False


def is_full(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def get_winner(board):
    lines = []  # rows, columns and diagonals list

    # rows
    for row in board:
        lines.append(row)

    # columns
    for col in range(BOARD_DIMENSION):
        column = [board[row][col] for row in range(BOARD_DIMENSION)]
        lines.append(column)

    # diagonals
    diagonal_1 = [board[i][i] for i in range(BOARD_DIMENSION)]
    diagonal_2 = [board[i][BOARD_DIMENSION - 1 - i] for i in range(BOARD_DIMENSION)]
    lines.append(diagonal_1)
    lines.append(diagonal_2)

    # check lines for winner
    for line in lines:
        if line.count("X") == BOARD_DIMENSION:
            return "X"
        if line.count("O") == BOARD_DIMENSION:
            return "O"

    return None


def get_mode():
    while True:
        print("Choose a game mode:")
        print("1. Player vs. Player (PVP)")
        print("2. Player vs. CPU (PvCPU)")
        choice = input("Enter 1 or 2: ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Invalid input. Please enter 1 or 2.")


def cpu_random_move(board):
    legal_moves = [
        (x, y)
        for x in range(BOARD_DIMENSION)
        for y in range(BOARD_DIMENSION)
        if board[x][y] is None
    ]
    return random.choice(legal_moves) if legal_moves else None


def main():
    try:
        board = new_board()
        render(board)

        game_mode = get_mode()

        players = ["X", "O"]
        curr_player_idx = 0

        while True:
            curr_player = players[curr_player_idx]

            if game_mode == 2 and curr_player == "O":
                print("CPU's turn...")
                move = cpu_random_move(board)
                if move:
                    x, y = move
                    make_move(board, x, y, curr_player)
            else:
                print(f"Player {curr_player}'s turn.")
                while True:
                    x, y = get_move()
                    if make_move(board, x, y, curr_player):
                        break

            render(board)

            winner = get_winner(board)
            if winner:
                print(f"Player {winner} has won!")
                break

            if is_full(board):
                print("The game is a draw!")
                break

            curr_player_idx = 1 - curr_player_idx

    except KeyboardInterrupt:
        print("\n Game interrupted. Thanks for playing!")


if __name__ == "__main__":
    main()
