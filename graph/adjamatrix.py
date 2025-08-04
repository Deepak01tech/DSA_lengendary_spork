def create_adjacency_matrix(edges, num_nodes):
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for u, v in edges:
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1  # Assuming undirected graph
    return adjacency_matrix

# Example usage:
if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    num_nodes = 6
    adjacency_matrix = create_adjacency_matrix(edges, num_nodes)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)
# This code creates an adjacency matrix from a list of edges for an undirected graph.