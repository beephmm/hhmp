class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children or []
        self.value = value
        self.is_leaf = len(self.children) == 0

def minimax(node, is_maximizing):
    if node.is_leaf:
        return node.value

    if is_maximizing:
        best_value = float('-inf')
        for child in node.children:
            value = minimax(child, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            value = minimax(child, True)
            best_value = min(best_value, value)
        return best_value

def best_move(root):
    best_val = float('-inf')
    best_child = None
    for child in root.children:
        val = minimax(child, False)
        if val > best_val:
            best_val = val
            best_child = child
    return best_child, best_val

leaf_3 = Node("Left-Left", value=3)
leaf_5 = Node("Left-Right", value=5)
leaf_6 = Node("Right-Left", value=6)
leaf_9 = Node("Right-Right", value=9)

Left = Node("Left", children=[leaf_3, leaf_5])
Right = Node("Right", children=[leaf_6, leaf_9])

root = Node("ROOT", children=[Left, Right])

move, value = best_move(root)
print(f"Best move: '{move.name}' with value = {value}")
