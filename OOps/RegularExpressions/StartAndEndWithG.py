import re


s=input()
res=re.findall(r"\bG\w*G\b",s)
print(res)
