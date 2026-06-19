s=input()
l=list(s.split())
res=""
for i in l:
    res= res+i[0]+i[(len(i)-1)//2]+i[len(i)-1]
print(res)