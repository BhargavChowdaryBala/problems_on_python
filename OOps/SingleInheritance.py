class Rectangle:
    def __init__(self):
        self._length = int(input("Enter Length :"))
        self._breadth = int(input("Enter Breadth :"))
    def area(self):
        return self._length * self._breadth 
    
    def perimeter(self):
        return (2*self._length) + (2*self._breadth)


class Cuboid(Rectangle):
    def __init__(self):
        super().__init__()
        self.__height = int(input("Enter Height:"))

    def cuboid_volume(self):
        return self._length * self._breadth * self.__height 
    
    def cuboid_area(self):
        return 2*(self._length + self._breadth + self.__height)
obj=Cuboid()
print("volume:",obj.cuboid_volume())
print("area:",obj.cuboid_area())
print("Area of rectangle",obj.area())
print("perimiter of recatngle ",obj.perimeter())
