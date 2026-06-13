n = int(input())

l1_list = []
for i in range(n):
    l3 = tuple(map(int, input().split()))
    l1_list.append(l3)
l1 = tuple(l1_list)

l2_list = []
for i in range(n):
    l4 = tuple(map(int, input().split()))
    l2_list.append(l4)
l2 = tuple(l2_list)
    
for i in range(n):
    for j in range(n):
        print(l1[i][j], end=" ")
    print()
    
c_list = []
for i in range(n):
    x_list = []
    for j in range(n):
        t = 0
        for k in range(n):
            t = t + l1[i][k] * l2[k][j]
        x_list.append(t)
    c_list.append(tuple(x_list))
c = tuple(c_list)
        
for i in range(n):
    for j in range(n):
        print(c[i][j], end=" ")
    print()
