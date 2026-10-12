from collections import deque
from math import gcd

def water_jug_bfs(cap1, cap2, target):
    if target > max(cap1, cap2) or target % gcd(cap1, cap2) != 0:
        return None

    start = (0, 0)
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        (j1, j2), path = queue.popleft()

        if j1 == target or j2 == target:
            return path

        possible_states = [
            (cap1, j2),
            (j1, cap2),
            (0, j2),
            (j1, 0),
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1)),
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

if __name__ == "__main__":
    cap1, cap2, target = 4, 3, 2

    solution = water_jug_bfs(cap1, cap2, target)

    if solution:
        print(f"Solution found in {len(solution) - 1} steps:\n")
        for i, state in enumerate(solution):
            print(f"Step {i}: Jug1 = {state[0]}L, Jug2 = {state[1]}L")
    else:
        print("No solution exists for these jug capacities and target.")
