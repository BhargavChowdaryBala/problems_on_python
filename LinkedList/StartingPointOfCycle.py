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
        def check_cycle(self):
            sp=self.head
            fp=self.head.next
            while(fp!=None and fp.next!=None):
                if(sp==fp):
                    return sp.data
                sp=sp.next
                fp=fp.next
                fp=fp.next
            return False
        def add_cycle(self):
            curr=self.head
            while(curr.next!=None):
                prev=curr
                curr=curr.next
            curr.next=prev
            

            
l=LinkedList()
l1=list(map(int,input().split()))

for i in l1:
    l.insert_at_end(i)


l.add_cycle()
print("Cycle present at")

print(l.check_cycle())






