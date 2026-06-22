def File(f_name):
    f=None
    f=open(f_name,'r')
    return f.readlines()
try:
    a=input()
    print(len(File(a)))
    
except FileNotFoundError:
    print("File Not Exits")