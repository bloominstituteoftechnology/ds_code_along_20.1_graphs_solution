from collections import deque

def traverse(graph, root):
    queue = deque()
    queue.append(root)
    values = []

    visited = set()
    visited.add(root)

    while queue:
        # Dequeue a vertex from queue
        current = queue.popleft()
        values.append(current)

        # If not yet visited, mark it as visited, and enqueue it
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return values

# Test cases
# We'll be using this simple undirected graph to test our BFT:
# 5 -- 3
# | \
# |  2
# | / \
# 1    4
graph = {1: [2, 5], 2: [1, 4, 5], 3: [5], 4: [2], 5: [1, 2, 3]}
print(traverse(graph, 1)) # 1, 2, 5, 4, 3
print(traverse(graph, 4)) # 4, 2, 1, 5, 3
print(traverse(graph, 5)) # 5, 1, 2, 3, 4