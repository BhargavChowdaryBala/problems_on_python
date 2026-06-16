d={
    "i101":{"name":"paper","price":160,"qty":20},
    "i202":{"name":"Tv","price":6000,"qty":32},
    "i303":{"name":"laptop","price":72000,"qty":29}
}

while True:
    print("1.sort by name")
    print("2.sort by price")
    print("3.sort by quantity")
    print("4.sort by name and price")
    print("5.sort by name and quantity")
    print("6.sort by price and quanityt")
    print("7,sort by name and price and quantity")
    print("8. exit")
    c=int(input("enter choice"))
    match c:
        case 1:
            new_dict=dict(sorted(d.items(),key=lambda x:x[1]["name"]))
            new_dict1=dict(sorted(d.items(),key=lambda x:x[1]["name"],reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 2:
            new_dict=dict(sorted(d.items(),key=lambda x:x[1]["price"]))
            new_dict1=dict(sorted(d.items(),key=lambda x:x[1]["price"],reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 3:
            new_dict=dict(sorted(d.items(),key=lambda x:x[1]["qty"]))
            new_dict1=dict(sorted(d.items(),key=lambda x:x[1]["qty"],reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 4:
            new_dict=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["price"])))
            new_dict1=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["price"]),reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 5:
            new_dict=dict(sorted(d.items(),key=lambda x:(x[1]["price"],x[1]["qty"])))
            new_dict1=dict(sorted(d.items(),key=lambda x:(x[1]["price"],x[1]["qty"]),reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 6:
            new_dict=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["qty"])))
            new_dict1=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["qty"]),reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 7:
            new_dict=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["price"],x[1]["qty"])))
            new_dict1=dict(sorted(d.items(),key=lambda x:(x[1]["name"],x[1]["price"],x[1]["qty"]),reverse=True))
            print("sorted dictionary according to ascending and descending ")
            print("ascending : ",new_dict)
            print("descending",new_dict1)
        case 8:
            break
        case _:
            print("Invalis")
            

