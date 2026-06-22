# s=input()
# b=False
# for i in range(len(s)):
#     r=s[i:]+s[:i]
#     if (r==r[::-1]):
#         b=True
# if(b):
#     print("Yes")
# else:
#     print("NO")



s=input()
d={}
n=len(s)
for i in range(n):
    d[s[i]]=d.get(s[i],0)+1
b=True
c=0
if(n%2==0):
    for key,val in d.items():
        if(val%2!=0):
            b=False

else:
    for key,val in d.items():
        if(val%2!=0):
            c=c+1
            if(c>1):
                b=False
if(b==False):
    print("No")
else:
    f=False
    for i in range(len(s)):
        r=s[i:]+s[:i]
        if(r==r[::-1]):
            f=True
            break
    if(f):
        print("Yes")
    else:
        print("No")
    

