# Import ABC and abstractmethod from the abc module.

# Create an abstract class Shape.

# Define an abstract method area(self).

# Create a class Square that inherits from Shape and implements the area logic (side * side).

# Try this: Try to create an object of Shape directly and see if Python stops you!

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side= side

    def area(self):
        area_of_square = self.side*self.side
        return area_of_square
    
square = Square(5)

print(square.area())