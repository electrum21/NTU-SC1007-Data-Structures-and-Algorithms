# ============================================================
#  Q2 — Count Leaf Nodes (Binary Tree)
#
#  Write countLeafNodes(root) — return the NUMBER of nodes
#  that ARE leaves (nodes with no children at all).
#
#  A leaf node: left is None AND right is None.
#  None nodes do NOT count.
#
#  Example tree:
#          4
#        /   \
#       2     6
#      / \   / \
#     1   3 5   7
#
#  Leaves    : 1, 3, 5, 7  -> countLeafNodes(root) = 4
#  Non-leaves: 4, 2, 6     -> not counted here
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, values):
        """Build tree from level-order list. Use None for missing nodes."""
        if not values or values[0] is None:
            return
        self.root = Node(values[0])
        queue = [self.root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1


# ============================================================
#  YOUR SOLUTION HERE
# ============================================================

def countLeafNodes(root):
    if root is None:
        return 0                                   # None guard — must come first

    if root.left is None and root.right is None:
        return 1                                   # leaf — count it

    return countLeafNodes(root.left) + countLeafNodes(root.right)

# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def run_test(label, values, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    bt = BinaryTree()
    bt.insert_level_order(values)
    result = countLeafNodes(bt.root)
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    print(f"  Tree (level-order) : {values}")
    print(f"  Expected           : {expected}")
    print(f"  Your answer        : {result}")
    print(f"  Result             : {status}")

# Test 1 — balanced 7-node tree, 4 leaves
run_test(
    "Test 1: balanced 7-node tree",
    [4, 2, 6, 1, 3, 5, 7],
    expected=4
)

# Test 2 — single node (it IS a leaf)
run_test(
    "Test 2: single node",
    [42],
    expected=1
)

# Test 3 — root with only left child (left child is the only leaf)
run_test(
    "Test 3: root + left child only",
    [1, 2],
    expected=1
)

# Test 4 — empty tree
run_test(
    "Test 4: empty tree (None root)",
    [],
    expected=0
)

# Test 5 — left-skewed chain of 4, only bottom node is a leaf
#    1
#   /
#  2
# /
# 3
# /
# 4
run_test(
    "Test 5: left-skewed chain of 4",
    [1, 2, None, 3, None, 4, None],
    expected=1
)

# Test 6 — root with 4 children (two levels), all 4 bottom nodes are leaves
run_test(
    "Test 6: two-level balanced tree",
    [5, 3, 7, 1, 4, 6, 8],
    expected=4
)
