### Day 17: API Development 

#### What is an API?
* Application Programming Interface — lets two applications talk to each other
* REST API uses HTTP methods to perform operations
* Python's most popular frameworks: Flask (simple) and FastAPI (modern, fast)

#### HTTP Methods

| Method | Purpose |
| --- | --- |
| GET |	Retrieve data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Delete data |

#### Flask Basics
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": []})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"id": user_id})

if __name__ == "__main__":
    app.run(debug=True)  # runs on http://127.0.0.1:5000
```

#### Request & Response
```python
# Getting data from request
data = request.json          # JSON body
args = request.args.get("q") # Query params ?q=hello
headers = request.headers    # Request headers

# Sending responses
return jsonify({"key": "value"}), 200  # 200 OK
return jsonify({"error": "Not found"}), 404
return jsonify({"error": "Bad request"}), 400
```

#### Status Codes
| Code | Meaning |
| --- | --- |
| 200 |	OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

#### FastAPI Basics
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/users")
def get_users():
    return {"users": []}

@app.post("/users")
def create_user(user: User):
    return {"message": "Created", "user": user}
# Run with: uvicorn filename:app --reload
```

#### Key Differences
| Feature |	Flask | FastAPI |
| --- | --- | --- |
| Speed	 | Moderate | Very Fast |
| Type hints | Manual |	Built-in |
| Docs	| Manual | Auto (Swagger) |
| Learning curve | Easy | Moderate |