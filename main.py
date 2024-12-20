# constants
BOARD_DIMENSION = 3


def new_board():
    return [[None for _ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]


def main():
    board = new_board()
    print(board)


if __name__ == "__main__":
    main()
