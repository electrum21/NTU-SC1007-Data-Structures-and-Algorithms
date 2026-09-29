class HashTableNode:
    def __init__(self, key=None):
        self.key = key
        self.deleted = False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key, i):
        return (key + i) % self.size

    def hash_delete(self, key):
        i = 0
        index = self._hash(key, i)

        while self.table[index] is not None:
            if self.table[index].key == key and not self.table[index].deleted:
                self.table[index].deleted = True
                return True
            i += 1
            if i >= self.size:
                return False
            index = self._hash(key, i)

        return False

    def hash_search(self, key):
        i = 0
        index = self._hash(key, i)

        while self.table[index] is not None:
            if self.table[index].key == key and not self.table[index].deleted:
                return True
            i += 1
            if i >= self.size:
                return False
            index = self._hash(key, i)

        return False
        
    def hash_insert(self, key):
        i = 0
        while i < self.size:
            index = self._hash(key, i)

            # Case 1: Slot is empty, insert new node
            if self.table[index] is None:
                self.table[index] = HashTableNode(key)
                return True
            
            # Case 2: Key already exists (and is not deleted), it's a duplicate
            if self.table[index].key == key and not self.table[index].deleted:
                return False

            # Case 3: Slot contains a tombstone, overwrite it to reuse space
            if self.table[index].deleted:
                self.table[index].key = key
                self.table[index].deleted = False
                return True
            
            i += 1 # Move to next probe index
        return False

def count_unique(nums):
    # Initializing table size to 2x elements reduces collision probability
    ht = HashTable(max(2 * len(nums), 1))
    unique_nums = 0
    
    # Track unique count by attempting insertion for every number
    for num in nums:
        if ht.hash_insert(num):
            unique_nums += 1
    return unique_nums


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
def run_tests():
    passed = 0
    failed = 0
 
    def test(description, nums, expected):
        nonlocal passed, failed
        result = count_unique(nums)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}: got {result}, expected {expected}")
 
    # All unique
    test("All unique elements",
         [1, 2, 3, 4, 5], 5)
 
    # All duplicates
    test("All duplicates",
         [7, 7, 7, 7], 1)
 
    # Mixed duplicates
    test("Mixed duplicates",
         [1, 2, 2, 3, 3, 3], 3)
 
    # Single element
    test("Single element",
         [42], 1)
 
    # Two identical elements
    test("Two identical elements",
         [5, 5], 1)
 
    # Two different elements
    test("Two different elements",
         [5, 6], 2)
 
    # Larger array with some repeats
    test("Larger array with repeats",
         [10, 20, 10, 30, 20, 40, 50, 40], 5)
 
    # Negative numbers
    test("Negative numbers (all unique)",
         [-1, -2, -3], 3)
 
    # Negatives with duplicates
    test("Negative numbers with duplicates",
         [-1, -1, -2, -2, -3], 3)
 
    # Zero included
    test("Array with zeros",
         [0, 0, 1, 2, 0], 3)
 
    # All zeros
    test("All zeros",
         [0, 0, 0], 1)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()
 