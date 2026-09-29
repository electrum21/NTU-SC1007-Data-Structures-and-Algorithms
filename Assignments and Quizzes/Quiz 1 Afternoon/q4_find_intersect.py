# ============================================================
#  Q4 — Intersect of Two Singly Linked Lists
#
#  Write findIntersect(ll1, ll2) — return a NEW linked list
#  containing values that appear in BOTH ll1 and ll2.
#  Result must be ordered by ll1 (same order values appear in ll1).
#  No duplicate values in the result.
#
#  No sets, dicts, or arrays allowed.
#
#  Example:
#    ll1 = 1 -> 3 -> 5 -> 7 -> 9
#    ll2 = 3 -> 5 -> 6 -> 7 -> 8
#    intersect (ordered by ll1) = 3 -> 5 -> 7
#
#  Example 2 (unsorted lists):
#    ll1 = 5 -> 1 -> 3 -> 7
#    ll2 = 7 -> 3 -> 9 -> 1
#    intersect (ordered by ll1) = 1 -> 3 -> 7
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

def findIntersect(ll1, ll2):
    new_ll = LinkedList()
    new_ll_index = 0
    prev_in_new_ll = None

    cur1 = ll1.head
    while cur1:                            # walk list1 in order
        cur2 = ll2.head
        while cur2:                        # search all of list2
            if cur1.item == cur2.item:     # match found
                # avoid inserting duplicates
                if prev_in_new_ll is None or cur1.item != prev_in_new_ll.item:
                    new_ll.insertNode(cur1.item, new_ll_index)
                    prev_in_new_ll = new_ll.findNode(new_ll_index)
                    new_ll_index += 1
                break                      # no need to keep searching list2
            cur2 = cur2.next
        cur1 = cur1.next

    return new_ll


# ============================================================
#  TEST RUNS — do not modify
# ============================================================

def build_ll(values):
    ll = LinkedList()
    for i, v in enumerate(values):
        ll.insertNode(v, i)
    return ll

def ll_to_list(ll):
    items = []
    current = ll.head
    while current:
        items.append(current.item)
        current = current.next
    return items

def run_test(label, vals1, vals2, expected):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    ll1 = build_ll(vals1)
    ll2 = build_ll(vals2)
    print(f"  ll1      : {vals1}")
    print(f"  ll2      : {vals2}")
    result_ll = findIntersect(ll1, ll2)
    if result_ll is None:
        result = []
    elif isinstance(result_ll, LinkedList):
        result = ll_to_list(result_ll)
    else:
        # handle if a Node (head) is returned instead of a LinkedList
        items = []
        cur = result_ll
        while cur:
            items.append(cur.item)
            cur = cur.next
        result = items
    status = "PASS ✓" if result == expected else f"FAIL ✗  (got {result})"
    print(f"  Expected : {expected}")
    print(f"  Your ans : {result}")
    print(f"  Result   : {status}")

# Test 1 — standard sorted intersect
run_test(
    "Test 1: sorted lists with common elements",
    [1, 3, 5, 7, 9],
    [3, 5, 6, 7, 8],
    expected=[3, 5, 7]
)

# Test 2 — unsorted lists, order follows ll1
run_test(
    "Test 2: unsorted lists, result ordered by ll1",
    [5, 1, 3, 7],
    [7, 3, 9, 1],
    expected=[1, 3, 7]
)

# Test 3 — no common elements
run_test(
    "Test 3: no common elements",
    [1, 2, 3],
    [4, 5, 6],
    expected=[]
)

# Test 4 — all elements in common
run_test(
    "Test 4: all elements common (same list)",
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    expected=[1, 2, 3, 4, 5]
)

# Test 5 — duplicates in ll1, result should not have duplicates
run_test(
    "Test 5: duplicate values in ll1, no duplicates in result",
    [1, 3, 3, 5, 7],
    [3, 5, 9],
    expected=[3, 5]
)

# Test 6 — one empty list
run_test(
    "Test 6: ll2 is empty",
    [1, 2, 3],
    [],
    expected=[]
)
