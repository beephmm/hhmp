import heapq

def astar(graph, start, goal, h):
    pq = [(h[start], 0, [start])]  
    while pq:
        f, g, path = heapq.heappop(pq)
        if path[-1] == goal:
            return path, g
        for nxt, cost in graph[path[-1]]:
            heapq.heappush(pq, (g + cost + h[nxt], g + cost, path + [nxt]))
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

path, cost = astar(graph, 'A', 'G', dict.fromkeys(graph, 0))
print("Path:", path)
print("Cost:", cost)