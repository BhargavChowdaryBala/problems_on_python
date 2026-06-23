class Complex_numbers:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def __add__(self, p1):
        p3=Complex_numbers()
        p3.r=self.r+p1.r
        p3.i=self.i+p1.i
        return p3
    def __sub__(self, p1):
        p3=Complex_numbers()
        p3.r=self.r-p1.r
        p3.i =self.i-p1.i
        return p3
    
    def show(self):
        print(f"{self.r}+{self.i}j")
c1=Complex_numbers(4,3)
c2=Complex_numbers(3,6)
c3=c1+c2
c4=c1-c2
c3.show()
c4.show()