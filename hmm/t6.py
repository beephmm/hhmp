tree = {'Left': [3, 5], 'Right': [6, 9]}  

def minimax(node, maximizing):
    if isinstance(node, int):
        return node
    values = [minimax(c, not maximizing) for c in node]
    return max(values) if maximizing else min(values)

move = max(tree, key=lambda m: minimax(tree[m], False))
print(f"Best move: '{move}' with value = {minimax(tree[move], False)}")