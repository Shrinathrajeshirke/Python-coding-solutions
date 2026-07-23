## Problem 2
# Add two more routes to your existing Flask app:

# GET /students/<int:student_id> → returns a single student by ID, returns 404 if not found
# DELETE /students/<int:student_id> → deletes a student by ID, returns 404 if not found, 200 if deleted

## Problem 3
# Add a PUT /students/<int:student_id> route that:

# Updates an existing student's details from JSON body
# Only updates fields that are provided in the request body (partial update)
# Returns the updated student
# Returns 404 if student not found

## Problem 4
# Add a GET /students/search route that:

# Accepts a query parameter grade (e.g. /students/search?grade=A)
# Returns all students matching that grade
# Returns 400 if no query parameter provided
# Returns 404 if no students found with that grade

## Problem 5
# Add these two routes for sorting and pagination:

# GET /students/sorted?by=age → returns students sorted by given field (name, age, grade)
# GET /students/page?page=1&size=2 → returns paginated students

# Returns 400 for invalid field or missing params.

## Problem 6
# Add error handling to your Flask app:

# A route GET /students/stats that returns:
# "total" → total number of students
# "average_age" → average age rounded to 2 decimals
# "top_grade" → most common grade
# Returns 400 if no students exist

## Problem 7

# Add a route POST /students/bulk that:

# Accepts a list of students in the request body
# Validates each student has name, age, and grade fields
# Adds valid students, skips invalid ones
# Returns count of added and skipped

## problem 8

# Add a route GET /students/filter that accepts two optional query parameters:

# min_age → return students with age greater than or equal to this
# max_age → return students with age less than or equal to this
# Both can be used together or individually
# Returns 400 if neither is provided

## Problem 9
# Add a route GET /students/summary that returns:

# "total" → total students
# "grades" → dictionary with count of each grade
# "oldest" → name of oldest student
# "youngest" → name of youngest student

# Returns 400 if no students exist.

## Problem 10
# Add a route POST /students/transfer that:

# Accepts a list of student IDs in request body {"ids": [1, 2]}
# Moves those students to a separate transferred list
# Removes them from students list
# Returns transferred students and remaining students count

from flask import Flask, jsonify, request

app = Flask(__name__)

students = []
next_id = 1

@app.route("/students", methods = ["GET"])
def get_students():
    return jsonify({"students": students})

@app.route("/students", methods = ["POST"])
def add_student():
    global students, next_id
    data = request.json
    student = {"id": next_id, **data}
    students.append(student)
    next_id += 1
    return {
        "message": "Student added",
        "Student": student
    }

@app.route("/students/<int:student_id>", methods= ["GET"])
def get_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "student not found."}), 404
    else:
        return jsonify({"student": student})

@app.route("/students/<int:student_id>", methods = ["DELETE"])
def delete_student(student_id):
    global students
    for student in students:
        if student_id == student["id"]:
            students.remove(student)
            return jsonify({"message": "Student deleted", 
                    "student": student}), 200
    return jsonify({"error": "student not found."}), 404

@app.route("/students/<int:student_id>", methods = ["PUT"])
def update_records(student_id):
    global students
    update_data = request.json

    if not update_data:
        return jsonify({"error": "No update data provided."}), 400

    for student in students:
        if student["id"] == student_id:
            for key, value in update_data.items():
                if key != "id":
                    student[key] = value
            return jsonify({
                "message": "Student updated.",
                "student": student
            }), 200

    return jsonify({"error": "Student not found."}), 404

@app.route("/students/search", methods = ["GET"])
def get_query_records():
    global students
    grade = request.args.get("grade")
    if not grade:
        return jsonify({"error": "No search parameter provided"}), 400
    result = []
    for student in students:
        if grade == student['grade']:
            result.append(student)
    if result==[]:
        return jsonify({"error": "No students found"}), 404
    else:
        return jsonify({"students": result})

@app.route("/students/sorted", methods = ["GET"])
def sort_records():
    global students
    valid_fields = ["name", "age", "grade"]
    by = request.args.get("by")
    if not by or by not in valid_fields:
        return jsonify({"error": "Invalid or missing sort field"}), 400
    result = sorted(students, key=lambda x: x[by])
    return jsonify({"students": result}), 200

@app.route("/students/page", methods = ["GET"])
def get_records_by_page():
    page = request.args.get("page")
    size = request.args.get("size")
    if not page or not size:
        return jsonify({"error": "No search parameter provided"}), 400
    page = int(page)
    size = int(size)
    start = (page - 1) * size
    end = start + size
    result = students[start:end]
    return jsonify({
        "page": page,
        "size": size,
        "total": len(students),
        "students": result
    }), 200

@app.route("/students/stats", methods = ["GET"])
def get_stats():
    global students
    total_stud = len(students)
    if total_stud == 0:
        return jsonify({"error": "No students found"}), 400
    total_age = sum(student['age'] for student in students)
    avg_age =  total_age/total_stud
    top_grade = max(set(s["grade"] for s in students), key=lambda g: sum(1 for s in students if s["grade"] == g))
    return jsonify({
        "total": total_stud,
        "average_age": round(avg_age,2),
        "top_grade": top_grade
    }), 200


@app.route("/students/bulk", methods = ["POST"])
def validate_students():
    global students, next_id
    data = request.json
    added = 0
    skipped = 0
    new_students = []
    required_fields = {"name", "age", "grade"}
    
    for item in data: 
        if required_fields.issubset(item.keys()):
            student = {"id": next_id, **item}
            students.append(student)
            new_students.append(student)
            next_id += 1
            added += 1
        else:
            skipped += 1
    
    return jsonify({"added": added, "skipped": skipped, "students": new_students}), 201

@app.route("/students/filter", methods = ["GET"])
def filter_students():
    min_age = request.args.get("min_age")
    max_age = request.args.get("max_age")
    if not min_age and not max_age:
        return jsonify({"error": "None of the parameter provided."}), 400
    min_age = int(min_age) if min_age else 0
    max_age = int(max_age) if max_age else float("inf")
    result = []
    global students
    for student in students:
        if min_age <= student['age'] <= max_age:
            result.append(student)
    return jsonify(
        {"students": result}
    )

@app.route("/students/summary", methods = ["GET"])
def summary():
    global students
    total_stud = len(students)
    if total_stud == 0:
        return jsonify({"error": "No students found"}), 400
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
    return jsonify({
        "total": total_stud,
        "grades": grade_count,
        "oldest": oldest,
        "youngest": youngest
        }), 200

@app.route("/students/transfer", methods = ["POST"])
def transfer_students():
    data = request.json
    ids = data['ids']
    transferred = []
    remaining = []
    for student in students:
        if student["id"] in ids:
            transferred.append(student)
        else:
            remaining.append(student)
    students = remaining
    return jsonify({
        "transferred": transferred,
        "remaining": remaining
    }), 200

if __name__ == "__main__":
    app.run(debug=True)