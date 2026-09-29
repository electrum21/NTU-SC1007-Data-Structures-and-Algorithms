class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def findNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
  
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = ListNode(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
            
        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" -> ")
            cur = cur.next
        print("None")

    def removeAllItems(self):
        self.head = None
        self.size = 0

def moveEvenItemsToBack(ll):
    if ll.head is None or ll.size < 2:
        return
    
    last = ll.head
    size = ll.size

    for _ in range(size):
        if last.next:
            last = last.next # Move last to point to the last node

    cur = ll.head
    prev_node = None
    count = 0

    while count < size:
        if cur.item % 2 == 0:
            next_node = cur.next # Store the next node before changing links

            if cur == ll.head: # Accounts for even number at the head
                ll.head = cur.next # Modify head to point to the next element
            else:
                prev_node.next = cur.next # Assuming cur is not ll.head, there would have been a previous node already

            last.next = cur # Append the even number to the end of the list
            cur.next = None # Set the next of the moved node to None since it's now the last node
            last = cur # After assigning the even number to the last element, last now points to the even number

            cur = next_node # Move cur to the next node in the original list
        else:
            prev_node = cur # Update prev_node only if current node is not moved
            cur = cur.next # Move to the next node in the original list
        
        count += 1 # Increment count to ensure we only process the original size of the list


if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list:")
        print("2: Move all even integers to the back of the linked list:")
        print("0: Quit:")

        choice = int(input("Please input your choice (1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            ll.insertNode(value, ll.size)
            print("The resulting linked list is:")
            ll.printList()
        elif choice == 2:
            moveEvenItemsToBack(ll)
            print("The resulting linked list after moving even integers to the back is:")
            ll.printList()
        elif choice == 0:
            ll.removeAllItems()
            break
        else:
            print("Choice unknown;")