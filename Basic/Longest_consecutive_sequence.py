def longest_consecutive_sequence(l):
    s = set(l)
    best = []
    for x in s:
        if x - 1 not in s:
            cur = []
            y = x
            while y in s:
                cur.append(y)
                y += 1
            if len(cur) > len(best):
                best = cur
    print(len(best))
    print(*best)
longest_consecutive_sequence([100,4,200,1,3,2])
longest_consecutive_sequence([20,19,18,17,16])
longest_consecutive_sequence([10,3,7,2,1,8,6,4,11,5])
longest_consecutive_sequence([10,1,2,11,15])