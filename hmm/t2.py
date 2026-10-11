graph = {'A': 'BC', 'B': 'ADE', 'C': 'AFG', 'D': 'B', 'E': 'B', 'F': 'C', 'G': 'C'}

def dfs_recursive(node, visited=None):
    visited = visited if visited is not None else []
    visited.append(node)
    for n in graph[node]:
        if n not in visited:
            dfs_recursive(n, visited)
    return visited

def dfs_iterative(start):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

print("Recursive DFS from A:", *dfs_recursive('A'))
print("Iterative DFS from A:", *dfs_iterative('A'))