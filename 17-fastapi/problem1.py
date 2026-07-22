# Create a Flask app with a simple REST API for managing a in-memory list of students (no database needed).

# Write the following:

# A students list to store data (starts empty)
# GET /students → returns all students
# POST /students → adds a new student from JSON body {"name": "Ali", "age": 20, "grade": "A"}
# Returns proper status codes

from flask import Flask, request, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)


