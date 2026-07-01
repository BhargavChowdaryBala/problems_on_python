n=int(input())
l=[]
for i in range(n):
    x=list(map(int,input().split()))
    l.append(x)
k=int(input())
l1=[]
t=False
for i in range(n):
    t=False
    for j in range(len(l[i])):
        if l[i][j]%k!=0:
            t=True
            break
    if t==False:
        l1.append(tuple(l[i]))
print(l1)
            
        
    
