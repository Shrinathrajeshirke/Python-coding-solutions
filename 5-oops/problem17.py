# Create a class Employee with:

# Attributes: name, salary, department
# Method: get_details()
# Method: get_annual_salary()

# Child class Manager that:

# Inherits from Employee
# Has extra attribute: team_size
# Has extra: bonus = 20% of salary
# Override get_details() to show
# bonus and team size too

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_details(self):
        print("=== Employee ===")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"monthly: {self.salary}")
        print(f"annually: {self.get_annual_salary()}")

    def get_annual_salary(self):
        return 12*self.salary

class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def get_details(self):
        print("=== Manager ===")
        super().get_details()
        print(f"Bonus: {0.20*self.salary}")
        print(f"Team size: {self.team_size}")
       
e = Employee("John", 50000, "IT")
m = Manager("Alice", 80000, "HR", 10)

e.get_details()
m.get_details()

        