class HashTableNode:
    def __init__(self, key=None):
        self.key = key
        self.deleted = False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None
        self.count = 0

    def _hash(self, key, i):
        return (key + i) % self.size  # Linear probing function

    def hash_insert(self, key):
        if self.count >= self.size:
            print("Hash table is full. Cannot insert new key.")
            return False
        
        i = 0
        index = self._hash(key, i) # start from the original hash position
        while self.table[index] is not None and not self.table[index].deleted:
            if self.table[index].key == key:
                return False # duplicate key found
            i += 1
            index = self._hash(key, i) # linear probing
            if i >= self.size:
                return False # entire table has been checked
            
        i += 1
        temp = (index + 1) % self.size
        while self.table[temp] is not None:
            if self.table[temp].key == key and not self.table[temp].deleted:
                return False # duplicate exists later in probe sequence
            i += 1
            temp = self._hash(key, i)
            if i >= self.size:
                break

        self.table[index] = HashTableNode(key)
        self.count += 1
        return True

    def hash_delete(self, key):
        i = 0
        index = self._hash(key, i) # Start probing the hash position
        while self.table[index] is not None:
            if self.table[index].key == key and not self.table[index].deleted:
                self.table[index].deleted = True # mark slot as deleted
                self.count -= 1
                return True
            i += 1
            index = self._hash(key, i) # continue linear probing
            if i >= self.size:
                return False # key not found
        return False

    def hash_search(self, key):
        i = 0
        index = self._hash(key, i) # Start probing from hash position
        while self.table[index] is not None:
            if self.table[index].key == key and not self.table[index].deleted:
                return True # key found
            i += 1
            index = self._hash(key, i) # continue probing
            if i >= self.size:
                return False # key not found after full scan
        return False

    def hash_print(self):
        print("Hash Table:")
        for i, node in enumerate(self.table):
            if node is None:
                print(f"Slot {i}: Empty")
            else:
                status = "Deleted" if node.deleted else "Occupied"
                print(f"Slot {i}: {node.key} ({status})")


# Menu-driven program
if __name__ == "__main__":
    print("============= Hash Table ============")
    print("|1. Create a hash table             |")
    print("|2. Insert a key to the hash table  |")
    print("|3. Search a key in the hash table  |")
    print("|4. Delete a key from the hash table|")
    print("|5. Print the hash table            |")
    print("|6. Quit                            |")
    print("=====================================")

    ht = None

    while True:
        opt = int(input("Enter selection: "))
        if opt == 1:
            size = int(input("Enter number of hash slots: "))
            ht = HashTable(size)
            print(f"HashTable with {size} slots is created.")
        elif opt == 2:
            key = int(input("Enter a key to be inserted: "))
            if ht and ht.hash_insert(key):
                print(f"{key} is inserted.")
            else:
                print(f"{key} is a duplicate or table is full. No key is inserted.")
        elif opt == 3:
            key = int(input("Enter a key for searching in the HashTable: "))
            if ht and ht.hash_search(key):
                print(f"{key} is found.")
            else:
                print(f"{key} is not found.")
        elif opt == 4:
            key = int(input("Enter a key to delete: "))
            if ht and ht.hash_delete(key):
                print(f"{key} is deleted.")
            else:
                print(f"{key} is not found.")
        elif opt == 5:
            if ht:
                ht.hash_print()
            else:
                print("No hash table created yet.")
        elif opt == 6:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")
