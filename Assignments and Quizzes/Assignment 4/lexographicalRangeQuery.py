class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling
        if curr and curr.char == char:
            return curr
        return None

    def _insert_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        if curr and curr.char == char:
            return curr  # already exists

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:
            node.first_child = new_node
        return new_node

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False  # Character path not found
        return node.is_end_of_word
    
    def insert(self, word):
        current = self.root
        for char in word:
            child = self._insert_child(current, char)
            current = child
        current.is_end_of_word = True
        
def count_in_range(trie, L, R): # L and R are strings
    count = 0
    # The stack stores tuples of (node, current_prefix)
    stack = Stack()
    stack.push((trie.root, ""))

    while not stack.is_empty():
        node, prefix = stack.pop()

        # Check if the current node completes a word and if it's within range
        if node.is_end_of_word:
            if L <= prefix <= R:
                count += 1

        # To maintain lexicographical order during a stack-based DFS (LIFO),
        # we process siblings in reverse order so the smallest character 
        # ends up at the top of the stack.
        
        # 1. Collect all children of the current node
        children = []
        curr = node.first_child
        while curr:
            children.append(curr)
            curr = curr.next_sibling
        
        # 2. Push children onto the stack in reverse order
        for i in range(len(children) - 1, -1, -1):
            child = children[i]
            next_prefix = prefix + child.char
            
            # Pruning: Only push onto the stack if the prefix could 
            # potentially lead to a word <= R.
            if next_prefix <= R or next_prefix[:len(R)] <= R:
                stack.push((child, next_prefix))
                
    return count

n, q = map(int, input().split())
trie = Trie()

# Insert words
for _ in range(n):
    word = input().strip()
    trie.insert(word)

# Process queries
for _ in range(q):
    L, R = input().strip().split()
    print(count_in_range(trie, L, R))