class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
   
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
   
    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped
   
    def peek(self):
        return None if self.is_empty() else self.top.data
   
    def is_empty(self):
        return self.size == 0

def pre_order_traversal(node):
    if not node:
        return
    s = Stack()
    current = node
    s.push(current)

    while not s.is_empty():
        current = s.pop()
        print(current.data, end = " ")
        if current.right:
            s.push(current.right)
        if current.left:
            s.push(current.left)


def in_order_traversal(node):
    if not node:
        return
    s = Stack()
    current = node

    while current or not s.is_empty():
        while current:
            s.push(current)
            current = current.left
        current = s.pop()
        print(current.data, end = " ")
        current = current.right

def post_order_traversal(node):
    if not node:
        return

    s1 = Stack()
    s2 = Stack()

    current = node
    s1.push(current)

    while not s1.is_empty():
        current = s1.pop()
        s2.push(current)

        if current.left:
            s1.push(current.left)
        if current.right:
            s2.push(current.right)
        
    while not s2.is_empty():
        print(s2.pop().data, end = " ")


# Example usage:
if __name__ == "__main__":
    # Creating a sample tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Pre-Order Traversal:")
    pre_order_traversal(root)
    print("\nIn-Order Traversal:")
    in_order_traversal(root)
    print("\nPost-Order Traversal:")
    post_order_traversal(root)
