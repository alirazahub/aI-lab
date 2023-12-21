class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Example tree:
#        3
#      / | \
#     5  2  9
#    /|\    |
#   1 8 4   7

leaf1 = TreeNode(1)
leaf2 = TreeNode(8)
leaf3 = TreeNode(4)
leaf4 = TreeNode(7)

subtree1 = TreeNode(5, [leaf1, leaf2, leaf3])
subtree2 = TreeNode(2)
subtree3 = TreeNode(9, [leaf4])

root = TreeNode(3, [subtree1, subtree2, subtree3])

# Applying Alpha-Beta Pruning
result = alpha_beta_pruning(root, 3, float('-inf'), float('inf'), True)
print("Result:", result)
