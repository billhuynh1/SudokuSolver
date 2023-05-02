from collections import defaultdict

# class Sudoku:
def is_valid(board) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
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
    for i in range(9):
        print(f"Row {i + 1}")
        board_row = list(input("Enter the row of the board separated by spaces, if the sudoku board has blank squares, input a period: ").split())
        if len(board_row) != 9:
            # check if the board is valid here
            print("Try again")
            board_input()
            continue
        board_list.append(board_row)
    
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

    # list index out of range because for loop runs 9 times
    if is_valid(board_input()):
        print("Valid Board.")
    else:
        print("Not valid.")

if __name__ == "__main__":
    main()