s=input("Enter the string: ")
res=""
for i in s:
    if i.isupper():
        res+=i
print(res)