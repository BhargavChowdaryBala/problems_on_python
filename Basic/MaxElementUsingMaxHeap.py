import heapq
n=int(input())
l=[3,2,1,4,5,6]
h=[-x for x in l]
heapq.heapify(h)
va=(heapq.nsmallest(1,h))
print(-va[0])
