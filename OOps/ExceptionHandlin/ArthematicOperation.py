a=int(input())
b=int(input())
try:
    print(a+b)
    print(a-b)
    print(a//b)
    print(a%b)
except ZeroDivisionError:
    print("Error Occured Default Value is ",a//2)