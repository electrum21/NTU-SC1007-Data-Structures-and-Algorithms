class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def printBTNode(self,space,left):
        if self.root is None:
            return
        else:
            self._printBTNode(self.root,space,left)

    def _printBTNode(self, node, space, left):
        if node is not None:
            # Print preceding spaces/branches
            for i in range(space - 1):
                print("|\t", end="")

            # Determine and print branch connectors for left/right child
            if space > 0:
                if left == 1:
                    print("|---", end="")
                else:
                    print("|___", end="")

            # Print the current node's item
            print(node.data)

            # Increment space for next level
            space += 1

            # Recursively print the left and right subtrees
            self._printBTNode(node.left, space, 1)   # left child
            self._printBTNode(node.right, space, 0)  # right child
            
    def sumGreaterTree(self):
        if self.root is None:
            return
        else:
            sum = 0
            self._sumGreaterTree(self.root, sum)


    '''
    self._sumGreaterTree(node.right, current_sum): The code dives as far right as possible first. It doesn't do any math until it reaches the very end of the right branch.
    current_sum += node.data: As the recursion "unwinds" (moves back up from the right), it adds the current node to the total accumulated from everything to its right.
    node.data = current_sum: It overwrites the node immediately.
    return self._sumGreaterTree(node.left, current_sum): Finally, it carries that new, larger sum into the left subtree, where all the smaller values live.
    '''
    def _sumGreaterTree(self, node, sum):
        if node is None:
            return sum

        # 1. Visit the Right child (larger values) first
        # Update current_sum with the results from the right subtree
        sum = self._sumGreaterTree(node.right, sum)
        
        # 2. Process the Current Node
        # Add this node's original data to the running sum
        sum += node.data
        node.data = sum

        # 3. Visit the Left child (smaller values)
        # Pass the updated current_sum down to the left subtree
        return self._sumGreaterTree(node.left, sum)


bt = BinaryTree()

values = input().split()
for i in values:
    bt.insert(int(i))

bt.printBTNode(0,0)
print()
bt.sumGreaterTree()
bt.printBTNode(0,0)