a=int(input("Enter a number "))

if (a>0 and a%2==0):
    print("positive and even")
elif (a>0 and a%2!=0):
    print("positive and odd")
elif (a<0 and a%2==0):
    print("negative and even")
elif (a<0 and a%2!=0):
    print("negative and odd")
else:    
    print("zero")    