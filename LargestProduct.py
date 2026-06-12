l=list(map(int,input("Enter the elements: ").split()))
l.sort()
temp=l[0]*l[1]
temp1=l[len(l)-1]*l[len(l)-2]
if(temp>temp1):
    print("The largest product is: ",temp)
else:    print("The largest product is: ",temp1)