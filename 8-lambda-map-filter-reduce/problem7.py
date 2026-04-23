# Using sorted() with lambda:

# Take a list of employees
# Sort by multiple criteria:

# First by department
# Then by salary (descending)


# Print sorted results

employees = [
    ("Alice", "IT",      75000),
    ("Bob",   "HR",      50000),
    ("Charlie","IT",     90000),
    ("David", "HR",      55000),
    ("Eve",   "Finance", 70000),
    ("Frank", "IT",      80000)
]

def sort_employee(emp):
    emp_sort_by_dept_salary = sorted(emp, key = lambda x: (x[1], -x[2]))

    for name, dept, salary in emp_sort_by_dept_salary:
        print(f"{dept:8} | {name:8} -> {salary}")

sort_employee(employees)