def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    val[i - 1] + dp[i - 1][w - wt[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

result = knapsack(capacity, weights, values, n)
print("Maximum value in Knapsack:", result)