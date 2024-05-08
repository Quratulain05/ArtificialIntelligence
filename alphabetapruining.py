class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def alpha_beta_pruning(values, level, alpha=float('-inf'), beta=float('inf'), is_max=True):
    if level == 0 or not values:
        return TreeNode(values[0])

    value = float('-inf') if is_max else float('inf')
    for _ in range(min(3, len(values))):
        child = alpha_beta_pruning(values[1:], level - 1, alpha, beta, not is_max)
        if is_max:
            value = max(value, child.value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        else:
            value = min(value, child.value)
            beta = min(beta, value)
            if beta <= alpha:
                break

    node = TreeNode(value)
    node.children.append(child)
    return node

def print_tree(node, level=0):
    if node:
        print('  ' * level + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)

# Test the code
leaf_values = [7, 4, 3, 8, 2, 6, 5, 1, 9]
root = alpha_beta_pruning(leaf_values, 2)
print("Alpha-Beta Pruning Tree:")
print_tree(root)
