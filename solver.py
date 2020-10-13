# Recursive back track function
#


def solve_board(board):
    find = find_empty_cell(board)
    if not find:  # Base case
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_solution(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False


def valid_solution(board, num, pos):
    # Check each coloumn of the row to see if it's already there
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: # Make sure we ignore the cell we just inserted the number into
            return False

    # Check column, same idea as before
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Int division to determine what box we're in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Same idea as earlier, now we're just checking the box instead of columns or rows
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty_cell(board):
    for i in range(len(board)):            # length of col
        for j in range(len(board[0])):     # length of row
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None
