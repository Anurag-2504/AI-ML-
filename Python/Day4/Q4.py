'''
Q4 
    Create a class Shape with a method area().
    Create subclasses circle, rectangle , and triangle that override the area()
    method.

'''

class Shape:
    
    
    def area(self):
        return 0

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14*self.radius**2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(10, 3)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())