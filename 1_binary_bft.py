from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    queue = deque()
    queue.append(root)
    values = []

    while queue:
        current = queue.popleft()
        values.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return values

# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 6, 3, 9