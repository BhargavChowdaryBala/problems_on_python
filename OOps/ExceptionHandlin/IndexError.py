l=list(map(int,input().split()))
try:
    c=0
    for i in l:
        c=c+i
    print("sum ",c)
    print("avg",c//len(l))
    print("max is",max(l))
    print("min is ",min(l))
    index=int(input("Enter index number"))
    print(l[index])
except IndexError:
    print("Enter the correct index")
