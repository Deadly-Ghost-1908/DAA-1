from collections import deque
graph = {
    0: [1, 2],
    1: [4],
    2: [5],
    5: [4],
    4: []
}
indegree = {node: 0 for node in graph}
for node in graph:
    for neigh in graph[node]:
        indegree[neigh] += 1
queue = deque([node for node in indegree if indegree[node] == 0])
topo_order = []
while queue:
    node = queue.popleft()
    topo_order.append(node)
    for neigh in graph[node]:
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            queue.append(neigh)
print("Topological Order (BFS / Kahn):", topo_order)



