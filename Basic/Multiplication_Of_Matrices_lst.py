n=int(input())
l1=[]
l2=[]
for i in range(n):
    l3=list(map(int,input().split()))
    l1.append(l3)

for i in range(n):
    l4=list(map(int,input().split()))
    l2.append(l4)
    
for i in range(n):
    for j in range(n):
        print(l1[i][j],end=" ")
    print()
    
c=[]
for i in range(n):
    x=[]
    for j in range(n):
        t=0
        for k in range(n):
            t=t+l1[i][k]*l2[k][j]
        x.append(t)
    c.append(x)
        
for i in range(n):
    for j in range(n):
        print(c[i][j],end=" ")
    print()
