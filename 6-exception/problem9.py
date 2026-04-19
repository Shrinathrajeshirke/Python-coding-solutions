# Write a program that:

# Writes student data to a file
# Reads it back
# Displays it nicely

students = [
    ("Ram", 85),
    ("Sam", 92),
    ("Tom", 67)
]
def write_students(ls):
    with open("student.txt", "w") as f:
        for student in students:
            name, marks = student
            f.write(f"{name}, {marks}\n")
    print("Data written successflly")


def read_students():
    try:
        with open("student.txt", "r") as f:
            print("Output: ")
            print("==== Student Records ====")
            for line in f:
                name, marks = line.strip().split(",")
                print(f"{name:6} -> {marks.strip()}")
    except FileNotFoundError:
        print("File not found!")

write_students(students)
read_students()

