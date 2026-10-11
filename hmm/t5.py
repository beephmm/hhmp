import heapq

def greedy_best_first_search(graph, start, goal, h):
    pq, visited = [(h[start], [start])], set()
    while pq:
        _, path = heapq.heappop(pq)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    heapq.heappush(pq, (h[n], path + [n]))

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['G'], 'F': ['G'], 'G': []}
h = {'A': 6, 'B': 4, 'C': 4, 'D': 5, 'E': 2, 'F': 1, 'G': 0}

print("Path found:", greedy_best_first_search(graph, 'A', 'G', h))