import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
graph = {
    0: [(1, 4), (2, 8)],
    1: [(4, 6)],
    2: [(3, 2)],
    3: [(4, 10)],
    4: []
}
source = 0
shortest_distances = dijkstra(graph, source)
print(f"Shortest distances from source vertex {source}:")
for node, distance in shortest_distances.items():
    print(f"Vertex {node} → Distance = {distance}")




    