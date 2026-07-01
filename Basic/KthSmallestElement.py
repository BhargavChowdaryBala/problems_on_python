def quickSelect(a, l, h):
    pivot = a[h]
    ploc = l
    for j in range(l, h):
        if a[j] <= pivot:
            a[j], a[ploc] = a[ploc], a[j]
            ploc += 1            
    a[h], a[ploc] = a[ploc], a[h]
    return ploc
def kthSmallest(a, l, h, k):
    if l <= h:
        pos = quickSelect(a, l, h)
    
        if pos == k - 1:
            return a[pos]
        elif pos < k - 1:
            return kthSmallest(a, pos + 1, h, k)
        else:
            return kthSmallest(a, l, pos - 1, k)
    return -1
n = int(input())
a = list(map(int, input().split()))
k = int(input())
res = kthSmallest(a, 0, n - 1, k)

print(res)
