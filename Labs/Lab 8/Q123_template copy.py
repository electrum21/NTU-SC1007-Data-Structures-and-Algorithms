class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        current = node.first_child
        while current:
            if current.char == char:
                return current
            current = current.next_sibling
        return None

    def _add_child(self, node, char):
        #add your implementations to insert a child following the alphabetical order
        new_node = TrieNode(char)
        if node.first_child is None or node.first_child.char > char:
            new_node.next_sibling = node.first_child
            node.first_child = new_node
            return new_node
        
        prev = node.first_child
        curr = node.first_child.next_sibling

        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        prev.next_sibling = new_node
        new_node.next_sibling = curr
        return new_node

    def insert(self, word):
        node = self.root
        for char in word:
            child = self._find_child(node, char)
            if not child:
                child = self._add_child(node, char)
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def print_words_alphabetically(self):
        self.dfs(self.root, "")

    def dfs(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)
            return True
        child = node.first_child
        while child:
            self.dfs(child, prefix + child.char)
            child = child.next_sibling
        
    def print_words_reverse_alphabetically(self):
        words = []
        self.dfs_reverse(self.root, "", words)
        for word in words:
            print(word)

    def dfs_reverse(self, node, prefix, words):
        stack = Stack()
        child = node.first_child

        while child:
            stack.push(child)
            child = child.next_sibling

        while not stack.is_empty():
            child = stack.pop()
            self.dfs_reverse(child, prefix + child.char, words)
            
        if node.is_end_of_word:
            words.append(prefix)

# Assume Trie, TrieNode, and Queue classes have already been defined.
# Create a new Trie instance
trie = Trie()
trie.insert("car")
trie.insert("care")
trie.insert("cat")
trie.insert("camp")
trie.insert("camera")

trie.print_words_reverse_alphabetically()
trie.print_words_alphabetically()
