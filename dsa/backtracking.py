# Code for checking is placing n queen posible in n*n chess board and if so one of the possible position

def is_attacked(x, y, board):
    # checking queen attacks from row and col of that position
    for i in range(rows):
        if board[i][y] == 1 or board[x][i] == 1:
            return True

    #checking both diagonals. want a suggestion for better checking with time complexity O(N)
    i = x-1
    j = y+1
    while i > -1 and j < rows:
        if board[i][j] == 1:
            return True
        i-=1
        j+=1
    i = x-1
    j = y-1
    while i > -1 and j > -1:
        if board[i][j] == 1:
            return True
        i-=1
        j-=1
    i = x+1
    j = y+1
    while i < rows and j < rows:
        if board[i][j] == 1:
            return True
        i+=1
        j+=1
    i = x+1
    j = y-1
    while i < rows and j > -1:
        if board[i][j] == 1:
            return True
        i+=1
        j-=1

    return False         

def n_queen(n, board):
    if n == 0:
        return True
    for i in range(rows):
        for j in range(cols):
            if is_attacked(i, j, board): #if queen present going to next iteration
                continue
            board[i][j] = 1 
            if n_queen(n-1, board): #backtracking
                return True
            board[i][j] = 0
    return False

def display_2D_array(board):
    for row in board:
        print(" ".join(map(str, row)))

n = int(input())

# chess board
rows = n
cols = n
board = [[0] * cols for _ in range(rows)]

result = n_queen(n, board)
print("YES" if result else "NO")
if result:
    display_2D_array(board)

