l=list(map(int,input().split()))

l.sort()

print(l)
c=0
t=0
for i in range(1,len(l)):
    if(l[i-1]==l[i]):
        continue
    elif(l[i-1]+1==l[i]):
        c=c+1
        if(c>t):
            t=c
    else:

        c=0
print(t+1)