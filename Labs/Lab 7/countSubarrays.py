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
    def subarray_sum(self, nums, k):
        ht = HashTable(len(nums))
        ht.hash_insert(0, 1)
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            if ht.hash_search(prefix_sum - k):
                count += ht.hash_get(prefix_sum - k)
            ht.hash_insert(prefix_sum, 1)

        return count
        
def test_subarray_num():
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 7, 0),
        ([], 0, 0),
        ([5], 5, 1),
        ([1, -1, 1], 1, 3),
        ([0, 0, 0], 0, 6)
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases):
        result = Solution().subarray_sum(nums, k)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i+1}: {status} | Expected: {expected}, Got: {result}")

test_subarray_num()