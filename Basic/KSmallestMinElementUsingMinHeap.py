import heapq
k=int(input())
l=[3,2,1,4,5,6,13]
heapq.heapify(l)
l1=(heapq.nsmallest(k,l))
print(l1[-1])

