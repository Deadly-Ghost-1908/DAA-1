import heapq
def prims_min_heap(graph, start=0):
    visited = set()
    min_heap = [(0, start)]
    total_weight = 0
    mst_edges = []
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_weight += weight
        for neighbor, wt in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (wt, neighbor))
                mst_edges.append((node, neighbor, wt))
    print("MST Edges:", mst_edges)
    print("Total Minimum Cost:", total_weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}
prims_min_heap(graph)






