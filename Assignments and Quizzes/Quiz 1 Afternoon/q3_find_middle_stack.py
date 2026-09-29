# ============================================================
#  Q3 — Find Middle Element of Stack
#
#  Given a stack and 1 temporary Stack, return the middle
#  element. The original stack must be UNCHANGED after the call.
#
#  Middle definition (0-indexed from top):
#    - n odd  -> exact middle = index n//2 from top
#    - n even -> index n//2 from top
#    Both cases use the same formula: pop (n//2 + 1) times.
#
#  You may only use: push(), pop(), peek(), isEmpty(), getSize()
#
#  Example (top -> bottom):
#    Stack: 5 4 3 2 1   (n=5, odd)
#    Middle = index 2 from top = 3
#    findMiddleElement(stack) -> 3
#
#    Stack: 4 3 2 1   (n=4, even)
#    Middle = index n//2 = 2 from top = 2
#    findMiddleElement(stack) -> 2
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def printStack(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print("Top -> [" + " ".join(items) + "] <- Bottom")


# ============================================================
#  YOUR SOLUTION HERE
# ============================================================

def findMiddleElement(stack):
    temp = Stack()
    n = stack.getSize()
    target = n // 2 + 1        # number of pops to reach middle

    result = None
    for _ in range(target):
        result = stack.pop()   # keep overwriting — last pop = middle
        temp.push(result)

    # Restore the original stack
    while not temp.isEmpty():
        stack.push(temp.pop())

    return result


# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def build_stack(values_bottom_to_top):
    """Push values so the last item ends up on top."""
    s = Stack()
    for v in values_bottom_to_top:
        s.push(v)
    return s

def stack_to_list(s):
    """Snapshot top->bottom without modifying."""
    items = []
    current = s.head
    while current:
        items.append(current.data)
        current = current.next
    return items

def run_test(label, values_bottom_to_top, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    s = build_stack(values_bottom_to_top)
    snapshot_before = stack_to_list(s)
    print(f"  Stack (top->bottom) : ", end=""); s.printStack()
    result = findMiddleElement(s)
    snapshot_after = stack_to_list(s)
    restored = snapshot_before == snapshot_after
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    restore_status = "RESTORED ✓" if restored else "NOT RESTORED ✗"
    print(f"  Expected            : {expected}")
    print(f"  Your answer         : {result}   {status}")
    print(f"  Stack after call    : ", end=""); s.printStack()
    print(f"  Stack restore check : {restore_status}")

# Test 1 — odd n=5, exact middle
# top->bottom: [5 4 3 2 1], middle = index 2 from top = 3
run_test(
    "Test 1: [5 4 3 2 1] top->bottom   (n=5 odd, middle=3)",
    values_bottom_to_top=[1, 2, 3, 4, 5],
    expected=3
)

# Test 2 — even n=4, index n//2=2 from top
# top->bottom: [4 3 2 1], middle = index 2 from top = 2
run_test(
    "Test 2: [4 3 2 1] top->bottom   (n=4 even, middle=2)",
    values_bottom_to_top=[1, 2, 3, 4],
    expected=2
)

# Test 3 — odd n=7, exact middle
# top->bottom: [7 6 5 4 3 2 1], middle = index 3 from top = 4
run_test(
    "Test 3: [7 6 5 4 3 2 1] top->bottom   (n=7 odd, middle=4)",
    values_bottom_to_top=[1, 2, 3, 4, 5, 6, 7],
    expected=4
)

# Test 4 — even n=6, index n//2=3 from top
# top->bottom: [6 5 4 3 2 1], middle = index 3 from top = 3
run_test(
    "Test 4: [6 5 4 3 2 1] top->bottom   (n=6 even, middle=3)",
    values_bottom_to_top=[1, 2, 3, 4, 5, 6],
    expected=3
)

# Test 5 — single element
run_test(
    "Test 5: [42] top->bottom   (n=1, middle=42)",
    values_bottom_to_top=[42],
    expected=42
)

# Test 6 — restoration check with distinct values
# top->bottom: [10 20 30 40 50], middle = index 2 from top = 30
run_test(
    "Test 6: [10 20 30 40 50] top->bottom   (n=5 odd, middle=30) — restoration check",
    values_bottom_to_top=[50, 40, 30, 20, 10],
    expected=30
)
