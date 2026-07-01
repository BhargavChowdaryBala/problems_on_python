l=list(map(int,input("Enter the elements: ").split()))
l1=l[::-1]
if(l==l1):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")