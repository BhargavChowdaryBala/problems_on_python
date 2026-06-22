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
            while cur.next is not None:
                cur = cur.next
            cur.next = t

    def traversal(self):
        cur = self.head

        while cur is not None:
            print(cur.data, "->", end=" ")
            cur = cur.next

        print("None")

    def remove_duplicates(self):
        if self.head is None:
            return

        prev = self.head
        curr = self.head.next

        while curr is not None:
            if prev.data == curr.data:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next


l = LinkedList()

l1 = list(map(int, input().split()))

for i in l1:
    l.insert_at_end(i)

l.remove_duplicates()
l.traversal()