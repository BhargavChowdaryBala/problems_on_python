s=input()
s=s.lower()
s1="aeiou"
c=0
for i in s:
    if i in s1:
        c=c+1
print(c)

