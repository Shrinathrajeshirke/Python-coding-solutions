# Class Animal (parent)

# name, sound, legs
# speak() → "name says sound"
# describe() → describes animal


# Class Dog(Animal)

# extra: breed
# fetch() → "Dog is fetching!"
# Override speak()


# Class Bird(Animal)

# extra: can_fly
# fly() → "Bird is flying!" or
# "Bird cannot fly!"
# Override speak()

class Animal:
    def __init__(self, name, sound, legs):
        self.name = name
        self.sound = sound
        self.legs = legs

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def describe(self):
        print(f"{self.name} is animal with {self.legs} legs")

    def fetch(self):
        print(f"{self.name} is fetching...")

class Dog(Animal):
    def __init__(self, name, sound, legs, breed):
        super().__init__(name, sound, legs)
        self.breed = breed

    def speak(self):
        return super().speak()

    def fetch(self):
        return super().fetch()    

    def describe(self):
        super().describe()
        print(f"Breed: {self.breed}")

class Bird(Animal):
    def __init__(self, name, sound, legs, can_fly):
        super().__init__(name, sound, legs)
        self.can_fly = can_fly

    def speak(self):
        return super().speak()   

    def describe(self):
        super().describe()

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying")
        else:
            print(f"{self.name} can not fly")


d = Dog("Rex", "Woof", 4, "Labrador")
b = Bird("Parrot", "Hello", 2, True)
e = Bird("Penguin", "Squawk", 2, False)

d.speak()
d.fetch()
d.describe()

b.speak()
b.fly()

e.speak()
e.fly()