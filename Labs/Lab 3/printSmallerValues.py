class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def printSmallerValues(node, m):
    # Check the current node’s value.
    # If it’s strictly smaller than m, print it (with a trailing comma and space).
    # If it’s equal to or greater than m, print nothing and continue.
    if node.item < m:
        print(node.item, end = ", ")

    # Explore the left subtree, then the right subtree.
    # This is a preorder-style check (current node first, then children), though we only “act” (print) based on the condition.
    printSmallerValues(node.left, m)
    printSmallerValues(node.right, m)

if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Tree Structure:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    print()
    
    # Using a hardcoded value instead of input()
    m = 4  # You can change this value for testing
    print(f"\nThe values smaller than {m} are:", end=" ")
    printSmallerValues(root, m)
    print()