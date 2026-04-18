# Create a class Shape and child classes:

# Parent: Shape with method area()
# and perimeter()
# Child 1: Circle with radius
# Child 2: Rectangle with length, width
# Child 3: Triangle with a, b, c sides

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
    def display(self):
        print(f"Circle -> Area: {self.area()} -> Perimeter: {self.perimeter()}")
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def display(self):
        print(f"Rectangle -> Area: {self.area()} -> Perimeter: {self.perimeter()}")  
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c)/2
        a = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return a
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def display(self):
        print(f"Triangle -> Area: {self.area()} -> Perimeter: {self.perimeter()}")

c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(3, 4, 5)

c.display()
r.display()
t.display()

    

        