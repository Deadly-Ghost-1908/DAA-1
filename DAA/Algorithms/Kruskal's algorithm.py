import heapq
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
        return True
    return False
def kruskals_min_heap(V, edges):
    heapq.heapify(edges)
    parent = [i for i in range(V)]
    rank = [0] * V
    mst = []
    total_weight = 0
    while edges and len(mst) < V - 1:
        weight, u, v = heapq.heappop(edges)
        if union(parent, rank, u, v):  
            mst.append((u, v, weight))
            total_weight += weight
    print("MST Edges:", mst)
    print("Total Minimum Cost:", total_weight)
edges = [
    (2, 0, 1),
    (3, 1, 2),
    (6, 0, 3),
    (8, 1, 3),
    (5, 1, 4),
    (7, 2, 4)
]
V = 5
kruskals_min_heap(V, edges)


