# Combine map(), filter(), reduce():

# Take a list of students with marks
# Filter students who passed (marks >= 40)
# Map their marks to grades
# Use reduce to find total marks of passed students

from functools import reduce

def marks_evaluation(stud_marks):
    passed = list(filter(lambda x: x[1]>=40,stud_marks))

    total_marks = reduce(lambda x,y: x+y[1], passed, 0)

    stud_grades = list(map(lambda x: (x[0], "A" if x[1]>=90
                                      else "B" if x[1] >= 80
                                      else "C" if x[1] >= 70
                                      else "D"), passed))
    
    return passed, total_marks, stud_grades



students = [
    ("Ram", 85),
    ("Sam", 35),
    ("Tom", 67),
    ("Jay", 28),
    ("Raj", 92)
]

passed_stud, total_marks, grades = marks_evaluation(students)

print(f"Passed students: {passed_stud}")
print(f"With grades: {grades}")
print(f"Total marks: {total_marks}")