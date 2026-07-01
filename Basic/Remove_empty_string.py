def remove_empty_strings(lst):
    return [x for x in lst if x]
print(remove_empty_strings(["Mike", "", "Emma", "Kelly", "", "Brad"]))