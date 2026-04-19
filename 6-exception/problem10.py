# Write a program that:

# Appends new students to existing file
# Reads entire file
# Counts total students
# Finds highest scorer

students = [
    ("Jay", 95),
    ("Raj",78)
]

def append_students(stud):
    with open("student.txt", 'a') as f:
        for student in students:
            name, marks = student
            f.write(f"{name}, {marks}\n")
    print("Data appended successfully")

def read_students():
    try:
        with open("student.txt","r") as f:
            print("Output:")
            print("=== All Students ===")
            count = 0
            highest_mark = 0
            highest_scorer = ""
            for line in f:
                count += 1
                name, marks = line.strip().split(",")
                if int(marks) > highest_mark:
                    highest_mark = int(marks)
                    highest_scorer = name
                print(f"{name:6} -> {marks}")
                
            print(f"Total students: {count}")
            print(f"Highest scorer -> {highest_scorer} -> {highest_mark}")
    except FileNotFoundError:
        print("File doesnot exists")
    print("Data reading completed")
    
append_students(students)

read_students()