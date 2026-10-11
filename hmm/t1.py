from collections import deque

tree = {'A': 'BC', 'B': 'DE', 'C': 'FG'}

def bfs(root):
    order, queue = [], deque(root)
    while queue:
        node = queue.popleft()
        order.append(node)
        queue.extend(tree.get(node, ''))
    return order

print("BFS Visit Order:", ", ".join(bfs('A')))