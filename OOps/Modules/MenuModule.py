import Calci2
import NumberOperations
while True:
    print("1. Arithmatic Operations")
    print("2. MenuDriven on an Integer")
    print("3. exit")
    ch=int(input("Enter your choice"))
    match ch:
        case 1:
            x,y=map(int,input("Enter the numbers space seperated").split())
            print("Sum is :",Calci2.add(x,y))
            print("Subtraction is :",Calci2.sub(x,y))
            print("Multiplication is :",Calci2.multiply(x,y))
            try:
                print("float Division :",Calci2.floatdivision(x,y))
                print("integer division :",Calci2.intdivision(x,y))
                print("modulo division :",Calci2.modulodivision(x,y))
            except ZeroDivisionError:
                print("Can't divisible by Zero")
        case 2:
            x=int(input("Enter a number"))
            print("Double of the number :",NumberOperations.double(x))
            print("Half of the number :",NumberOperations.halfnumber(x))
            print("Square of the number :",NumberOperations.square(x))
            print("Cube of the number :",NumberOperations.cube(x))
        case 3:
            break