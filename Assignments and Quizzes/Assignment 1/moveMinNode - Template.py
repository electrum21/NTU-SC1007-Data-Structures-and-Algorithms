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
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True
    
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

def moveMinNode(head):
    if head is None or head.next is None: # to check for list with size 0 or size 1
        return
    
    # First pass: Find min value
    min_data = head.data
    cur = head
    while cur:
        if cur.data < min_data:
            min_data = cur.data
        cur = cur.next

    min_head = None
    min_tail = None
    others_head = None
    others_tail = None

    cur = head
    while cur:
        if cur.data == min_data:
            if min_head == None:
                min_head = cur
                min_tail = cur
            else:
                min_tail.next = cur
                min_tail = cur
        else:
            if others_head == None:
                others_head = cur
                others_tail = cur
            else:
                others_tail.next = cur
                others_tail = cur
        cur = cur.next
    
    if min_head == None:
        return others_head
    else:
        min_tail.next = others_head
        if others_tail:
            others_tail.next = None
        return min_head
    

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
    
    linked_list.head = moveMinNode(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()