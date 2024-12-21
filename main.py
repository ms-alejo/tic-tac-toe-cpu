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
    updated_board = board
    updated_board[x_coord][y_coord] = player
    return updated_board


def is_full(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def main():
    board = new_board()
    render(board)

    players = ["X", "O"]
    curr_player_idx = 0

    while True:
        print(f"Player {players[curr_player_idx]}'s turn.")
        x, y = get_move()
        if make_move(board, x, y, players[curr_player_idx]):
            render(board)
            if is_full(board):
                print("The game is a draw!")
                break
            curr_player_idx = 1 - curr_player_idx


if __name__ == "__main__":
    main()
