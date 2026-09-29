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
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
def precedence(op):
    if op == '**':
        return 3 
    elif op in '*/':
        return 2
    elif op in '+-':
        return 1
    else:
        return -1

def in2postS(expr):
    op_stack = Stack()
    output = Stack()

    for token in expr:
        # Case 1: operand (number OR variable)
        if token not in PRECEDENCE and token not in ('(', ')'):
            output.push(token)

        # Case 2: left parenthesis
        elif token == '(':
            op_stack.push(token)

        # Case 3: right parenthesis
        elif token == ')':
            while (not op_stack.isEmpty() and
                   op_stack.peek() != '('):
                output.push(op_stack.pop())
            if not op_stack.isEmpty():
                op_stack.pop()  # remove '('

        # Case 4: operator
        else:
            while (not op_stack.isEmpty() and
                   op_stack.peek() != '(' and
                   PRECEDENCE[op_stack.peek()] >= PRECEDENCE[token]):
                output.push(op_stack.pop())
            op_stack.push(token)

    # Pop remaining operators
    while not op_stack.isEmpty():
        output.push(op_stack.pop())

    return output

if __name__ == "__main__":
    infix = input("Enter infix expression (space separated): ")
    postfix = in2postS(list(infix.split(' ')))

    # Reverse stack to print in correct postfix order
    temp = Stack()
    while not postfix.isEmpty():
        temp.push(postfix.pop())

    result = ""
    while not temp.isEmpty():
        result += temp.pop() + " "

    print("Postfix expression:", result.strip())