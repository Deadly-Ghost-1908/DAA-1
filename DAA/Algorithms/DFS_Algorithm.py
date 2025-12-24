def dfs(graph, start):
    visited=set()
    stack=[start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
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

dfs(graph,1)