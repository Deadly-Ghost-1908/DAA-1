import sys
def matrix_chain_memo(p, n):
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return solve(p, 1, n - 1, dp)
def solve(p, i, j, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = sys.maxsize
    for k in range(i, j):
        cost = (
            solve(p, i, k, dp) +
            solve(p, k + 1, j, dp) +
            p[i - 1] * p[k] * p[j]
        )
        dp[i][j] = min(dp[i][j], cost)
    return dp[i][j]
p = [10, 20, 30, 40, 30]
n = len(p)
print(matrix_chain_memo(p, n))


