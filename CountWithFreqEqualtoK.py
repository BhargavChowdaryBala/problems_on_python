n=int(input())
k=int(input("Enter k"))
a=list(map(int,input().split()))
d={}

for i in a:
    val=d.get(i,0)+1
    d[i]=val
c=0
for key,val in d.items():
    if(val==k):
        c=c+1
print(c)