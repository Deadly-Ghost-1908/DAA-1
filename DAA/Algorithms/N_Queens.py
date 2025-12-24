def is_safe(board, r, c, n):
    for i in range(r):
        if board[i] == c or abs(board[i] - c) == abs(i - r):
            return False
    return True
def solve(row, board, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(row + 1, board, n, solutions)
n = 4
board = [-1] * n
sol = []
solve(0, board, n, sol)
print("Total:", len(sol))
for s in sol:
    print(s)



