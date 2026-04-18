# Create a class with:

# Private attributes
# Getters and Setters
# Data validation



# Class Person with:

# Private: __name, __age, __email
# Getter and Setter for each
# Validate:

# age must be 0-120
# email must contain @
# name can't be empty

class Person:
    def __init__(self, name, age, email):
        self.__name = ""
        self.__age = 0
        self.__email = ""
        self.set_name(name)
        self.set_age(age)
        self.set_email(email)

    def get_name(self):
        return self.__name
        
    def get_age(self):
        return self.__age
    
    def get_email(self):
        return self.__email
    
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Invalid name!")

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            print("Invalid age!")

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email!")


p = Person("Shrinath", 20, "shrinath@gmail.com")
print(p.get_name())   
print(p.get_age())    

p.set_age(150)        
p.set_email("wrong")  
p.set_email("s@uni.com")
p.set_name("")        

p.set_age(25)         
print(p.get_age())
print(p.get_email())
    
