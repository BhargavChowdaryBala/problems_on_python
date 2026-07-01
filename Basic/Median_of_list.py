def median_list(l):
    l = sorted(l)
    n = len(l)
    if n % 2:
        return l[n//2]
    return (l[n//2-1] + l[n//2]) / 2
print(median_list([1,2,3,4,5]))
print(median_list([1,2,3,4,5,6]))