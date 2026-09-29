class Node:
    def __init__(self, key, value=1):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, num_data):
        self.load_factor = 3
        self.size = max(10, num_data // self.load_factor)
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def hash_insert(self, key, value=1):
        index = self._hash(key)
        current = self.table[index]

        # If key already exists, update value
        while current:
            if current.key == key:
                current.value += value
                return
            current = current.next

        # Insert new node
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def hash_search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next

        return False

    def hash_get(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return 0

    def hash_print(self):
        print("Hash Table:")
        for i, node in enumerate(self.table):
            print(f"Slot {i}: ", end="")
            current = node
            while current:
                print(f"({current.key}:{current.value}) -> ", end="")
                current = current.next
            print("None")

class Solution:
    def longest_consecutive(self, nums):
        
        if not nums:
            return 0 # Empty array has no sequence

        ht = HashTable(len(nums)) # Create hash table for fast lookup

        # Insert all numbers into the hash table
        for num in nums:
            if not ht.hash_search(num):
                ht.hash_insert(num)

        longest = 0 # Store the longest sequence length found

        for num in nums:
            # Only start counting from the beginning of a sequence
            if not ht.hash_search(num - 1):
                current = num
                length = 1

                # Extend the sequence while the next number exists
                while ht.hash_search(current + 1):
                    current += 1
                    length += 1
                
                longest = max(longest, length)

        return longest