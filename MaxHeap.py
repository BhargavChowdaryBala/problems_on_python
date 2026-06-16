import heapq
l=[3,2,1,4,5,6]
h=[-x for x in l]
heapq.heapify(h)
while True:
    print("1.Add element")
    print("2.Remove element")
    print("3.Display min elment")
    print("4. display the heap")
    print("5.exit")
    ch=int(input("Enter choice"))
    match ch:
        case 1:
            x=int(input())
            heapq.heappush(l,x)
        case 2:
            var=heapq.heappop(l)
            print(var)
        case 3:
            var=heapq.nsmallest(1,l)
            print(var)
        case 4:
            print([-x for x in h])
        case 5:
            break
        case _:
            print("invalid")

