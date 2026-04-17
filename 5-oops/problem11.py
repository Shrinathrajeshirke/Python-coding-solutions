# Create a class Person with:

# Attributes: name, age, city
# Method: introduce() that prints
# a self introduction
# Method: is_adult() that returns
# True if age >= 18

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"My name is {self.name}. I'm {self.age} years old. I'm from {self.city}")

    def is_adult(self):
        return self.age >= 18
    
person1 = Person("abc", 20, "AU")

person1.introduce()

print(f"Is adult: {person1.is_adult()}")
        