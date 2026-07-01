print("Enter the elements")
l=list(map(int,input().split()))
print("Enter the element to find the distance")
a=int(input())
i=0
j=len(l)-1
while(i<j):
    if(l[i]==a and l[j]==a):
        print(j-i)
        break
    elif(l[i]!=a):
        i=i+1
    else:
        j=j-1