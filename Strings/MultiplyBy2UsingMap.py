def multiply(x):
    return x*2
l=list(map(int,input().split()))
# res=list(map(multiply,l))
# using lambda function instead of direct function
res=list(map(lambda x:x*2,l))    
print(res)