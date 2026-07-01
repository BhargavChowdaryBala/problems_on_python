n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    val=d.get(i,0)+1
    d[i]=val
print(d)