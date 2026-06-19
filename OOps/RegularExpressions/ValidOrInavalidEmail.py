import re
s=input("Enter email")
if re.search(r"[a-zA-Z0-9]+@gmail\.[com,in]",s):
    print("Valid email")
else:
    print("Invalid")