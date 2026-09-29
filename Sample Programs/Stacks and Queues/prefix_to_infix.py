# Define operator precedence globally
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

class Node:
    """Defines a node for a linked list-based stack"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Implements a stack using a linked list"""
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

def is_operator(char):
    """Check if the character is an operator"""
    return char in PRECEDENCE

def prefix_to_infix(expression):
    """Convert prefix expression to infix"""
    stack = Stack()
    token = expression.split()
    
    for char in token[::-1]:
        if char not in PRECEDENCE and char not in '()':
            stack.push(char)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push('(' + val1 + ' ' + char + ' ' + val2 + ')')

    return stack.pop()


def prefix_to_infix(expression):
    """Convert prefix expression to infix"""
    stack = Stack()
    token = expression.split()
    
    for char in token[::-1]:
        if char not in PRECEDENCE and char not in '()':
            stack.push(char)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push('(' + val1 + ' ' + char + ' ' + val2 + ')')

    return stack.pop()

# Test the function
if __name__ == "__main__":
    prefix_exp = input("Enter a prefix expression: ")
    try:
        infix_exp = prefix_to_infix(prefix_exp)
        print(f"Infix expression: {infix_exp}")
    except ValueError as e:
        print(f"Error: {e}")