# Code for checking is placing n queen posible in n*n chess board and if so one of the possible position

def n_queen(n, row, columns, diag1, diag2, board):
    if row == n:  # All queens are placed successfully
        return True
    
    for col in range(n):
        # Check if the column or diagonal is under attack
        if col in columns or (row - col) in diag1 or (row + col) in diag2:
            continue

        # Place the queen
        columns.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        board[row][col] = 1

        # Recur to place the next queen
        if n_queen(n, row + 1, columns, diag1, diag2, board):
            return True

        # Backtrack: Remove the queen
        columns.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)
        board[row][col] = 0

    return False

def display_2D_array(board):
    for row in board:
        print(" ".join(map(str, row)))

n = int(input())

# Chess board initialization
board = [[0] * n for _ in range(n)]
columns = set()  # Tracks the columns that are under attack
diag1 = set()    # Tracks the major diagonals (row - col)
diag2 = set()    # Tracks the minor diagonals (row + col)

# Start the backtracking process
result = n_queen(n, 0, columns, diag1, diag2, board)
if result:
    display_2D_array(board)
else:
    print("Not possible")
