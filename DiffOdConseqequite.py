l=[ 6,3,98,24,3,5,74,1,5,6,3]
l1=[]
for i in range(len(l)-1):
    l1.append(l[i]-l[i+1])
print(l1)