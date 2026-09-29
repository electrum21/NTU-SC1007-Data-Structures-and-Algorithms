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
    def findLCA(self, root, p, q):
        if root.data > p and root.data > q:  # Both values are smaller than the root
            return self.findLCA(root.left, p, q)  # Move to the left subtree
        elif root.data < p and root.data < q:  # Both values are larger than the root
            return self.findLCA(root.right, p, q)  # Move to the right subtree
        else:  # One value on each side, or root itself is one of the values
            return root.data  # The current node is the LCA

if __name__ == "__main__":
    root = None
    print("BST Lowest Common Ancestor Program")
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

    print("\nNow let's find lowest common ancestors:")
    while True:
        try:
            p = input("\nEnter first node value p (-1 to quit): ")
            if not p:
                continue
            p = int(p)
            if p == -1:
                break
            q = input("Enter second node value q: ")
            if not q:
                continue
            q = int(q)
            result = Solution().findLCA(root, p, q)
            if result != -1:
                print(f"\nThe LCA of {p} and {q} is: {result}")
            else:
                print("One or both values not found in the tree!")
        except ValueError:
            print("Invalid input! Please enter an integer.")