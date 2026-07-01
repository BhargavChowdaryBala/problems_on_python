def rotate_right(l, n):

    n %= len(l)
    l1 = l[len(l) - n:] + l[:len(l) - n]
    return l1


print(rotate_right([1,2,3,4,5], 2))
print(rotate_right([10,20,30], 1))
print(rotate_right([1,2,3], 3))
print(rotate_right([7], 10))
print(rotate_right([1,2,3,4], 0))
print(rotate_right([1,2,3,4], 6))