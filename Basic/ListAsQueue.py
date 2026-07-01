l=[1,2,3,4,5]
while True:
    print("1. enqueue")
    print("2.dequeue")
    print("3. front")
    print("4. Rear")
    print("5. exit")
    print()
    c=int(input("Enter your choice"))
    match c:
        case 1:
            a=int(input("Enter element to append"))
            l.append(a)
            print("Queue is",l)
        case 2:
            if(len(l)<0):
                print("Queue is empty")

            else:
                e=l.pop(0)
                print("Popped element is",e)
                print("Queue is",l)
        case 3:
            if(len(l)<0):
                print("Queue is empty")
            else:
                print("Top element is",l[0])
                print("Queue is",l)
        case 4:
            if(len(l)<0):
                print("Queue is empty")
            else:
                print("Rear element is",l[-1])
                print("Queue is",l)

        case 5:
            break
        case _:
            print("Invalid choice")

    print()