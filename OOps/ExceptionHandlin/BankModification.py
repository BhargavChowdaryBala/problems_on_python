class InvalidAmountException(Exception):
    pass

class Bank:
    id=0
    def __init__(self,name1):
        Bank.id+=1
        self.name=name1
        self.acc_no=Bank.id
        self.balance=0
    def deposit(self,amount):
        self.balance=amount+self.balance
        print("Sucess")
    def withdrawl(self,a):
        try:
            if self.balance<a:
                raise InvalidAmountException
            else:
                self.balance-=a
        except InvalidAmountException:
            print("Invalid Amount")
    def checkBalance(self):
        print("Balance Amount : ",self.balance)
    def display(self):
        print("Name",self.name)
        print("Acc No",self.acc_no)
name=input("Enter Name : ")
b1=Bank(name)
while True:
    print("1.Deposit")
    print("2.WithDrawl")
    print("3.ChecKBalance")
    print("4.Display")
    print("5.Exit")
    ch=int(input())
    match ch:
        case 1:
            n=int(input("Enter Amount to Deposit : "))
            b1.deposit(n)
        case 2:
            n=int(input("Enter Amount to WithDrawl"))
            b1.withdrawl(n)
        case 3:
            b1.checkBalance()
        case 4:
            b1.display()
        case 5:
            exit()
        case _:
            print("Invalid Input...")