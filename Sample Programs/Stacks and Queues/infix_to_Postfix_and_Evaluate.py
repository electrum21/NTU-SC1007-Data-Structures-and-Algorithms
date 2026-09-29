# Define operator precedence globally
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

class Node:
    def __init__(self, data):
        # Initialize a node with data and null next pointer
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Initialize an empty stack with no elements
        self.top = None
        self.size = 0
    
    def push(self, data):
        # Add a new element to the top of the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        # Remove and return the top element of the stack
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped
    
    def peek(self):
        # Return the top element without removing it
        return None if self.is_empty() else self.top.data
    
    def is_empty(self):
        # Check if the stack has no elements
        return self.size == 0

def is_operand(char):
    # Check if a character is a letter or digit
    return char.isalnum()

def has_higher_precedence(op1, op2, precedence=PRECEDENCE):
    # Compare precedence of two operators using the global precedence
    return precedence.get(op1, 0) >= precedence.get(op2, 0)

def infix_to_postfix(expression):
    output = ""
    operator_stack = Stack()
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # Handle multi-digit numbers
        if char.isdigit():
            number = ""
            while i < len(expression) and expression[i].isdigit(): # Handle multi-digit numbers
                number += expression[i] # Append digit to number
                i += 1
            output += number + " " 
            i -= 1   # Adjust index since it will be incremented in the loop
        elif char == '(':  # If character is '(', push to stack
            operator_stack.push(char)
        elif char == ')': # If character is ')', pop until '('
            while not operator_stack.is_empty() and operator_stack.peek() != '(': # Pop until '('
                output += operator_stack.pop() + " " # Append popped operator to output
            
            if not operator_stack.is_empty() and operator_stack.peek() == '(': # Pop the '(' from stack
                operator_stack.pop()
        elif char in PRECEDENCE:  # Check if character is an operator
            while (not operator_stack.is_empty() and 
                   operator_stack.peek() != '(' and
                   has_higher_precedence(operator_stack.peek(), char)): # While top of stack has higher precedence than current operator
                output += operator_stack.pop() + " " # Append popped operator to output
            
            operator_stack.push(char)
        
        i += 1
    
    while not operator_stack.is_empty():
        output += operator_stack.pop() + " "
    
    return output.strip()

def evaluate_postfix(postfix):
    stack = Stack()
    tokens = postfix.split()
    
    for token in tokens:
        if token.isdigit(): # If token is an operand, push to stack
            stack.push(int(token))
        else: # Token is an operator
            val2 = stack.pop() # Pop two operands
            val1 = stack.pop() # Pop two operands
            if token == '+':
                stack.push(val1 + val2) # Push result back to stack
            elif token == '-':
                stack.push(val1 - val2) # Push result back to stack
            elif token == '*':
                stack.push(val1 * val2) # Push result back to stack
            elif token == '/':
                stack.push(val1 / val2) # Push result back to stack
            elif token == '^':
                stack.push(val1 ** val2) # Push result back to stack
    
    return stack.pop()


def postfix_to_infix(postfix):
    stack = Stack()
    tokens = postfix.split()


    for token in tokens:
        if token.isdigit():
            stack.push(token)
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            stack.push('(' + val1 + " " + token + " " + val2 + ')')
    
    return stack.pop()

def postfix_to_prefix(postfix):
    stack = Stack()
    tokens = postfix.split()


    for token in tokens:
        if token.isdigit():
            stack.push(token)
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            stack.push(token + " " + val1 + " " + val2)
    
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

def prefix_to_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens[::-1]:
        if token not in PRECEDENCE and token not in '()':
            stack.push(token)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(val1 + ' ' + val2 + ' ' + token)
    
    return stack.pop()

if __name__ == "__main__":
    # Main program entry point for user interaction
    exp = input("Enter infix expression: ")
    postfix = infix_to_postfix(exp)
    print(f"Postfix after Infix: {postfix}")
    # try:
    result = evaluate_postfix(postfix)
    infix = postfix_to_infix(postfix)
    prefix = postfix_to_prefix(postfix)
    print(f"Prefix after Postfix: {prefix}")
    print(f"Infix after Postfix: {infix}")
    infix = prefix_to_infix(prefix)
    postfix = prefix_to_postfix(prefix)
    print(f"Postfix after Prefix: {postfix}")
    print(f"Infix after Prefix: {infix}")
    print(f"Result: {result}")
    # except Exception as e:
    #     print(f"Error evaluating expression: {e}")
    #     print("Make sure the expression contains valid numbers and operators.")