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

def postOrderIterativeS2(root):
    if root is None:
        return

    s1 = Stack() # s1 is used for the initial traversal (processing nodes)
    s2 = Stack() # s2 acts as a reverse buffer to store the final post-order sequence

    push(s1, root) # Start by pushing the root node onto the first stack

    # First Loop: Process nodes to build the reverse post-order in s2
    while not is_empty(s1):
        current_node = pop(s1) # Pop the top node from s1 (Current Root)
        push(s2, current_node) # Push the current node to s2. 
        
        # Push children to s1: Left first, then Right.
        # This ensures that Right is on top of s1 and processed before Left.
        # The resulting order in s2 becomes Root -> Right -> Left.
        if current_node.left:
            push(s1, current_node.left)
        if current_node.right:
            push(s1, current_node.right)

    # Second Loop: Print the results from s2
    # Popping s2 reverses the 'Root -> Right -> Left' order into 'Left -> Right -> Root'
    while not is_empty(s2):
        print(pop(s2).data, end=" ")

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the post-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("Post-order traversal: ", end="")
           postOrderIterativeS2(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")