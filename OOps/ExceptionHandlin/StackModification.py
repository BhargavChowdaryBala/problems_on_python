class StackException(Exception):
    pass

def push(x):
     stack.append(x)
     print(stack)
def pop():
    try:
        if len(stack)>0:
            print(stack.pop())
            print(stack)
        else:
            raise StackException
    except StackException:
        print("Stack does't have elements..")
def top():
    return stack[-1]
def isEmpty():
    if len(stack)==0:
        return True
    else:
        return False
def size():
    if len(stack)==0:
        return 0 
    return len(stack)
stack=[]
while True:
    print("MENU:")
    print("1.Push")
    print("2.Pop")
    print("3.Top")
    print("4.IsEmpty")
    print("5.Size")
    print("6.Exit")
    
    ch=int(input())
    match ch:
        case 1:
            x=int(input())
            push(x)
        case 2:
            pop()
        case 3:
            print(top())
        case 4:
            print(isEmpty())
        case 5:
            print(size())
        case 6:
            break
        case _:
            print("Invalid input")