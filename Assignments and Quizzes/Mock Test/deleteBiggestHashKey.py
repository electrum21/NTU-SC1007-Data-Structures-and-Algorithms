class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, hSize=0):
        self.hSize = hSize #the number of hash slots
        self.nSize = 0 #the number of keys
        self.table = [None] * self.hSize

def hash_func(key, hSize):
    return key % hSize

def hash_search(ht, key):
    if ht.hSize == 0:
        return None
    index = hash_func(key, ht.hSize)
    curr = ht.table[index]
    while curr:
        if curr.key == key:
            return curr
        curr = curr.next
    return None

def hash_print(ht):
    for i in range(ht.hSize):
        print(f"{i}:", end=" ")
        curr = ht.table[i]
        while curr:
            print(f"{curr.key} ->", end=" ")
            curr = curr.next
        print()
        
def hash_insert(ht, key):
    index = hash_func(key, ht.hSize)
    curr = ht.table[index]

    # Check duplicate
    while curr:
        if curr.key == key:
            return 0
        curr = curr.next

    # Insert at head
    new_node = Node(key)
    new_node.next = ht.table[index]
    ht.table[index] = new_node
    ht.nSize += 1

    return 1


def hash_delete_biggest(ht):
    if ht.nSize == 0:
        return 0

    max_key = -1
    max_index = -1
    max_node = None

    # Step 1: find biggest key
    for i in range(ht.hSize):
        curr = ht.table[i]
        while curr:
            if curr.key > max_key:
                max_key = curr.key
                max_index = i
                max_node = curr
            curr = curr.next

    if max_node is None:
        return 0

    # Step 2: delete from linked list
    curr = ht.table[max_index]
    prev = None

    while curr:
        if curr.key == max_key:
            if prev is None:
                # deleting head
                ht.table[max_index] = curr.next
            else:
                prev.next = curr.next
            ht.nSize -= 1
            return 1

        prev = curr
        curr = curr.next

    return 0


# def main():
#     ht = None

#     import sys
#     input = sys.stdin.read
#     data = list(map(int, input().split()))
#     i = 0

#     print("============= Hash Table ============")
#     print("|1. Create a hash table                   |")
#     print("|2. Insert a key to the hash table        |")
#     print("|3. Search a key in the hash table        |")
#     print("|4. Delete biggest key in the hash table  |")
#     print("|5. Print the hash table                  |")
#     print("|6. Quit                                  |")
#     print("=====================================")

#     print("Enter Selection: ", end="")
#     while i < len(data):
#         opt = data[i]
#         i += 1

#         if opt == 1:
#             print("Enter the size of hash table:")
#             size = data[i]
#             i+=1
#             ht = HashTable(size)
#             print("HashTable is created.")

#         elif opt == 2:
#             if ht is None:
#                 print("HashTable not created yet.")
#                 continue
#             print("Enter a key to be inserted:")
#             key = data[i]
#             i+=1
#             if hash_insert(ht, key):
#                 print(f"{key} is inserted.")
#             else:
#                 print(f"{key} is a duplicate. No key is inserted.")
#         elif opt == 3:
#             if ht is None:
#                 print("HashTable not created yet.")
#                 continue
#             print("Enter a key for searching in the HashTable:")
#             key = data[i]
#             i+=1
#             if hash_search(ht, key):
#                 print(f"{key} is found.")
#             else:
#                 print(f"{key} is not found.")
#         elif opt == 4:
#             if ht is None:
#                 print("HashTable not created yet.")
#                 continue
#             if hash_delete_biggest(ht):
#                 print("Biggest key is deleted.")
#             else:
#                 print("Biggest key is not existing.")
#         elif opt == 5:
#             if ht is None:
#                 print("HashTable not created yet.")
#                 continue
#             hash_print(ht)
#         elif opt == 6:
#             print("Exiting.")
#             break
#         else:
#             print("Invalid option.")
#         print("Enter Selection: ", end="")

# if __name__ == "__main__":
#     main()

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
def run_tests():
    passed = 0
    failed = 0
 
    def check(description, condition):
        nonlocal passed, failed
        status = "PASS" if condition else "FAIL"
        if condition:
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}")
 
    # Test 1: Delete biggest from a populated table
    ht = HashTable(5)
    for k in [3, 7, 1, 9, 4]:
        hash_insert(ht, k)
    result = hash_delete_biggest(ht)
    check("Delete biggest returns 1 on success", result == 1)
    check("Key 9 no longer found after deletion", hash_search(ht, 9) is None)
    check("nSize decremented after deletion", ht.nSize == 4)
 
    # Test 2: Deleting biggest repeatedly narrows down correctly
    ht2 = HashTable(7)
    for k in [10, 20, 30]:
        hash_insert(ht2, k)
    hash_delete_biggest(ht2)  # removes 30
    check("After removing 30, 20 is still found", hash_search(ht2, 20) is not None)
    hash_delete_biggest(ht2)  # removes 20
    check("After removing 20, 10 is still found", hash_search(ht2, 10) is not None)
    hash_delete_biggest(ht2)  # removes 10
    check("After removing all, nSize is 0", ht2.nSize == 0)
 
    # Test 3: Delete from empty table returns 0
    ht3 = HashTable(5)
    check("Delete biggest on empty table returns 0", hash_delete_biggest(ht3) == 0)
 
    # Test 4: Duplicate insertion is rejected
    ht4 = HashTable(5)
    hash_insert(ht4, 5)
    result_dup = hash_insert(ht4, 5)
    check("Duplicate insert returns 0", result_dup == 0)
    check("nSize unchanged after duplicate insert", ht4.nSize == 1)
 
    # Test 5: Search for non-existent key
    ht5 = HashTable(5)
    hash_insert(ht5, 2)
    check("Search for absent key returns None", hash_search(ht5, 99) is None)
 
    # Test 6: Single element table — delete biggest removes only element
    ht6 = HashTable(3)
    hash_insert(ht6, 42)
    hash_delete_biggest(ht6)
    check("After deleting only element, search returns None", hash_search(ht6, 42) is None)
    check("nSize is 0 after deleting only element", ht6.nSize == 0)
 
    # Test 7: Biggest key is at head of a chained bucket
    ht7 = HashTable(3)
    # Keys 0, 3, 6 all map to slot 0 — test deletion from mid-chain
    for k in [0, 3, 6]:
        hash_insert(ht7, k)
    hash_delete_biggest(ht7)  # removes 6
    check("6 deleted from chained bucket", hash_search(ht7, 6) is None)
    check("3 still present after deleting 6", hash_search(ht7, 3) is not None)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()