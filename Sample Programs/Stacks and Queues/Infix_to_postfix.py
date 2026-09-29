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

def has_higher_precedence(op1, op2):
    """Check if op1 has higher or equal precedence to op2"""
    if op1 not in PRECEDENCE or op2 not in PRECEDENCE:
        return False
    return PRECEDENCE[op1] >= PRECEDENCE[op2] # >= is important

def infix_to_postfix(expression):
    if expression == "":
        return
    
    output = Stack()
    op_stack = Stack()

    for char in expression:
        if char not in PRECEDENCE and char not in '()':
            output.push(char)
        elif char == '(':
            op_stack.push(char)
        elif char == ')':
            while op_stack.peek() != '(' and not op_stack.is_empty():
                output.push(op_stack.pop())
            if op_stack.peek() == '(':
                op_stack.pop()
        else:
            while op_stack.peek() != '(' and not op_stack.is_empty() and has_higher_precedence(op_stack.peek(), char):
                output.push(op_stack.pop())
            op_stack.push(char)
    
    while not op_stack.is_empty():
        output.push(op_stack.pop())

    return output

# Test the function
if __name__ == "__main__":
    infix_exp = input("Enter an infix expression: ")
    try:
        reverse_output = Stack()
        postfix_exp = infix_to_postfix(infix_exp)
        while postfix_exp.is_empty() == False:
            reverse_output.push(postfix_exp.pop())
        while reverse_output.is_empty() == False:
            print(reverse_output.pop(), end = "")
    except ValueError as e:
        print(f"Error: {e}")