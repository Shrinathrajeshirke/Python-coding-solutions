# > **Write a program that:**
# > - Creates a dictionary of 5 students with their marks
# > - Assigns grades based on marks:
# ```
# 90-100  → Grade A
# 80-89   → Grade B
# 70-79   → Grade C
# 60-69   → Grade D
# below 60 → Grade F
# ```

# > - Prints each student with marks and grade
# > - Prints how many students got each grade

def get_grade(mark):
    if mark>=90:
        grade = "A"
    elif 80 <= mark < 90:
        grade = "B"
    elif 70 <= mark < 80:
        grade = "C"
    elif 60 <= mark < 70:
        grade = "D"
    else:
        grade = "F"
    return grade

students = {
    "Ram": 85,
    "Sam": 92,
    "Tom": 67,
    "Jay": 78,
    "Raj": 55
}

grade_count = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "F":0
}

for k,v in students.items():
    g = get_grade(v)
    print(f"{k} -> {v} -> Grade {g}")
    grade_count[g] += 1

for grade, count in grade_count.items():
    print(f"Grade {grade} -> {count}")
