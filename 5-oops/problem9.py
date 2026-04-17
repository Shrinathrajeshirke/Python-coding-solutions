# Create a class Student.

# Use a Class Attribute school_name = "Python Academy".

# Create a @classmethod called change_school(cls, new_name) that updates the class attribute.

# Create a @staticmethod called is_holiday(day) that returns True if the day is "Sunday". (Static methods don't need self or cls).

class Student:
    school_name = "ABC"
    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        return cls.school_name

    @staticmethod
    def is_holiday( day):
        if day == "Sunday":
            return True
        else:
            return False
        
print(Student.change_school("AI University"))
        
        