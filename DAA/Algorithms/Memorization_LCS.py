def lcs_memo(X, Y):
    m, n = len(X), len(Y)
    memo = {}
    def solve(i, j):
        if i == m or j == n:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if X[i] == Y[j]:
            memo[(i, j)] = 1 + solve(i + 1, j + 1)
        else:
            memo[(i, j)] = max(
                solve(i + 1, j),
                solve(i, j + 1)
            )
        return memo[(i, j)]
    return solve(0, 0)
X = "ABCBDAB"
Y = "BDCABA"
print("LCS length =", lcs_memo(X, Y))


