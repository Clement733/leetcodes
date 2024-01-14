def isValidSudoku(board) -> bool:
        for row in board:
            digits = [d for d in row if d != '.']
            if len(digits) != len(set(digits)):
                return False

        for col in range(9):
            digits = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(digits) != len(set(digits)):
                return False

        for i in range(3):
            for j in range(3):
                digits = [board[row][col] for row in range(3*i, 3*(i+1)) for col in range(3*j, 3*(j+1)) if board[row][col] != '.']
                if len(digits) != len(set(digits)):
                    return False

        return True

if __name__ == "__main__":
    board = []
    for i in range(9):
        lst = list(map(str, input().split()))
        board.append(lst)
    print(isValidSudoku(board))
