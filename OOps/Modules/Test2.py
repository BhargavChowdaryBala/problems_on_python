import Calc1
x=int(input("Enter a number"))
y=int(input("Enter b number"))
while True:
    try:
        print("1. add")
        print("2. substract")
        print("3. integer division")
        print("4. Modular Division")
        print("5. Float Division")
        print("6.multiply")
        print("7.exit")
        print()
        print("Enter your choice")
        ch=int(input())
        match ch:
            case 1:
                print(Calc1.add(x,y))
            case 2:
                print(Calc1.sub(x,y))
            case 3:
                print(Calc1.intdiv(x,y))
            case 4:
                print(Calc1.moddiv(x,y))
            case 5:
                print(Calc1.floatdiv(x,y))
            case 6:
                print(Calc1.multiply(x,y))
            case 7:
                break
            case _:
                print("Invalid Input")
        print()
    except ZeroDivisionError:
        print("b cant be zerooo")
            