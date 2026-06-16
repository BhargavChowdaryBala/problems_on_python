import heapq
k=int(input())
l=[3,2,1,4,5,6,13]
h=[-x for x in l]
heapq.heapify(h)
l1=(heapq.nsmallest(k,h))
print(-l1[-1])

