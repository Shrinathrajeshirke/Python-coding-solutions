# Parent: Device class → __init__ takes brand → method power_on() returns "{brand} is now ON".

# Child: Smartphone class → inherits from Device → adds method call() returns "Making a call...".

# Action: Create a Smartphone object, power it on, and make a call.

class Device:

    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        return f"{self.brand} is now ON."
    
class Smartphone(Device):
    def call(self):
        return "Making a call..."
    
object = Smartphone("Apple")

print(object.power_on())

print(object.call())


    
