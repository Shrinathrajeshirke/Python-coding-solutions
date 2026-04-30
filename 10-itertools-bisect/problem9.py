# Implement a grade calculator
# Use bisect to find grade boundaries
# Handle multiple students

breakpoints = [40, 50, 60, 70, 80, 90]
grades = ['F', 'E', 'D', 'C', 'B', 'A', 'A+']

students = [
    ("Alice", 85),
    ("Bob", 55),
    ("Charlie", 92),
    ("David", 38),
    ("Eve", 78)
]

import bisect
from collections import Counter

def get_grade(marks):
    index = bisect.bisect(breakpoints, marks)
    return grades[index]

print("Output")
print("Grade Report: ")
for name, marks in students:
    grade = get_grade(marks)
    print(f"{name:8}: {marks} -> {grade}")

print("Grade distribution")
all_grades = [get_grade(marks) for name, marks in students]
grade_count = Counter(all_grades)
grade_count = dict(sorted(grade_count.items(), reverse=True))
for grade, count in grade_count.items():
    print(f"{grade}: {count} students")