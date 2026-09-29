# ============================================================
#  Q1 — Reverse Between Specified Indexes
#
#  You are NOT given head. Use ll.findNode(index) to locate nodes.
#  You ARE allowed 1 temporary linked list (tempList).
#
#  reverseBetween(ll, m, n):
#    - Reverse the nodes at indexes m..n (inclusive) in ll
#    - Store the reversed segment in tempList
#    - Print tempList using tempList.printList()
#    - ll itself should also reflect the reversal
#
#  Example:
#    ll      = 1 2 3 4 5 6
#    reverseBetween(ll, 2, 3)
#    tempList prints: 4 3
#    ll becomes:      1 2 4 3 5 6
# ============================================================

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertNode(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def removeNode(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def findNode(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def printList(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.item))
            current = current.next
        print(" -> ".join(items) if items else "Empty list")


# ============================================================
#  YOUR SOLUTION HERE
# ============================================================

def reverseBetween(ll, m, n):
    tempList = LinkedList()

    # m and n inclusive
    i = m
    while i <= n:
        node = ll.findNode(i)
        tempList.insertNode(node.item, 0)
        i += 1
    
    print("My templist:")
    tempList.printList()

    j = m
    while j <= n:
        cur = ll.findNode(j)
        cur.item = tempList.findNode(j - m).item
        j += 1
    
    print("My ll")
    ll.printList()


# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def build_ll(values):
    ll = LinkedList()
    for i, v in enumerate(values):
        ll.insertNode(v, i)
    return ll

def run_test(label, values, m, n, expected_ll, expected_temp):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    ll = build_ll(values)
    print(f"  ll before  : {values}")
    print(f"  Call       : reverseBetween(ll, {m}, {n})")
    print(f"  tempList   (expected): {expected_temp}")
    print(f"  ll after   (expected): {expected_ll}")
    print(f"  --- your output ---")
    print(f"  tempList   : ", end="")
    reverseBetween(ll, m, n)
    print(f"  ll after   : ", end="")
    ll.printList()

# Test 1 — given example
run_test(
    "Test 1: reverseBetween(ll, 2, 3)  — middle segment",
    [1, 2, 3, 4, 5, 6], 2, 3,
    expected_ll   = [1, 2, 4, 3, 5, 6],
    expected_temp = [4, 3]
)

# Test 2 — reverse from index 0 (includes head)
run_test(
    "Test 2: reverseBetween(ll, 0, 2)  — from head",
    [1, 2, 3, 4, 5, 6], 0, 2,
    expected_ll   = [3, 2, 1, 4, 5, 6],
    expected_temp = [3, 2, 1]
)

# Test 3 — reverse to last index (includes tail)
run_test(
    "Test 3: reverseBetween(ll, 3, 5)  — to tail",
    [1, 2, 3, 4, 5, 6], 3, 5,
    expected_ll   = [1, 2, 3, 6, 5, 4],
    expected_temp = [6, 5, 4]
)

# Test 4 — single element (no-op)
run_test(
    "Test 4: reverseBetween(ll, 2, 2)  — single element, no change",
    [1, 2, 3, 4, 5, 6], 2, 2,
    expected_ll   = [1, 2, 3, 4, 5, 6],
    expected_temp = [3]
)

# Test 5 — whole list reversed
run_test(
    "Test 5: reverseBetween(ll, 0, 5)  — entire list",
    [1, 2, 3, 4, 5, 6], 0, 5,
    expected_ll   = [6, 5, 4, 3, 2, 1],
    expected_temp = [6, 5, 4, 3, 2, 1]
)
