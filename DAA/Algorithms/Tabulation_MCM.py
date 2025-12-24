import sys
def matrix_chain_tab(p, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = (
                    dp[i][k] + 
                    dp[k + 1][j] + 
                    p[i - 1] * p[k] * p[j]
                )
                dp[i][j] = min(dp[i][j], cost)
    return dp[1][n - 1]
p = [10, 20, 30, 40, 30]
n = len(p)
print(matrix_chain_tab(p, n))

