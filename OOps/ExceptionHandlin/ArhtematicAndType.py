a=input()
b=input()
try:
    a1=int(a)
    b1=int(b)
    c=a1//b1
except ValueError:
    print("Enter the integer inputs onlyy")
except ZeroDivisionError:
    print("The denominator cant be zeroo")