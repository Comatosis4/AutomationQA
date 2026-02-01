class Figure:
    def perimeter(self):
        pass
    def area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side
    def area(self):
        areas = self.__side**2
        print(f'Площа квадрата = {areas}')
    def perimeter(self):
        perimeter = self.__side*4
        print(f'Периметр квадрата = {perimeter}')

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        areas = self.__radius**2*3.1415
        print(f'Площа кола = {round(areas, 3)}')
    def perimeter(self):
        perimeter = self.__radius*2*3.1415
        print(f'Периметр колаа = {perimeter}')

class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2
    def area(self):
        areas = self.__side1*self.__side2
        print(f'Площа прямокутникаа = {areas}')
    def perimeter(self):
        perimeter = (self.__side1+self.__side2)*2
        print(f'Периметр прямокутника = {perimeter}')

square = Square(2)
circle = Circle(3)
rectangle = Rectangle(4, 5)

list1 = [square, circle, rectangle]
for item in list1:
    item.area()
    item.perimeter()
