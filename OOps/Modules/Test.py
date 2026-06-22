import Calc
try:
    a=int(input("Enter a number"))
    b=int(input("Enter b number"))
    res=Calc.add(a,b)
    res1=Calc.sub(a,b)
    res2=Calc.multiply(a,b)
    res3=Calc.div(a,b)
    print(res)
    print(res1)
    print(res2)
    print(res3)

except ZeroDivisionError:
    print("div not posible")