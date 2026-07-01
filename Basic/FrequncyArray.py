n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    val=d.get(i,0)+1
    d[i]=val
for i in a:
    print(d.get(i),end=" ")