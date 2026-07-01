l=[1,2,3,4,5]
while True:
    print("1. append")
    print("2.pop")
    print("3. top")
    print("4. exit")
    print()
    c=int(input("Enter your choice"))
    match c:
        case 1:
            a=int(input("Enter element to append"))
            l.append(a)
            print("Stack is",l)
        case 2:
            if(len(l)<0):
                print("Stack is empty")

            else:
                e=l.pop()
                print("Popped element is",e)
                print("Stack is",l)
        case 3:
            if(len(l)<0):
                print("Stack is empty")
            else:
                print("Top element is",l[-1])
                print("Stack is",l)
        case 4:
            break
        case _:
            print("Invalid choice")

    print()