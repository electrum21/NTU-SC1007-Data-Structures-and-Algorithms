class BTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, node=None):
       self.btnode = node
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

   def push(self, node):
       temp = StackNode(node)
       if self.top is None:
           self.top = temp
       else:
           temp.next = self.top
           self.top = temp

   def pop(self):
       if self.top is None:
           return None
       temp = self.top
       self.top = self.top.next
       return temp.btnode

def createBTNode(data):
   return BTNode(data)

def createTree():
   stk = Stack()
   root = None

   item = input("Enter an integer value for the root: ")
   if item.isdigit():
       root = createBTNode(int(item))
       stk.push(root)
   else:
       return None

   while True:
       temp = stk.pop()
       if temp is None:
           break

       item = input(f"Enter an integer value for the Left child of {temp.data}: ")
       if item.isdigit():
           temp.left = createBTNode(int(item))

       item = input(f"Enter an integer value for the Right child of {temp.data}: ")
       if item.isdigit():
           temp.right = createBTNode(int(item))

       if temp.right:
           stk.push(temp.right)
       if temp.left:
           stk.push(temp.left)

   return root

def printTree(node):
   if node is None:
       return
   printTree(node.left)
   print(node.data, end=" ")
   printTree(node.right)

def removeAll(node):
   if node is not None:
       removeAll(node.left)
       removeAll(node.right)
       node = None

def identical(tree1, tree2):
    # Base cases
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False

    # Compare current nodes and recursively check left and right subtrees
    return (tree1.data == tree2.data and 
            identical(tree1.left, tree2.left) and 
            identical(tree1.right, tree2.right))

    #Return true if both trees are identical, false otherwise
    return True

if __name__ == "__main__":
   root1 = None
   root2 = None
   while True:
       print("\n1: Create a binary tree1.")
       print("2: Create a binary tree2.")
       print("3: Check whether two trees are structurally identical.")
       print("0: Quit;")
       
       choice = input("Please input your choice(1/2/3/0): ")

       if choice == '1':
           removeAll(root1)
           print("Creating tree1:")
           root1 = createTree()
           print("The resulting tree1 is: ", end="")
           printTree(root1)
           print()
       elif choice == '2':
           removeAll(root2)
           print("Creating tree2:")
           root2 = createTree()
           print("The resulting tree2 is: ", end="")
           printTree(root2)
           print()
       elif choice == '3':
           if identical(root1, root2):
               print("Both trees are structurally identical.")
           else:
               print("Both trees are different.")
           removeAll(root1)
           removeAll(root2)
       elif choice == '0':
           removeAll(root1)
           removeAll(root2)
           break
       else:
           print("Choice unknown;")
