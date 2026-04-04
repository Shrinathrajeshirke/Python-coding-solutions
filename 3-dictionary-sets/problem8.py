# Write a program that:
# Creates a dictionary of employees
# with their department and salary
# Groups employees by department
# Finds highest paid in each department
# Finds average salary per department

def dept_info():
    employees = [
    ("Alice", "IT", 75000),
    ("Bob", "HR", 50000),
    ("Charlie", "IT", 90000),
    ("David", "HR", 55000),
    ("Eve", "IT", 80000),
    ("Frank", "Finance", 70000)
    ]

    departments = {}
    for name, dept, salary in employees:
        if dept not in departments:
            departments[dept] = []
        departments[dept].append((name, salary))
    
    for dept, values in departments.items():
        print(f"{dept} Department:")
        total = 0
        max_salary = 0
        max_name = ""
        employees = []
        length = len(departments[dept])

        for name, salary in values:
            total += salary
            employees.append(name)
            if salary > max_salary:
                max_salary = salary
                max_name = name

        # for i in range(length):
        #     total += departments[dept][i][1]
        #     employees.append(departments[dept][i][0])
        #     if departments[dept][i][1] > max_salary:
        #         max_salary = departments[dept][i][1]
        #         max_name = departments[dept][i][0]
        print(f"Employees: {", ".join(employees)}")
        avg = total/length
        print(f"Highest Paid: {max_name} -> {max_salary}")
        print(f"Average Salary: {round(avg, 2)}")

dept_info()
