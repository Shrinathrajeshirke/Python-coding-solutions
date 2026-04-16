# Create a class Animal with a method speak() that returns "General sound".

# Create a class Dog that inherits from Animal and overrides speak() to return "Woof!".

# Create a class Cat that inherits from Animal and overrides speak() to return "Meow!".

# Goal: Create a list containing one Dog and one Cat. Loop through the list and call .speak() on each to see the different results.

class Animal:
    def speak(self):
        return "General sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(f"{animal.speak()}")