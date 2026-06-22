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
        def middle(self):
            sp=self.head
            fp=self.head
            while(fp!=None and fp.next!=None):
                sp=sp.next
                fp=fp.next
                fp=fp.next
            print(sp.data)
     
        
        
l=LinkedList()
l1=list(map(int,input().split()))
for i in l1:
    l.insert_at_end(i)

l.middle()

