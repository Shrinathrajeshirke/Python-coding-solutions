# Create a class Engine with a method start() that returns "Engine started".

# Create a class Car. In its __init__, create an instance of Engine and store it in self.engine.

# Add a method drive() to Car that calls self.engine.start().

class Engine:
    def start(self):
        return "Engine started"
    
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
    
my_car = Car()

print(my_car.start())

        