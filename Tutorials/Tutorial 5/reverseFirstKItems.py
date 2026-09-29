class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.find_node(index - 1)
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        return 0

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.find_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
        return 0
    
    def print_list(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("None")

class Queue:
   def __init__(self):
       self.ll = LinkedList()

   def enqueue(self, data):    
       self.ll.insert_node(self.ll.size, data)

   def dequeue(self):
       if self.isEmpty():
           return None
       data = self.ll.head.item    
       self.ll.remove_node(0)
       return data

   def getFront(self):
       if self.isEmpty():
           raise IndexError("Peek from empty queue")
       return self.ll.head.item

   def getSize(self):           
       return self.ll.size

   def isEmpty(self):
       return self.ll.size == 0
  
   def printQueue(self):
       if self.isEmpty():
           print("Queue is empty")
           return
       current = self.ll.head
       while current:
           print(current.item, end=" ")    
           current = current.next
       print()

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.isEmpty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.item

    def isEmpty(self):
        return self.ll.size == 0
    
    def get_size(self):
        return self.ll.size
    
    def print_stack(self):
        self.ll.print_list()

def reverse_queue(queue, number):
    stack = Stack()
    queue_size = queue.getSize()
    iteration = 0
    for i in range(number):
        stack.push(queue.dequeue())
        iteration += 1
    while not stack.isEmpty():
        queue.enqueue(stack.pop())
    for i in range(queue_size - iteration):
        queue.enqueue(queue.dequeue())
    return queue

queue = Queue()
while True:
        print("1: Insert an integer into the queue:")
        print("2: Reverse the elements of the queue until the given number:")
        print("0: Quit:")

        choice = int(input("Please input your choice (1/2/0): "))
        
        if choice == 1:
            value = int(input("Input an integer that you want to insert into the stack: "))
            queue.enqueue(value)
            print("The resulting queue is:")
            queue.printQueue() 
        elif choice == 2:
            number = int(input("Enter an integer to reverse the queue until that number: "))
            queue = reverse_queue(queue, number)
            print("The resulting queue after after reversing first", number, "elements is:")
            queue.printQueue()   
        elif choice == 0:
            break
        else:
            print("Choice unknown.")