import sys
from collections import deque
def BFS(adjacency_list, start):
    visited = [False]*len(adjacency_list)

    queue = deque()
    queue.append(start)
    visited[start] = True
    result = []

    while queue:
        start = queue.popleft()
        result.append(start)
        for neighbor in adjacency_list[start]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


#example usage:
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
    print("BFS starting from node", start_node, ":", BFS(adjacency_list, start_node))

