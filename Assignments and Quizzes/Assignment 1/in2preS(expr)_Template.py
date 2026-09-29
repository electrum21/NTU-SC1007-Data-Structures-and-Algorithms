# Define operator precedence globally 
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data

def in2preS(expr):
    def tokenize(tokens):
        """Separate parentheses and operators from operands if they're attached"""
        result = []
        for token in tokens:
            i = 0
            while i < len(token):
                if token[i] in '()':
                    result.append(token[i])
                    i += 1
                elif token[i].isdigit():
                    # Extract the full number
                    num = ''
                    while i < len(token) and token[i].isdigit():
                        num += token[i]
                        i += 1
                    result.append(num)
                elif i < len(token) - 1 and token[i:i+2] == '**':
                    result.append('**')
                    i += 2
                elif token[i] in '+-*/':
                    result.append(token[i])
                    i += 1
                else:
                    i += 1
        return result
    
    def is_operator(token):
        return token in PRECEDENCE
    
    def is_operand(token):
        return token.isdigit()
    
    # Tokenize properly (handle parentheses attached to numbers)
    tokens = tokenize(expr)
    
    # Reverse the expression and swap parentheses
    reversed_expr = []
    for token in reversed(tokens):
        if token == '(':
            reversed_expr.append(')')
        elif token == ')':
            reversed_expr.append('(')
        else:
            reversed_expr.append(token)
    
    # Convert reversed infix to postfix
    operator_stack = Stack()
    postfix = []
    
    for token in reversed_expr:
        if is_operand(token):
            # Operand goes directly to output
            postfix.append(token)
        elif token == '(':
            # Opening parenthesis goes to stack
            operator_stack.push(token)
        elif token == ')':
            # Closing parenthesis: pop until we find opening
            while not operator_stack.isEmpty() and operator_stack.peek() != '(':
                postfix.append(operator_stack.peek())
                operator_stack.pop()
            if not operator_stack.isEmpty():
                operator_stack.pop()  # Remove the '('
        elif is_operator(token):
            # For reversed infix: pop only if stack top has STRICTLY greater precedence
            while (not operator_stack.isEmpty() and 
                   operator_stack.peek() != '(' and
                   is_operator(operator_stack.peek())):
                stack_op = operator_stack.peek()
                if PRECEDENCE[stack_op] > PRECEDENCE[token]:
                    postfix.append(operator_stack.peek())
                    operator_stack.pop()
                else:
                    break
            
            operator_stack.push(token)
    
    # Pop all remaining operators
    while not operator_stack.isEmpty():
        postfix.append(operator_stack.peek())
        operator_stack.pop()
    
    # Reverse the postfix to get prefix
    prefix_list = list(reversed(postfix))
    
    # Create result stack (push in reverse so popping gives correct order)
    result_stack = Stack()
    for token in reversed(prefix_list):
        result_stack.push(token)
    
    return result_stack
    


if __name__ == "__main__":
    infix = input("Enter infix expression: ")
    prefix = in2preS(list(infix.split(' ')))
    
    # Print the prefix expression
    result = ""
    while not prefix.isEmpty():
        result += prefix.peek()
        prefix.pop()
    
    print(f"Prefix expression: {result}")