import re
s=input("Enter string")
res=re.sub(r"\d+","###",s)
print(res)
