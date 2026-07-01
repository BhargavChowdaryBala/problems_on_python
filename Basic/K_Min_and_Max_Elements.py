l=list(map(int,input().split()))
k=int(input("Enter k : "))
t=tuple(l)
t1=sorted(t)
l1=[]
l2=[]
for i in range(k):
    l1.append(t1[i])
    l2.append(t1[len(l)-i-1])
print(l1)
print(l2)