l=list(map(int,input("Enter the elements: ").split()))
t=0
for i in range(1,len(l),2):
    t+=l[i]
print("The sum of elements at odd indices is: ",t)