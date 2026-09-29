class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
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
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

def moveOdditemstoback(head):
    # If the list is empty (head is None) or has only one node, there’s nothing to rearrange, so we return it as-is.
    if not head or not head.next:
        return head
    
    # We create two lists internally: even_head & even_tail → start and end of the even-number list. odd_head & odd_tail → start and end of the odd-number list.
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    current = head

    # This means keep going until current becomes None (i.e., end of the linked list). At the start, current = head.
    while current:
        # We temporarily store the next node so we can continue the loop later.
        # This is important because in the next step we’re going to cut the link from current.
        next_node = current.next 
        current.next = None  
        
        # We check if the data in the node is divisible by 2. If yes → node is even → goes into the even list.
        # If even_head is None → this is the first even node → set both head and tail to current.
        # Otherwise: Attach this node after the tail: even_tail.next = current. Move the tail pointer to the new node: even_tail = current.
        # If not even, it must be odd. Same logic as the even list: If odd_head is None → first odd node → set head and tail to current.
        # Otherwise, attach to the odd tail and move the tail pointer.
        if current.data % 2 == 0:  
            if not even_head:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        else:  
            if not odd_head:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current

        # We jump to the next node we saved earlier. Loop continues until current becomes None.        
        current = next_node

    # Merge even and odd lists If one group is empty, just return the other. Otherwise, connect the even list's tail to the odd list's head.
    if not even_head:
        return odd_head
    if not odd_head:
        return even_head
    even_tail.next = odd_head
    odd_tail.next = None

    return even_head

if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break

    print("\nBefore:", end=" ")
    linked_list.printList()
    linked_list.head = moveOdditemstoback(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()