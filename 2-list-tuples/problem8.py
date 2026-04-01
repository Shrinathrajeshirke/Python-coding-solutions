# Write a program using Tuple Unpacking:

# Create a list of tuples with student name and marks
# Unpack each tuple
# Print formatted report
# Find topper

def tuple_unpacking():
    students = [
        ("Ram", 85),
        ("Sam", 92),
        ("Tom", 67),
        ("Jay", 78),
        ("Raj", 95)
    ]

    print("Student report: ")
    for name, score in students:
        print(f"{name} scored {score} marks")

    topper = ""
    topper_score = 0

    for name, score in students:
        if score > topper_score:
            topper_score = score
            topper = name
    
    print(f"Topper: {topper} with {topper_score} marks")

tuple_unpacking()