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

def hasGreatGrandchild(node):
    if node is None:
        return -1 # If the node doesn’t exist (None), return -1. 
        # This trick helps: when you calculate height, a leaf node ends up with height 0 (since both its children return -1, and max(-1,-1)+1 = 0).

    # Recursively call the function on the left and right subtrees. These calls return the heights of the left and right subtrees.
    left_height = hasGreatGrandchild(node.left)
    right_height = hasGreatGrandchild(node.right)
    
    # Take the taller side’s height. This tells us how many levels exist below this node.
    max_height = max(left_height, right_height)
    
    if max_height > 1: # If the maximum depth below this node is greater than 1, it means this node has a descendant at least 3 levels down → a great-grandchild exists.
        print(node.item, end=" ")
    return max_height + 1 # Add 1 to include the current node in the height count. This ensures the parent receives the correct height of this subtree.
if __name__ == "__main__":
    # Create a tree with nodes having great-grandchildren
    root = BTNode(1)
    
    # Left subtree
    root.left = BTNode(2)
    root.left.left = BTNode(4)
    root.left.left.left = BTNode(8)
    root.left.left.left.left = BTNode(16)
    
    # Right subtree  
    root.right = BTNode(3)
    root.right.right = BTNode(7)
    root.right.right.right = BTNode(15)
    root.right.right.right.right = BTNode(31)

    print("Visual representation of the tree:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    
    print("\nNodes with great-grandchildren:", end=" ")
    hasGreatGrandchild(root)
    print()