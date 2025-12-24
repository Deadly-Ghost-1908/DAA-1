def knapsack_memo(W, wt, val, n, memo):
    if n == 0 or W == 0:
        return 0
    if (n, W) in memo:
        return memo[(n, W)]
    if wt[n-1] > W:
        memo[(n, W)] = knapsack_memo(W, wt, val, n-1, memo)
    else:
        memo[(n, W)] = max(val[n-1] + knapsack_memo(W - wt[n-1], wt, val, n-1, memo),
                           knapsack_memo(W, wt, val, n-1, memo))
    return memo[(n, W)]
val = [60, 100, 120]
wt = [1, 2, 3]
W = 5
memo = {}
print(knapsack_memo(W, wt, val, len(val), memo))


