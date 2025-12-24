import networkx as nx
def tsp_mst_approx(distance_matrix):
    n = len(distance_matrix)
    G = nx.Graph()
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(i, j, weight=distance_matrix[i][j])
    mst = nx.minimum_spanning_tree(G)
    pre_order = list(nx.dfs_preorder_nodes(mst, source=0))
    approx_cost = sum(distance_matrix[pre_order[i]][pre_order[(i+1)%n]] for i in range(n))
    return pre_order, approx_cost
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp_mst_approx(distance_matrix)
print("Approximate path:", path)
print("Approximate cost:", cost)



