n = int(input())
l = []
for i in range(n):
    x = tuple(map(int, input().split()))
    l.append(x)

l.sort(key=lambda t: t[1])

print(l)
