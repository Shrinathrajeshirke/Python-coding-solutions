# Create a class Temperature.

# Use a private attribute __celsius.

# Use @property to create a "getter" for celsius.

# Use @celsius.setter to ensure that if someone tries to set a temperature below -273.15, it prints an error instead of updating.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, temp):
        if temp < -273.15:
            raise ValueError("temperature can't be below -273.15")
        
        print(f"old temperature was {self._celsius}")
        self._celsius = temp
        print(f"new temperature is {self._celsius}")

temp1 = Temperature(26)

print(temp1.celsius)

temp1.celsius = 30