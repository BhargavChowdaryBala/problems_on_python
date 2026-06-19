s=input()
l=list(s.split())

s1=""
for i in l:
    s1=s1+i[::-1]+" "
print(s1)