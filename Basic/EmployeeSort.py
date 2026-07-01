l=[]
n=int(input())
for i in range(n):
    l1=list(map(str,input().split()))
    l.append(l1)
print("1 for sort by employee name")
print("2 for sort by employee job")
print("3 for sort by employee salary")
print("4 for sort by employee location")
print("5 for sort by job and salary")
print("6 for sort by grade and job")
print("7 for sort by grade and salary")
print("8 for exit")
while True:
    c=int(input())
    match c:
        case 1:
            l.sort(key=lambda x:x[1])
            print(l)
        case 2:
            l.sort(key=lambda x:x[2])
            print(l)
        case 3:
            l.sort(key=lambda x:x[3])
            print(l)
        case 4:
            l.sort(key=lambda x:x[5])
            print(l)
        case 5:
            l.sort(key=lambda x:(x[2],x[3]))
            print(l)
        case 6:
            l.sort(key=lambda x:(x[0],x[2]))
            print(l)
        case 7:
            l.sort(key=lambda x:(x[0],x[3]))
            print(l)
        case 8:
            break
        case _:
            print("invalid input")
