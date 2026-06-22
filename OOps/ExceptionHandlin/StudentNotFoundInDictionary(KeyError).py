n=int(input())
d={}
for _ in range(n):
    key=input("Enter student name")
    val=input("Enter Grade")
    d[key]=val
try:
    s=input("Enter name ")
    print(d[s])
except KeyError:
    print("Student Not Found")