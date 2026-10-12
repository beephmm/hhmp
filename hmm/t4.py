import heapq

def astar(graph, start, goal, h):
    open_set = [(h[start], start, [start], 0)]

    while open_set:
        f, node, path, g = heapq.heappop(open_set)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            new_g = g + cost
            heapq.heappush(open_set, (new_g + h[neighbor], neighbor, path + [neighbor], new_g))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 6)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

h = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}

path, cost = astar(graph, 'A', 'G', h)
print("Path:", path)
print("Cost:", cost)
