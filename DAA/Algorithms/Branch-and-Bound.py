def knapsack(values, weights, W):
    n = len(values)
    def bound(i, w, p):
        if w >= W: return 0
        b = p
        while i < n and w + weights[i] <= W:
            w += weights[i]
            b += values[i]
            i += 1
        if i < n:
            b += (W - w) * (values[i] / weights[i])
        return b
    best = 0
    stack = [(0, 0, 0)]
    while stack:
        i, w, p = stack.pop()
        if i == n: continue
        w1, p1 = w + weights[i], p + values[i]
        if w1 <= W:
            best = max(best, p1)
            if bound(i+1, w1, p1) > best:
                stack.append((i+1, w1, p1))
        if bound(i+1, w, p) > best:
            stack.append((i+1, w, p))
    return best
print("Max Profit:", knapsack([60,100,120], [10,20,30], 50))





