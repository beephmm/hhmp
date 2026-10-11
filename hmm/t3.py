from collections import deque
from math import gcd

def water_jug_bfs(c1, c2, target):
    if target > max(c1, c2) or target % gcd(c1, c2):
        return None
    queue, seen = deque([[(0, 0)]]), {(0, 0)}
    while queue:
        path = queue.popleft()
        a, b = path[-1]
        if target in (a, b):
            return path
        p1, p2 = min(a, c2 - b), min(b, c1 - a)
        for s in [(c1, b), (a, c2), (0, b), (a, 0), (a - p1, b + p1), (a + p2, b - p2)]:
            if s not in seen:
                seen.add(s)
                queue.append(path + [s])

sol = water_jug_bfs(4, 3, 2)
if sol:
    print(f"Solution found in {len(sol) - 1} steps:\n")
    for i, (a, b) in enumerate(sol):
        print(f"Step {i}: Jug1 = {a}L, Jug2 = {b}L")
else:
    print("No solution exists for these jug capacities and target.")