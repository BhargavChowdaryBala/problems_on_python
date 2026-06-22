class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        t = Node(x)

        if self.head is None:
            self.head = t
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = t

    def traversal(self):
        cur = self.head
        while cur:
            print(cur.data, "->", end=" ")
            cur = cur.next
        print("None")


def add_lists(l1, l2):
    s1 = []
    s2 = []

    cur = l1.head
    while cur:
        s1.append(cur.data)
        cur = cur.next

    cur = l2.head
    while cur:
        s2.append(cur.data)
        cur = cur.next

    carry = 0
    result_head = None

    while s1 or s2 or carry:

        x = s1.pop() if s1 else 0
        y = s2.pop() if s2 else 0

        total = x + y + carry

        carry = total // 10
        digit = total % 10

        new_node = Node(digit)

        # insert at front
        new_node.next = result_head
        result_head = new_node

    res = LinkedList()
    res.head = result_head
    return res


# Input
l1 = LinkedList()
arr1 = list(map(int, input("List1: ").split()))

l2 = LinkedList()
arr2 = list(map(int, input("List2: ").split()))

for x in arr1:
    l1.insert_at_end(x)

for x in arr2:
    l2.insert_at_end(x)

ans = add_lists(l1, l2)

print("Result:")
ans.traversal()