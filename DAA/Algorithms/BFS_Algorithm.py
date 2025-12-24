from collections import deque
def bfs(graph, start):
    visited=set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    1: [4, 5],
    2: [4, 5],
    3: [4, 2, 6, 5],
    4: [1, 9, 3],
    5: [1, 3, 2],
    6: [3],
    7: [8, 9],
    8: [7],
    9: [4, 7]
}

bfs(graph,1)