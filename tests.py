from main import get_winner


def check(expected_result, actual_result, test_case_id):
    if expected_result == actual_result:
        print(f"Test Case {test_case_id}: Passed")
    else:
        print(f"Test Case {test_case_id}: Failed")
        print(f"Expected: {expected_result}, Actual: {actual_result}")


if __name__ == "__main__":
    # Test Case 1: Winner is X (diagonal)
    board_1 = [
        ["X", "X", "O"],
        ["O", "X", None],
        ["O", "O", "X"],
    ]
    result_1 = get_winner(board_1)
    check("X", result_1, 1)

    # Test Case 2: No winner (incomplete board)
    board_2 = [
        ["X", "X", "O"],
        ["O", None, "X"],
        ["O", "O", "X"],
    ]
    result_2 = get_winner(board_2)
    check(None, result_2, 2)

    # Test Case 3: Winner is O (row)
    board_3 = [
        ["O", "O", "O"],
        ["X", None, "X"],
        ["X", "X", None],
    ]
    result_3 = get_winner(board_3)
    check("O", result_3, 3)

    # Test Case 4: No winner (empty board)
    board_4 = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    result_4 = get_winner(board_4)
    check(None, result_4, 4)

    # Test Case 5: No winner (complete board)
    board_5 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    result_5 = get_winner(board_5)
    check(None, result_5, 5)
