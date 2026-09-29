# ============================================================
#  Q1 — Reverse Between Index m and n of a Queue (inclusive)
#
#  You are given 1 temporary Stack.
#  You may only use: enqueue(), dequeue(), push(), pop(),
#                    isEmpty(), getSize()
#
#  reverseQueueBetween(queue, m, n):
#    - Reverse elements at indexes m..n (inclusive, 0-indexed)
#    - Everything outside that range stays in original order
#
#  Example:
#    Queue (front->back): 1 2 3 4 5   m=1, n=3
#    After call          : 1 4 3 2 5
#                            ^^^^^  reversed
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
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

def reverseQueueBetween(queue, m, n):
    s = Stack()

    # Phase 1: rotate first m elements to the back
    for i in range(m):
        queue.enqueue(queue.dequeue())

    # Phase 2: push segment [m..n] onto stack → LIFO reverses it
    for i in range(n - m + 1):
        s.push(queue.dequeue())

    # Phase 3: pop stack back to queue → reversed segment appended at back
    while not s.isEmpty():
        queue.enqueue(s.pop())

    # Phase 4: rotate the post-segment elements (now at front) to the back
    for i in range(queue.getSize() - n - 1):
        queue.enqueue(queue.dequeue())

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

def run_test(label, values, m, n, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    q = build_queue(values)
    print(f"  Before   : ", end=""); q.printQueue()
    print(f"  Call     : reverseQueueBetween(queue, {m}, {n})")
    reverseQueueBetween(q, m, n)
    result = queue_to_list(q)
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    print(f"  After    : ", end=""); q.printQueue()
    print(f"  Expected : Front -> [{' '.join(map(str, expected))}] <- Back")
    print(f"  Result   : {status}")

# Test 1 — given example, middle segment
run_test(
    "Test 1: [1 2 3 4 5]  m=1, n=3  — middle segment",
    [1, 2, 3, 4, 5], 1, 3,
    expected=[1, 4, 3, 2, 5]
)

# Test 2 — reverse from index 0 (includes front)
run_test(
    "Test 2: [1 2 3 4 5]  m=0, n=2  — from front",
    [1, 2, 3, 4, 5], 0, 2,
    expected=[3, 2, 1, 4, 5]
)

# Test 3 — reverse to last index (includes back)
run_test(
    "Test 3: [1 2 3 4 5]  m=2, n=4  — to back",
    [1, 2, 3, 4, 5], 2, 4,
    expected=[1, 2, 5, 4, 3]
)

# Test 4 — single element (no change)
run_test(
    "Test 4: [1 2 3 4 5]  m=2, n=2  — single element",
    [1, 2, 3, 4, 5], 2, 2,
    expected=[1, 2, 3, 4, 5]
)

# Test 5 — entire queue reversed
run_test(
    "Test 5: [1 2 3 4 5]  m=0, n=4  — entire queue",
    [1, 2, 3, 4, 5], 0, 4,
    expected=[5, 4, 3, 2, 1]
)
