students = [
    {"name": "Ali", "age": 20, "grade": "A"},
    {"name": "Sara", "age": 22, "grade": "B"},
]

def summary():
    global students
    total_stud = len(students)
    # if total_stud == 0:
    #     return jsonify({"error": "No students found"}), 400
    grade_count = {}
    for student in students:
        if student['grade'] not in grade_count.keys():
            grade_count[student['grade']] = 1
        else:
            grade_count[student['grade']] += 1

    max_age = max(student['age'] for student in students)
    min_age = min(student['age'] for student in students)
    oldest = ""
    youngest = ""
    for student in students:
        if student['age'] == max_age:
            oldest = student['name'] 

    for student in students:
        if student['age'] == min_age:
            youngest = student['name']


    return {
        "total": total_stud,
        "grades": grade_count,
        "oldest": oldest,
        "youngest": youngest
    }

print(summary())