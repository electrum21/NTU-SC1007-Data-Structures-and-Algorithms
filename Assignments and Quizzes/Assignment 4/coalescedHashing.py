TABLESIZE = 37
PRIME = 13
EMPTY = 0
USED = 1

class HashSlot:
    def __init__(self):
        self.key = 0
        self.indicator = EMPTY
        self.next = -1

def hash_func(key):
    return key % TABLESIZE

def hash_insert(key, hash_table):

    home_index = key % TABLESIZE
    
    # Below block is to check for duplicate keys
    temp = home_index
    while temp != -1:
        if hash_table[temp].indicator == USED and hash_table[temp].key == key:
            return -1 # Duplicate key 
        temp = hash_table[temp].next

    # Below block is like a successful first hit. If the calculated home_index is empty, means no collision,
    # can just immediately place key without needing to traverse or probe
    if hash_table[home_index].indicator == EMPTY:
        hash_table[home_index].key = key
        hash_table[home_index].indicator = USED
        return home_index

    # Otherwise if not empty, then we need to track the previous hash table entry so that we can update next
    # to point to the new entry being inserted
    last_in_chain = home_index
    while hash_table[last_in_chain].next != -1:
        last_in_chain = hash_table[last_in_chain].next

    # Do the coalesce check and linear probing, to check for the next available slot and insert an entry there
    for i in range(1, TABLESIZE):
        new_slot = (home_index + i) % TABLESIZE
        if hash_table[new_slot].indicator == EMPTY:
            hash_table[new_slot].key = key
            hash_table[new_slot].indicator = USED
            hash_table[last_in_chain].next = new_slot 
            return new_slot

    # Assignment requirement, return value larger than table size if table is full.
    # By the time the code reaches here, the table has to be full
    return TABLESIZE + 1

def hash_find(key, hash_table):
    curr_index = hash_func(key)
    while curr_index != -1:
        if hash_table[curr_index].indicator == USED and hash_table[curr_index].key == key:
            return curr_index
        curr_index = hash_table[curr_index].next

    return -1

def print_menu():
    print("============= Hash Table ============")
    print("|1. Insert a key to the hash table  |")
    print("|2. Search a key in the hash table  |")
    print("|3. Print the hash table            |")
    print("|4. Quit                            |")
    print("=====================================")
    print("Enter selection: ", end="")


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    hash_table = [HashSlot() for _ in range(TABLESIZE)]
    for slot in hash_table:
        slot.key = 0
        slot.indicator = EMPTY
        slot.next = -1

    i = 0
    print_menu()
    while i < len(data):

        opt = data[i]
        i += 1

        if opt == 1:  # Insert
            print("Enter a key to be inserted:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_insert(key, hash_table)
            if index < 0:
                print("Duplicate key")
            elif index < TABLESIZE:
                print(f"Insert {key} at index {index}")
            else:
                print("Table is full.")
            print("Enter selection: ", end="")
        elif opt == 2:  # Search
            print("Enter a key for searching in the HashTable:")
            if i >= len(data):
                break
            key = data[i]
            i += 1
            index = hash_find(key, hash_table)
            if index != -1:
                print(f"{key} is found at index {index}.")
            else:
                print(f"{key} is not found.")
            print("Enter selection: ", end="")
        elif opt == 3:  # Print table
            print("index:\t key \t next")
            for j in range(TABLESIZE):
                print(f"{j}\t{hash_table[j].key}\t{hash_table[j].next}")
            print("Enter selection: ", end="")
        elif opt == 4:
            break
        else:
            print("Enter selection: ", end="")
            continue


if __name__ == "__main__":
    main()