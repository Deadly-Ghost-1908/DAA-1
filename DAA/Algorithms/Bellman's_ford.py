V = 4  
edges = [
    (1, 2, 4),
    (1, 4, 5),
    (4, 3, 3),
    (3, 2, -10)
]
def bellman_ford(V, edges, src):
    dist = {i: float('inf') for i in range(1, V+1)}
    dist[src] = 0
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            return
    print("Vertex\tDistance from Source")
    for vertex in range(1, V + 1):
        print(f"{vertex}\t{dist[vertex]}")
bellman_ford(V, edges, src=1)



