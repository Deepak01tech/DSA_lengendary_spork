from collections import defaultdict

def create_adjacency_list(edges):
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # Assuming undirected graph
    return adjacency_list

# Example usage:
if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    adjacency_list = create_adjacency_list(edges)
    print("Adjacency List:", dict(adjacency_list))