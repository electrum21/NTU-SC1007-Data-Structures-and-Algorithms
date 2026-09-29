class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insertBSTNode(root, value):
    """ Recursive approach to insert a node into a BST. """
    if root is None:
        return BTNode(value)
    if value < root.data:
        root.left = insertBSTNode(root.left, value)
    elif value > root.data:
        root.right = insertBSTNode(root.right, value)
    return root

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.data, end=" ")
        printBSTInOrder(node.right)

def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.data))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

class Solution:
    def kthSmallest(self, root, k):
        # -------- DO NOT MODIFY ANYTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------
        stack = []
        curr = root
        
        # Iterative In-order traversal
        while stack or curr:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the node (this is the next smallest element)
            curr = stack.pop()
            k -= 1
            
            # If k reaches 0, we found the k-th smallest element
            if k == 0:
                return curr.data
            
            # Move to the right child
            curr = curr.right
            
        return -1
        # -------- DO NOT MODIFY ANYTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------

if __name__ == "__main__":
    root = None
    print("BST Kth Smallest Element Program")
    print("=====================================")
    print("\nFirst, let's build the BST:")
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue
            i = int(value)
            if i == -1:
                break
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            print("\nIn-order traversal: ", end="")
            printBSTInOrder(root)
            print()
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nNow let's find kth smallest elements:")
    while True:
        try:
            value = input("\nEnter k to find k-th smallest (-1 to quit): ")
            if not value:
                continue
            k = int(value)
            if k == -1:
                break
            result = kthSmallest(root, k)
            if result != -1:
                print(f"\nThe {k}-th smallest element is: {result}")
            else:
                print("Invalid k or tree is empty!")
        except ValueError:
            print("Invalid input! Please enter an integer.")