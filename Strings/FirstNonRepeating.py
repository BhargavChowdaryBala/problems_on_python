s="abcba"
d={}
for i in s:
    val=d.get(i,0)+1
    d[i]=val
for i in s:
    if(d.get(i)==1):
        print(i)
        break
else:
    print("-1")