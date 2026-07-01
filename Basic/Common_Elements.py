def common_elements(a, b):
    l=[]
    for i in a:
        if i in b:
            l.append(i)
    return l
l1=common_elements([1,2,3,4,5], [3,4,5,6,7])
print(l1)