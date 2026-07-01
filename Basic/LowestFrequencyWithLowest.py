n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    val=d.get(i,0)+1
    d[i]=val
l=min(d.values())
l1=[]
for key,val in d.items():
    if(val==l):
        l1.append(key)
print(min(l1))

