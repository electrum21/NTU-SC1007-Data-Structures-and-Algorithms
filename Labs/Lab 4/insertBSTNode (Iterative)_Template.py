class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

def insertBSTNode(root, value):
    """Iterative approach to insert a node into the BST"""
    new_node = BTNode(value)
    
    if root is None:
        return new_node
    
    current = root
    parent = None

    # Traverse the BST to find the parent node, for which the child node will be inserted
    while current is not None:
        parent = current
        if value < current.item:
            current = current.left
        elif value > current.item:
            current = current.right
        else:
            return root

    # This is where the insertion happens, based on comparison with the parent node    
    if value < parent.item:
        parent.left = new_node
    else:
        parent.right = new_node     
    
    return root
    

def printTree(node, level=0, prefix="Root: "):
    """Prints the tree structure for better visualization"""
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

if __name__ == "__main__":
    root = None
    print("Binary Search Tree Insertion Program")
    print("===================================")
    
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:  
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            
        except ValueError:
            print("Please enter a valid integer!")

    print("\nFinal BST structure:")
    printTree(root)