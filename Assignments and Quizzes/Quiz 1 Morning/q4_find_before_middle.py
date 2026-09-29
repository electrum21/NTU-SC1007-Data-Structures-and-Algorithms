# ============================================================
#  Q4 — Find Element Just Before Middle of Stack
#
#  Given a stack and 1 temporary Stack, return the element
#  that sits just BELOW the middle element (one position
#  deeper than middle, i.e. closer to the bottom).
#
#  You may only use: push(), pop(), peek(), isEmpty(), getSize()
#  The original stack must be fully RESTORED after the call.
#
#  Middle definition: position (n//2 + 1) from the top (1-indexed)
#  Before-middle    : position (n//2) from the top — the element popped
#                     just BEFORE you reach the middle when counting from top
#
#  Example (top to bottom):
#    Stack: 5 4 3 2 1   (top = 5, n = 5)
#    Popping from top:  5(1st) 4(2nd=before-middle) 3(3rd=middle) ...
#    Middle         = 3  (3rd from top)
#    Before-middle  = 4  (2nd from top, encountered just before middle)
#    findBeforeMiddleElement(stack) -> 4
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

def findBeforeMiddleElement(stack):
    temp = Stack()
    middle = stack.getSize() // 2
    for _ in range(middle):
        temp.push(stack.pop())

    data = temp.peek()

    while not temp.isEmpty():
        stack.push(temp.pop())
    
    return data


# ============================================================
#  TEST RUNS -- do not modify
# ============================================================

def build_stack(values_bottom_to_top):
    """Push values so that the last item in the list ends up on top."""
    s = Stack()
    for v in values_bottom_to_top:
        s.push(v)
    return s

def stack_to_list(s):
    """Snapshot top-to-bottom without modifying the stack."""
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
    result = findBeforeMiddleElement(s)
    snapshot_after = stack_to_list(s)
    restored = snapshot_before == snapshot_after
    status = "PASS  ✓" if result == expected else f"FAIL  ✗  (got {result})"
    restore_status = "RESTORED ✓" if restored else "NOT RESTORED ✗"
    print(f"  Expected            : {expected}")
    print(f"  Your answer         : {result}   {status}")
    print(f"  Stack after call    : ", end=""); s.printStack()
    print(f"  Stack restore check : {restore_status}")

# Test 1 -- given example: top=5, bottom=1
# n=5, middle=pos3->3,  before-middle=pos2->4
run_test(
    "Test 1: stack top->bottom = [5 4 3 2 1]   (n=5, middle=3, before-middle=4)",
    values_bottom_to_top=[1, 2, 3, 4, 5],
    expected=4
)

# Test 2 -- n=4: top->bottom = [4 3 2 1]
# n=4, middle=pos3->2,  before-middle=pos2->3
run_test(
    "Test 2: stack top->bottom = [4 3 2 1]   (n=4, middle=2, before-middle=3)",
    values_bottom_to_top=[1, 2, 3, 4],
    expected=3
)

# Test 3 -- n=6: top->bottom = [6 5 4 3 2 1]
# n=6, middle=pos4->3,  before-middle=pos3->4
run_test(
    "Test 3: stack top->bottom = [6 5 4 3 2 1]   (n=6, middle=3, before-middle=4)",
    values_bottom_to_top=[1, 2, 3, 4, 5, 6],
    expected=4
)

# Test 4 -- n=7: top->bottom = [7 6 5 4 3 2 1]
# n=7, middle=pos4->4,  before-middle=pos3->5
run_test(
    "Test 4: stack top->bottom = [7 6 5 4 3 2 1]   (n=7, middle=4, before-middle=5)",
    values_bottom_to_top=[1, 2, 3, 4, 5, 6, 7],
    expected=5
)

# Test 5 -- different values, also checks restoration
# top->bottom = [10 20 30 40 50], n=5, middle=pos3->30, before-middle=pos2->20
run_test(
    "Test 5: stack top->bottom = [10 20 30 40 50]   restoration check",
    values_bottom_to_top=[50, 40, 30, 20, 10],
    expected=20
)
