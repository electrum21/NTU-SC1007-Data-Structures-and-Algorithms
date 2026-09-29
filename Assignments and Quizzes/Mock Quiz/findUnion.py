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

def findUnion(head1, head2):
    new_ll = LinkedList()
    prev_in_new_ll = None
    new_ll_index = 0

    while head1 and head2:
        if head1.data == head2.data:
            if prev_in_new_ll and head1.data == prev_in_new_ll.data:
                head1 = head1.next
                head2 = head2.next
                continue
            new_ll.insertNode(head1.data, new_ll_index)
            prev_in_new_ll = new_ll.findNode(new_ll_index)
            new_ll_index += 1
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            if prev_in_new_ll and head1.data == prev_in_new_ll.data:
                head1 = head1.next
                continue
            new_ll.insertNode(head1.data, new_ll_index)
            prev_in_new_ll = new_ll.findNode(new_ll_index)
            new_ll_index += 1
            head1 = head1.next
        elif head1.data > head2.data:
            if prev_in_new_ll and head2.data == prev_in_new_ll.data:
                head2 = head2.next
                continue
            new_ll.insertNode(head2.data, new_ll_index)
            prev_in_new_ll = new_ll.findNode(new_ll_index)
            new_ll_index += 1
            head2 = head2.next
    
    while head1:
        if prev_in_new_ll and head1.data == prev_in_new_ll.data:
            head1 = head1.next
            continue
        new_ll.insertNode(head1.data, new_ll_index)
        prev_in_new_ll = new_ll.findNode(new_ll_index)
        new_ll_index += 1
        head1 = head1.next
    
    while head2:
        if prev_in_new_ll and head2.data == prev_in_new_ll.data:
            head2 = head2.next
            continue
        new_ll.insertNode(head2.data, new_ll_index)
        prev_in_new_ll = new_ll.findNode(new_ll_index)
        new_ll_index += 1
        head2 = head2.next

    return new_ll.findNode(0)


if __name__ == "__main__":
    # Helper function to create a linked list from a string of space-separated numbers
    def create_linked_list_from_input(input_string):
        linked_list = LinkedList()
        numbers = []
        for item in input_string.split():
            try:
                numbers.append(int(item))
            except ValueError:
                continue
       
        for i, num in enumerate(numbers):
            linked_list.insertNode(num, i)
       
        return linked_list
   
    # Read input from file (or stdin if redirect is used)
    try:
        # Read first line for first linked list
        input_str1 = input()
        list1 = create_linked_list_from_input(input_str1)
       
        # Read second line for second linked list
        input_str2 = input()
        list2 = create_linked_list_from_input(input_str2)
       
        # Find the union
        result = findUnion(list1.head, list2.head)
       
        # Print the union list
        if result is None:
            print("No elements")
        else:
            temp = result
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
   
    except EOFError:
        print("Error: Input file should contain at least two lines with the linked lists data.")