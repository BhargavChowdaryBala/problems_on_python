s=input()
c=0
max1=0
for i in range(1,len(s)):
    if(s[i-1]==s[i]):
        c=c+1
        max1=max(c,max1)
    else:
        c=0
print(max1+1)