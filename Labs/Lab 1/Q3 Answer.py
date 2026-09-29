class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        new_node = Node(data)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            print("Index out of range")
            return False

        new_node.next = current.next
        current.next = new_node
        return True

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def deleteList(self):
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current = temp
        self.head = None

def split(ll):
    if not ll.head:
        return LinkedList(), LinkedList()

    # Create Two New Lists
    # even_list → stores nodes from even positions.
    # odd_list → stores nodes from odd positions.
    # Both start as empty linked lists.
    even_list = LinkedList()
    odd_list = LinkedList()

    # current → pointer to traverse the original list.
    # index → keeps track of the current node’s position (0-based).
    # even_count → how many elements have been inserted into even_list.
    # odd_count → how many elements have been inserted into odd_list.
    # These counts are needed because .insert(data, position) requires the position in the target list, not the original.
    current = ll.head
    index = 0
    even_count = 0
    odd_count = 0

    while current:
        # If index % 2 == 0 → position is even:
        # Insert the current node’s data into even_list at position even_count.
        # Increase even_count because even_list got a new node.
        # Otherwise (odd position):
        # Insert into odd_list at position odd_count.
        # Increase odd_count.
        if index % 2 == 0:  # Even index (0, 2, 4, ...)
            even_list.insert(current.data, even_count)
            even_count += 1
        else:  # Odd index (1, 3, 5, ...)
            odd_list.insert(current.data, odd_count)
            odd_count += 1
        # Moves the pointer to the next node in the original list.
        # Increments index so the next iteration knows whether it’s even or odd.
        current = current.next
        index += 1

    return even_list, odd_list # Returns two completely separate linked lists. Original list remains untouched.

if __name__ == "__main__":
    linked_list = LinkedList()
    index = 0

    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if linked_list.insert(item, index):
                print(f"Successfully inserted {item} at index {index}")
                index += 1
            else:
                print(f"Failed to insert {item}")
    except ValueError:
        pass

    print("\nBefore split() is called:")
    print("Current list:", end=" ")
    linked_list.printList()

    even_list, odd_list = split(linked_list)

    print("\nAfter split() was called:")
    print("Current list:", end=" ")
    linked_list.printList()

    print("Even list:", end=" ")
    even_list.printList()

    print("Odd list:", end=" ")
    odd_list.printList()

    linked_list.deleteList()
    even_list.deleteList()
    odd_list.deleteList()