class Circle :
    def __init__(self):
        self._radius = int(input("Enter Radius :"))
    def area(self):
        return 3.14 * (self._radius ** 2)
     


class Cylinder(Circle):
    def __init__(self):
        super().__init__()
        self.__height = int(input("Enter Height of The cylinder :"))
    

    def vloume(self):
        return 3.14 * (self._radius**2) * self.__height

Cobj = Cylinder()

print(Cobj.area())
print(Cobj.vloume())


class Spehere(Circle) :
    def __init__(self):
        super().__init__()
    def volume(self):
        return (4/3) * (3.14) * (self._radius**3)

sobj = Spehere()
sobj.volume()