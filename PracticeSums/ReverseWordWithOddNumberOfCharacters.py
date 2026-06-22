s=input()
l=s.split()
res=[]
for i in l:
    if len(i)%2!=0:
        res.append(i[::-1])
    else:
        res.append(i)
print(" ".join(res))