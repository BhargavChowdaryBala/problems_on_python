class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
     def __init__(self):
        self.head=None
     def insert_at_end(self,x):
        t=Node(x)
        if self.head is None:
            self.head=t
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=t
        return self.head
     def traversal(self):
        cur=self.head
        while cur!=None:
            print(cur.data,"->",end=" ")
            cur=cur.next
        print("none")
     def reverse(self):
            curr=self.head
            prev=None
            nt=self.head.next
            while(curr.next!=None):
                curr.next=prev
                prev=curr
                curr=nt
                nt=nt.next
            curr.next=prev
            self.head=curr
        
        
l=LinkedList()
l1=list(map(int,input().split()))
for i in l1:
    l.insert_at_end(i)
print(l.traversal())
l.reverse()
print(l.traversal())
