def remove_even_indices(l):
    return [l[i] for i in range(len(l)) if i % 2 == 1]
print(remove_even_indices([1,2,3,4,5,6]))