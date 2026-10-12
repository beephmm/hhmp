from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.children = [B, C]
B.children = [D, E]
C.children = [F, G]

def bfs(root):
    visit_order = []
    queue = deque([root])            

    while queue:
        node = queue.popleft()       
        visit_order.append(node.value)

        for child in node.children:
            queue.append(child)     

    return visit_order

print("BFS Visit Order:", ", ".join(bfs(A)))
