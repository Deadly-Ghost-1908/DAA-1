graph = {
    0: [1, 2],
    1: [4],
    2: [5],
    5: [4],
    4: []
}
visited = []
stack = []
def dfs(node):
    if node in visited:
        return
    visited.append(node)
    for neighbor in graph[node]:
        dfs(neighbor)
    stack.append(node)
for node in graph:
    dfs(node)
stack.reverse()
print("Topological Order (DFS):", stack)



