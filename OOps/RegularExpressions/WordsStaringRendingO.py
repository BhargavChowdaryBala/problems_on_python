import re
s=input("enter string")
res=re.findall(r"\br\w*o\b",s)
print(res)