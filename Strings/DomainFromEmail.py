s = input()
s1 = ""
for i in range(len(s)):
    if s[i] == "@":
        s1 = s[i+1:]
        break 
s2 = ""
for i in range(len(s1)):
    if s1[i] == ".":
        break
    else:
        s2=s2+s1[i]
print(s2)
