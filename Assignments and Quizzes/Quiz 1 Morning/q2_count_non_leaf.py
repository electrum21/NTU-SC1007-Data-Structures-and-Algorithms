# ============================================================
#  Q2 — Count Non-Leaf Nodes (Binary Tree)
#
#  Write countNonLeafNodes(root) — return the NUMBER of nodes
#  that are NOT leaves (i.e. internal nodes that have at least
#  one child).
#
#  A leaf node has no children (left is None AND right is None).
#  None nodes do NOT count.
#
#  Example tree:
#          4
#        /   \
#       2     6
#      / \   / \
#     1   3 5   7
#
#  Leaves    : 1, 3, 5, 7  (4 nodes)
#  Non-leaves: 4, 2, 6     (3 nodes)
#  countNonLeafNodes(root) → 3
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

def countNonLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + countNonLeafNodes(root.left) + countNonLeafNodes(root.right)


# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def run_test(label, values, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    bt = BinaryTree()
    bt.insert_level_order(values)
    result = countNonLeafNodes(bt.root)
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    print(f"  Tree (level-order) : {values}")
    print(f"  Expected           : {expected}")
    print(f"  Your answer        : {result}")
    print(f"  Result             : {status}")

# Test 1 — balanced tree, 3 non-leaves
run_test(
    "Test 1: balanced 7-node tree",
    [4, 2, 6, 1, 3, 5, 7],
    expected=3
)

# Test 2 — single node (it's a leaf, so 0 non-leaves)
run_test(
    "Test 2: single node",
    [42],
    expected=0
)

# Test 3 — root with only left child (root is non-leaf, child is leaf)
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

# Test 5 — deeper unbalanced tree
#        1
#       /
#      2
#     /
#    3
#   /
#  4
run_test(
    "Test 5: left-skewed chain of 4",
    [1, 2, None, 3, None, 4, None],
    expected=3    # 1, 2, 3 are non-leaves; 4 is a leaf
)

# Test 6 — all leaves except root
run_test(
    "Test 6: root with 4 children (two levels)",
    [5, 3, 7, 1, 4, 6, 8],
    expected=3    # 5, 3, 7 are non-leaves
)
