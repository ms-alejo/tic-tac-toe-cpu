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


def main():
    board = new_board()
    board[0][1] = "X"
    board[2][0] = "O"
    render(board)


if __name__ == "__main__":
    main()
