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
        def nth_from_front(self,n):
            cur=self.head
            c=1

            while(cur!=None):
                if(c==n):
                    print(cur.data)
                    return
                cur=cur.next
                c+=1

            print("Position out of range")


        def nth_from_last(self,n):
            cur=self.head
            l=0
            while(cur!=None):
                l+=1
                cur=cur.next
            pos=l-n+1
            cur=self.head
            c=1
            while(cur!=None):
                if(c==pos):
                    print(cur.data)
                    return
                cur=cur.next
                c+=1
            
l=LinkedList()
l1=list(map(int,input().split()))

for i in l1:
    l.insert_at_end(i)

n=int(input("Enter n: "))

print("Nth element from front:")
l.nth_from_front(n)

print("Nth element from last:")
l.nth_from_last(n)

