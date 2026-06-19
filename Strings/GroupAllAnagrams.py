s=["ate","eat","abc","xyz","bca","rat","art","can","xyz","tar"]
d={}
for i in s:
    key=''.join(sorted(i))
    
    val=d.get(key,0)
    if(val==0):
        l=[]
        l.append(i)
        d[key]=l
    else:
        d.get(key).append(i)
l1=[]
for key,val in d.items():
    l1.append(val)
print(l1)
