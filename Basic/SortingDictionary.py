d=dict({"india":30, "usa":20, "china":40, "japan":10})
new_dict=dict(sorted(d.items(),key=lambda x:x[0]))
new_dict1=dict(sorted(d.items(),key=lambda x:x[1]))
new_dict2=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))



print("old dictionary:",d)
print("new dictionary:",new_dict)
print("sorted according to values in ascending order dictionary:",new_dict1)
print("sorted according to values in descending order dictionary:",new_dict2)
