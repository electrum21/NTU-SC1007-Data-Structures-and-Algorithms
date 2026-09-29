PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        if self.is_empty(): return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped
    
    def peek(self):
        return None if self.is_empty() else self.top.data
    
    def is_empty(self):
        return self.size == 0

def infix_to_prefix(expression):
    # 1. Reverse the expression and swap parentheses
    reversed_exp = []
    for char in reversed(expression):
        if char == '(': reversed_exp.append(')')
        elif char == ')': reversed_exp.append('(')
        else: reversed_exp.append(char)
    
    # 2. Convert reversed infix to a "modified" postfix
    output = []
    operator_stack = Stack()
    
    i = 0
    expr = "".join(reversed_exp)
    while i < len(expr):
        char = expr[i]
        
        if char.isdigit():
            number = ""
            while i < len(expr) and expr[i].isdigit():
                number += expr[i]
                i += 1
            # We reverse the digits of the multi-digit number back to normal
            output.append(number[::-1]) 
            i -= 1
        elif char == '(':
            operator_stack.push(char)
        elif char == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        elif char in PRECEDENCE:
            # Tweak: In Prefix conversion, if precedence is equal, we don't pop
            while (not operator_stack.is_empty() and 
                   operator_stack.peek() != '(' and
                   PRECEDENCE.get(operator_stack.peek(), 0) > PRECEDENCE.get(char, 0)):
                output.append(operator_stack.pop())
            operator_stack.push(char)
        i += 1
        
    while not operator_stack.is_empty():
        output.append(operator_stack.pop())
    
    # 3. Reverse the result to get Prefix
    return " ".join(reversed(output))

def evaluate_prefix(prefix):
    stack = Stack()
    tokens = prefix.split()
    
    # Evaluate from right to left for Prefix
    for token in reversed(tokens):
        if token.isdigit():
            stack.push(int(token))
        else:
            # First pop is Operand 1, second is Operand 2
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+': stack.push(val1 + val2)
            elif token == '-': stack.push(val1 - val2)
            elif token == '*': stack.push(val1 * val2)
            elif token == '/': stack.push(val1 / val2)
            elif token == '^': stack.push(val1 ** val2)
            
    return stack.pop()

if __name__ == "__main__":
    exp = input("Enter infix expression (e.g., (10+2)*3): ")
    prefix = infix_to_prefix(exp)
    print(f"Prefix expression: {prefix}")
    try:
        result = evaluate_prefix(prefix)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")