n=int(input())
l=[]
for i in range(n):
    x=list(map(int,input().split()))
    l.append(x)
l1=[]
for i in range(n):
    l1.append(len(l[i]))
l2=list(zip(l1,l))
l2.sort()
print(l2)
