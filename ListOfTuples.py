n=int(input("Enter number of elements :    "))
l=[]
for i in range(n):
    l1=[]
    x=int(input("Enter element : "))
    l1.append(x)
    l1.append(x**2)
    l1.append(x**3)
    l.append(tuple(l1))
print(l)