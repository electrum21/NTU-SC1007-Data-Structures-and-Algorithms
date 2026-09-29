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

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        return None

    def is_empty(self):
        return len(self.items) == 0

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.is_end_of_word = False
        self.first_child = None
        self.next_sibling = None

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

def count_words_with_length(trie, target_length):

    # result[1] stores the running count of words matching the target_length
    result = [target_length, 0]
    
    def dfs(node, current_length):
        # If we reached the end of a word, check if its length matches the target
        if node.is_end_of_word:
            if current_length == result[0]:
                result[1] += 1


        # Recurse into all children (first_child and subsequent next_siblings)
        child = node.first_child
        while child:
            dfs(child, current_length + 1)
            child = child.next_sibling
    
    # Start DFS traversal from the root at depth 0
    dfs(trie.root, 0)

    return result[1]
        

# # Main program
# n_l = input().split()
# n = int(n_l[0])
# L = int(n_l[1])

# trie = Trie()
# for _ in range(n):
#     word = input().strip()
#     trie.insert(word)

# print(count_words_with_length(trie,L))

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
def run_tests():
    passed = 0
    failed = 0
 
    def test(description, words, target_length, expected):
        nonlocal passed, failed
        trie = Trie()
        for w in words:
            trie.insert(w)
        result = count_words_with_length(trie, target_length)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}: got {result}, expected {expected}")
 
    # Basic match
    test("Single word matches target length",
         ["cat"], 3, 1)
 
    # No word matches target length
    test("No word matches target length",
         ["cat", "dog", "elephant"], 5, 0)
 
    # Multiple words of matching length
    test("Multiple words of same length",
         ["cat", "dog", "bat", "run"], 3, 4)
 
    # Mixed lengths, count only those matching L=4
    test("Mixed lengths, count L=4",
         ["cat", "bear", "lion", "ox", "deer"], 4, 3)
 
    # Empty trie
    test("Empty trie returns 0",
         [], 3, 0)
 
    # Words with length 1
    test("Single-character words",
         ["a", "b", "c", "ab"], 1, 3)
 
    # Target length longer than any word
    test("Target length longer than all words",
         ["hi", "bye"], 10, 0)
 
    # Duplicate words (trie deduplicates)
    test("Duplicate insertions are deduplicated",
         ["cat", "cat", "cat"], 3, 1)
 
    # Prefix words - both 'car' and 'card' inserted, count L=4
    test("Prefix overlap, count L=4",
         ["car", "card", "care", "cat"], 4, 2)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()
 