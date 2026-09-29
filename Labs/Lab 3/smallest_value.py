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

def smallest_value(node):

    # If the function is called with an empty node (None), it means there is no value here.
    # We return float('inf') (infinity), which is bigger than any real number in the tree.
    if node is None:
        return float('inf')
    
    # Recursively go down the left and right child of the current node.
    # The recursion continues until it either finds a leaf or a None.
    left_smallest = smallest_value(node.left)
    right_smallest = smallest_value(node.right)

    # At each node, we compare three values:
    # - The value stored in the current node (node.item)
    # - The smallest value in the left subtree
    # - The smallest value in the right subtree
    # The min() function ensures that the smallest among the three is returned upward in the recursion.
    return min(node.item, left_smallest, right_smallest)

if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.left = None
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Tree Structure:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    print()
    
    print("\nThe smallest value in the tree is:", smallest_value(root))