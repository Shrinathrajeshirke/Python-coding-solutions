# Create a Parent class Person with __init__ taking name.

# Create a Child class Employee that inherits from Person.

# The Employee __init__ should take name AND salary.

# Crucial Step: Use super().__init__(name) to let the Parent handle the name, and then set the salary in the Child.

# Add a method to Employee to display both.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        return f"salary of {self.name} is {self.salary}"
    
employee1 = Employee("abc", 100000)

print(employee1.display())
