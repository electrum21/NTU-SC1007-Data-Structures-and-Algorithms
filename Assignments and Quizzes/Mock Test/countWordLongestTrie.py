class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.is_end_of_word = False
        self.first_child = None
        self.next_sibling = None

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

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _insert_child(self, node, char):
        prev = None
        curr = node.first_child
        while curr and curr.char < char:
            prev = curr
            curr = curr.next_sibling

        if curr and curr.char == char:
            return curr

        new_node = TrieNode(char)
        new_node.next_sibling = curr
        if prev:
            prev.next_sibling = new_node
        else:
            node.first_child = new_node
        return new_node

    def insert(self, word):
        current = self.root
        for char in word:
            current = self._insert_child(current, char)
        current.is_end_of_word = True
    
    def _find_child(self, node, char):
        curr = node.first_child
        while curr:
            if curr.char == char:
                return curr
            curr = curr.next_sibling
        return None

    def search(self, word):
        curr = self.root
        for char in word:
            curr = self._find_child(curr, char)
            if not curr:
                return False
        return curr.is_end_of_word
    
def count_words_longest(trie):

    # This list will store the max length found and its count
    # Using a list [max_len, count] to allow modification inside helper
    result = [0, 0]

    def dfs(node, current_depth):
        if node.is_end_of_word:
            if current_depth > result[0]:
                result[0] = current_depth
                result[1] = 1
            elif current_depth == result[0]:
                result[1] += 1

        child = node.first_child
        while child:
            dfs(child, current_depth + 1)
            child = child.next_sibling

    dfs(trie.root, 0)

    return result[1]
        



# # Main program
# n = int(input())
# trie = Trie()

# # Insert words
# for _ in range(n):
#     word = input().strip()
#     trie.insert(word)
# print(count_words_longest(trie))

 
# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
def run_tests():
    passed = 0
    failed = 0
 
    def test(description, words, expected):
        nonlocal passed, failed
        trie = Trie()
        for w in words:
            trie.insert(w)
        result = count_words_longest(trie)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}: got {result}, expected {expected}")
 
    # Only one longest word
    test("Single longest word",
         ["cat", "elephant", "dog"], 1)
 
    # All words same length → all are longest
    test("All words same length",
         ["cat", "dog", "bat"], 3)
 
    # Two words tied for longest
    test("Two words tied for longest",
         ["hello", "world", "hi"], 2)
 
    # Single word in trie
    test("Single word",
         ["python"], 1)
 
    # Empty trie returns 0
    test("Empty trie returns 0",
         [], 0)
 
    # Prefix words: 'car' and 'card' — longest is 'card'
    test("Prefix overlap, only longer counts",
         ["car", "card"], 1)
 
    # Duplicates are deduplicated by trie
    test("Duplicate words deduplicated",
         ["moon", "moon", "sun"], 1)
 
    # Multiple words all share max length
    test("Three-way tie for longest",
         ["abc", "xyz", "def", "ab", "a"], 3)
 
    # One-character words
    test("All single-character words",
         ["a", "b", "c"], 3)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()