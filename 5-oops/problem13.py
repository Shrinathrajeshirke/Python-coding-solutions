# Create a class Student with:

# Attributes: name, marks (list of 5 subjects)
# Method: get_total() → returns total
# Method: get_average() → returns average
# Method: get_grade() → returns grade
# Method: display() → prints full report

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_total(self):
        return sum(self.marks)
    
    def get_average(self):
        return round(self.get_total()/len(self.marks),2)
    
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def display(self):
        print("Output: ")
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.get_total()}")
        print(f"Average: {self.get_average()}")
        print(f"Grade: {self.get_grade()}")

s = Student("Shrinath", [82, 92, 78, 95, 88])
s.display()