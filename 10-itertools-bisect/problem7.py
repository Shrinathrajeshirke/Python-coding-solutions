# Take a list of students with grades
# Group students by grade
# Show count per grade
# # Important: Sort first!

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eve", "B"),
    ("Frank", "A"),
    ("Grace", "C")
]

import itertools

def group_by_grades(students):
    sorted_stud = sorted(students, key=lambda x: x[1])
    grade_group = itertools.groupby(sorted_stud, key= lambda x: x[1])
    for key, group in grade_group:
        group_list= list(group)
        print(f"\nGrade {key} ({len(group_list)} students):")
        for student, _ in group_list:
            print(f"- {student}")

group_by_grades(students)
