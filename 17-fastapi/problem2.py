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
    by = request.args.get("by")
    if not by:
        return jsonify({"error": "No search parameter provided"}), 400
    result = sorted(students, key = lambda x: x[by])
    return jsonify({"students": result}), 200

@app.route("/students/page", methods = ["GET"])
def get_records_by_page():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    if not page or not size:
        return jsonify({"error": "No search parameter provided"}), 400
    start = (page - 1) * size
    end = start + size
    result = students[start:end]
    return jsonify({"students": result}), 200

if __name__ == "__main__":
    app.run(debug=True)