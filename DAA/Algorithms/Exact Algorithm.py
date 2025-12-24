from itertools import permutations
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    min_path = None
    min_cost = float('inf')
    cities = range(n)
    for perm in permutations(cities):
        cost = sum(distance_matrix[perm[i]][perm[(i+1)%n]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = perm
    return min_path, min_cost
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp_brute_force(distance_matrix)
print("Optimal path:", path)
print("Optimal cost:", cost)



