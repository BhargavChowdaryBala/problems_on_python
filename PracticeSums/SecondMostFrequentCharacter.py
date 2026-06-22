s=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
max1=0
max2=0
for key,val in d.items():
    max1=max(max1,val)
res=""
for key,val in d.items():
    if(val<max1 and val>max2):
        max2=val
        res=key
print(res)
