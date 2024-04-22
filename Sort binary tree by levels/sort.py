from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    output = []
    current = node
    temp = deque()
    temp.append(current)
    while temp:
        current = temp.popleft()
        if current.left:
            temp.append(current.left)
        if current.right:
            temp.append(current.right)
        output.append(current.value)
    return output