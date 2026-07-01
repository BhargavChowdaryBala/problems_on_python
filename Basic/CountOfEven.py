l=list(map(int,input().split()))
e=0
o=0
for i in l:
    if(i%2==0):
        e=e+1
    else:
        o=o+1
print(e)
print(o)