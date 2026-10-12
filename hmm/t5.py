import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic[start], start)]
    came_from = {start: None}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                came_from.setdefault(neighbor, current)
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }

    heuristic = {
        'A': 6, 'B': 4, 'C': 4,
        'D': 5, 'E': 2, 'F': 1, 'G': 0
    }

    path = greedy_best_first_search(graph, 'A', 'G', heuristic)
    print("Path found:", path)
