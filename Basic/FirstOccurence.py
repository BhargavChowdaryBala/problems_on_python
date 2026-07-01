l=[1,2,3,1,4,3,5,3,2,4]
a=int(input("Enter the element to find the first occurrence: "))
t=0
for i in range(len(l)):
    if(l[i]==a):
        print("The first occurrence of the element is at index: ",i)
        t=1
        break
if(t==0):
    print("-1")