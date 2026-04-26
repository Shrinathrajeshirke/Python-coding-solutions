# Using namedtuple:

# Create a Student record system
# Each student has: name, roll, marks, grade
# Operations:

# Add students
# Find top 3 students
# Find students by grade
# Calculate average mark

from collections import namedtuple

Student = namedtuple('Student', ['name', 'roll', 'marks', 'grade'])

students = [
    Student("Ram", 101, 85, "B"),
    Student("Sam", 102, 92, "A"),
    Student("Tom", 103, 67, "C"),
    Student("Jay", 104, 95, "A"),
    Student("Raj", 105, 78, "B")
]

def stud_marks(students):
    sorted_students = sorted(students, key=lambda x: -x.marks)

    print("Output: ")
    print("Top 3 students: ")
    for student in sorted_students[:3]:
        print(f"{student.name} - {student.marks}")
    print("")
    print("Grade A students: ")
    for student in students:
        if student.grade == 'A':
            print(f"{student.name} - {student.marks}")
    
    total = 0
    for student in students:
        total += student.marks
    
    avg_marks = round(total/len(students),2)
    print("")
    print(f"Average marks: {avg_marks}")

stud_marks(students)
    



