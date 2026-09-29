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

    reversed_expr = []
    for char in expression[::-1]:
        if char == '(':
            reversed_expr.append(')')
        elif char == ')':
            reversed_expr.append('(')
        else:
            reversed_expr.append(char)

    expr = "".join(reversed_expr)

    output = Stack()
    op_stack = Stack()

    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit():
            number = ""
            while i < len(expr) and expr[i].isdigit():
                number += expr[i]
                i += 1
            output.push(number[::-1])
            i -= 1
        elif char == '(':
            op_stack.push('(')
        elif char == ')':
            while not op_stack.is_empty() and op_stack.peek() != '(':
                output.push(op_stack.pop())
            op_stack.pop()
        else:
            while not op_stack.is_empty() and op_stack.peek() != '(' and PRECEDENCE[op_stack.peek()] > PRECEDENCE[char]:
                output.push(op_stack.pop())
            op_stack.push(char)
        i += 1
    
    while not op_stack.is_empty():
        output.push(op_stack.pop())
    
    return output


# def evaluate_prefix(prefix):



if __name__ == "__main__":
    exp = input("Enter infix expression (e.g., (10+2)*3): ")
    prefix_stack = infix_to_prefix(exp)
    print("Prefix Expression: ")
    prefix = ""
    while not prefix_stack.is_empty():
        prefix = prefix + prefix_stack.pop() + " "
    print(prefix)
    # try:
    #     result = evaluate_prefix(prefix)
    #     print(f"Result: {result}")
    # except Exception as e:
    #     print(f"Error: {e}")