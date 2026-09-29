# ============================================================
#  Q3 — Reverse Second Half of an Even Queue
#
#  Given a queue with an EVEN number of elements and
#  1 temporary Stack, reverse only the second half.
#
#  You may only use: enqueue(), dequeue(), push(), pop(),
#                    isEmpty(), getSize()
#
#  Example:
#    Queue (front → back): 1 2 3 4 5 6
#    After call           : 1 2 3 6 5 4
#                                 ^^^^^^ reversed
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # back
        self._size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return data

    def isEmpty(self):
        return self._size == 0

    def getSize(self):
        return self._size

    def printQueue(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print("Front -> [" + " ".join(items) + "] <- Back")


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def peek(self):
        return self.head.data if self.head else None

    def isEmpty(self):
        return self._size == 0

    def getSize(self):
        return self._size


# ============================================================
#  YOUR SOLUTION HERE
# ============================================================

def reverseSecondHalf(queue):
    half_length = queue.getSize() // 2
    for i in range(half_length):
        queue.enqueue(queue.dequeue())
    s = Stack()
    for i in range(half_length):
        s.push(queue.dequeue())
    for i in range(half_length):
        queue.enqueue(s.pop())

    return queue


# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def build_queue(values):
    q = Queue()
    for v in values:
        q.enqueue(v)
    return q

def queue_to_list(q):
    items = []
    current = q.head
    while current:
        items.append(current.data)
        current = current.next
    return items

def run_test(label, values, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    q = build_queue(values)
    print(f"  Before   : ", end=""); q.printQueue()
    reverseSecondHalf(q)
    result = queue_to_list(q)
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    print(f"  After    : ", end=""); q.printQueue()
    print(f"  Expected : Front -> [{' '.join(map(str, expected))}] <- Back")
    print(f"  Result   : {status}")

# Test 1 — given example
run_test(
    "Test 1: [1 2 3 4 5 6] — reverse second half",
    [1, 2, 3, 4, 5, 6],
    expected=[1, 2, 3, 6, 5, 4]
)

# Test 2 — 2 elements
run_test(
    "Test 2: [1 2] — minimal even queue",
    [1, 2],
    expected=[1, 2]    # second half is just [2], reversing single = same
)

# Test 3 — 4 elements
run_test(
    "Test 3: [1 2 3 4] — 4 elements",
    [1, 2, 3, 4],
    expected=[1, 2, 4, 3]
)

# Test 4 — 8 elements
run_test(
    "Test 4: [1 2 3 4 5 6 7 8] — 8 elements",
    [1, 2, 3, 4, 5, 6, 7, 8],
    expected=[1, 2, 3, 4, 8, 7, 6, 5]
)

# Test 5 — applying twice should restore the original
# First half=[1,2,3], second half=[6,5,4] -> reversed second=[4,5,6] -> [1,2,3,4,5,6]
run_test(
    "Test 5: [1 2 3 6 5 4] — reverse already-reversed second half",
    [1, 2, 3, 6, 5, 4],
    expected=[1, 2, 3, 4, 5, 6]
)
