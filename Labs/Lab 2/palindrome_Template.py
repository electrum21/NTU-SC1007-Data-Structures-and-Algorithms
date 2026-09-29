class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

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

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.item

    def is_empty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.insert_node(self.ll.size, item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def is_empty(self):
        return self.ll.size == 0

def palindrome(word):
    stack = Stack()
    queue = Queue()

    '''
    Converts the word to uppercase so the comparison is case-insensitive.
    Only considers alphanumeric characters (char.isalnum()), ignoring spaces and punctuation.
    Each valid character is pushed to the stack and enqueued in the queue:
    • Stack: Last character pushed → top of stack.
    • Queue: First character enqueued → front of queue.
    '''
    word = word.upper()
    for char in word:
        if char.isalnum():
            stack.push(char)
            queue.enqueue(char)

    ''' 
    If the stack and queue somehow got out of sync (different sizes), this loop would remove extra elements from the stack to match the queue.
    This is added as a “safety check” in case non-alphanumeric characters were filtered inconsistently.
    '''
    while stack.ll.size > queue.ll.size:
        stack.pop()
    
    '''
    Pop from stack → gets the last character of the word.
    Dequeue from queue → gets the first character of the word.
    Compare the two:
    • If different, the word is not a palindrome, and the function returns False.
    • Otherwise, continue until the stack is empty.
    '''
    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            print("The string is not a palindrome")
            return False
        
    '''
    If the loop completes without finding a mismatch, the word is a palindrome.
    '''
    print("The string is a palindrome")
    return True

    # MY ORIGINAL CODES
    # for letter in word.lower():
    #     if letter != " ":
    #         stack.push(letter)
    # for letter in word.lower():
    #     if letter != " ":
    #         if letter != stack.pop():
    #             print("The string is not a palindrome")
    #             return False
    # print("The string is a palindrome")
    # return True   

if __name__ == "__main__":
    print("Sample String : A man a plan a canal Panama")
    palindrome("A man a plan a canal Panama")
    print("Sample String : Superman in the sky")
    palindrome("Superman in the sky")