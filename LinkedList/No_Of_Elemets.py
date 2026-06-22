class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,x):
        t=Node(x)
        t.next=self.head
        self.head=t
        return self.head
    def display(self):
        c=0
        t=self.head
        while t is not None:
            c+=1
            t=t.next
        return c
l=LinkedList()
l1=list(map(int,input().split()))
for i in l1:
    l.insert_begin(i)
print(l.display())