n=int(input())
l=[]
for i in range(n):
    x=list(map(int,input().split()))
    l.append(x)
k=int(input())
l1=[]
for i in range(n):
    if(len(l[i])==k):
        l1.append(tuple(l[i]))
print(l1)
            
        
    
