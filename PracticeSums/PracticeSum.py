s=input()
l=[]
n=len(s)
for i in range(n):
    for j in range(i+1,n):
        sub=s[i:j+1]
        rev=sub[:-1]
        if(sub==rev):
            l.append(sub)
print(l)
