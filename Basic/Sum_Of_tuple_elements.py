n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=tuple(l)
s=0
for i in range(len(t)):
    s=s+t[i]
print("Total :",s)