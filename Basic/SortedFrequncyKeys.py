n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    val=d.get(i,0)+1
    d[i]=val
d1=dict(sorted(d.items(),key=lambda x:x[0]))
print(d1)