class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

def push(stack, node):
   temp = StackNode(node)
   if stack.top is None:
       stack.top = temp
       temp.next = None
   else:
       temp.next = stack.top
       stack.top = temp

def pop(stack):
   if stack.top is not None:
       temp = stack.top
       stack.top = temp.next
       return temp.data
   return None

def is_empty(stack):
   return stack.top is None

def inorderIterative(root):
    # Initialize an empty stack to keep track of parent nodes
    s = Stack()
    # Start the traversal from the root node
    current_node = root
    
    # Continue as long as there are nodes to visit or nodes left on the stack
    while current_node is not None or not is_empty(s):
        
        # Reach the left-most node of the current subtree
        while current_node is not None:
            # Push the current node onto the stack before moving to its left child
            push(s, current_node)
            current_node = current_node.left
            
        # At this point, current_node is None, so we backtrack by popping from the stack
        current_node = pop(s)
        
        # Process the node's data (the "visit" step)
        print(current_node.data, end = " ")
        
        # We have visited the node and its left subtree; now move to the right subtree
        current_node = current_node.right

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the in-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("In-order traversal: ", end="")
           inorderIterative(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")