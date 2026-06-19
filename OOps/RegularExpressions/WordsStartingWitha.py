# import re
# s=input("Enter the string")
# l=s.split(" ")
# l1=[]
# for i in l:
#      if re.search(r"^a", i,re.IGNORECASE):
#           l1.append(i)
# print(l1)

import re
s = input("Enter the string: ")
res = re.findall(r"\ba\w*", s,)
print(res)

