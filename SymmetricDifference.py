a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))