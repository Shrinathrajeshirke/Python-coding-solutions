# Write a function using *args and **kwargs together:

# Function called student_report
# *args → takes subject marks
# **kwargs → takes student details
# Prints complete report

def student_report(*args, **kwargs):
    print("=== Student Report ===")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    marks = list(args)
    print(f"Marks: {marks}")

    total_marks = sum(marks)
    n = len(marks)
    average = total_marks/n
    result = "Pass" if average >= 40 else "Fail"
    print(f"Total Marks: {total_marks}")
    print(f"Average: {average}")
    print(f"Result: {result}")
    print("==================================")
    
student_report(85, 92, 78, 95, 88,
    name="Shrinath",
    class_="10th",
    school="ABC School")