elif token == '-':
                stack.push(val1 - val2) # Push result back to stack
            elif token == '*':
                stack.push(val1 * val2) # Push result back to stack
            elif token == '/':
                stack.push(val1 / val2) # Push result back to stack
            elif token == '^':
                stack.push(val1 ** val2) # Push result back to stack