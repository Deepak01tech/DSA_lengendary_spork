
def Dfs(adjacency_list, start_node):
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add unvisited neighbors to the stack
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

# Example usage:
if __name__ == "__main__":
    adjacency_list = [
        [1, 2],
        [0, 3, 4],
        [0, 5],
        [1],
        [1],
        [2]
    ]
    start_node = 0
    print("DFS starting from node", start_node, ":", Dfs(adjacency_list, start_node))
