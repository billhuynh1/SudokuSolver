from collections import defaultdict
BOARD_LENGTH = 9

# class Sudoku:
def is_valid(board: list) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(BOARD_LENGTH):
        for c in range(BOARD_LENGTH):
            if board[r][c] == "0":
                continue
            curr = board[r][c]
            if (curr in rows[r] or curr in cols[c] or curr in squares[(r // 3, c //3)]):
                return False
            cols[c].add(curr)
            rows[r].add(curr)
            squares[(r // 3, c // 3)].add(curr)
    return True

# def solve(board):


# Todo: Board input
def board_input():
    board_list = []
    idx = 0
    while idx < BOARD_LENGTH:
        print(f"Row {idx + 1}")
        row = list(input("Enter the numbers in the row, if it is a blank space input a '.': "))
        if len(row) != BOARD_LENGTH:
            print("\nTry again")
            continue
        else:
            board_list.append(row)
            idx += 1
    return board_list

def main():
    # board = [["5","3","7",".",".",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]
    board = board_input()

    print(board)
if __name__ == "__main__":
    main()