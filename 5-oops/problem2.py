# Create a class named SmartWatch.

# In __init__, set a private attribute __steps to 0.

# Add a method add_steps(count) that adds the count to __steps.

# Add a method get_steps() that returns the current step count.

# Constraint: Try to access print(your_object.__steps) directly from outside the class and see what happens.

class Smartwatch():
    def __init__(self, steps):
        self.__steps = steps

    def add_steps(self, count):
        self.__steps += count

    def get_steps(self):
        return self.__steps
    
watch = Smartwatch(10000)

watch.add_steps(2000)

print(watch.get_sSteps())