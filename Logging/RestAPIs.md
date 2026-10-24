1. What is a REST API?
A REST API allows two applications to communicate over HTTP using defined endpoints and methods.

Example: A Python application requests student details from a server, and the server returns the information as JSON.
- Consume an API: Use an existing API to retrieve or send data.
- Build an API: Create your own API so other applications can access your data.
2. Important REST API concepts
Term	Meaning	Example
Endpoint	URL used to access a resource	/students/1
Method	Action performed on the resource	GET
Input	Data or parameters sent with a request	Student ID 1
Response	Data returned by the API	Student details in JSON
Status code	Indicates the result	200 OK
JSON	Common format for exchanging data	{"id": 1, "name": "Rahul"}

3. Common REST API methods
Method	Purpose	Example
GET	Retrieve data	Get student details
POST	Create a resource	Add a student
PUT	Replace a resource	Replace student details
PATCH	Update part of a resource	Change student name
DELETE	Delete a resource	Remove a student

4. Example: Sketch a GET endpoint
Suppose we build a student API.
GET
http://localhost:8000/students/1

Request input

Student ID: 1

Response — JSON


{
  "id": 1,
  "name": "Rahul",
  "course": "Python"
}
  
The endpoint uses the student ID from the URL and returns that student's details.

5. Build a simple REST API using Python
We'll use FastAPI, a Python framework for creating APIs.

# Step 1: Install FastAPI
>>python -m pip install fastapi uvicorn

# Step 2: Create main.py


from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"id": 1, "name": "Rahul", "course": "Python"},
    2: {"id": 2, "name": "Priya", "course": "Java"}
}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]

    return {"error": "Student not found"}

# Step 3: Start the API server

Your terminal is currently in the Honda Training folder. 
Run:
>>python -m uvicorn main:app --reload --app-dir Logging

You should see something similar to:
>>Uvicorn running on http://127.0.0.1:8000

# Step 3: Test your API
Open your browser and visit:

Student 1:
Returns Rahul's details
http://127.0.0.1:8000/students/1

API documentation:
Explore and test the endpoint
http://127.0.0.1:8000/docs


Keep the terminal running while testing the API.

6. Consume your own API using Python

Create another file called client.py:

import requests

url = "http://127.0.0.1:8000/students/1"

response = requests.get(url, timeout=10)

print("Status code:", response.status_code)

data = response.json()

print("Student name:", data["name"])
print("Course:", data["course"])

# Expected output:
 Status code: 200
 Student name: Rahul
 Course: Python

>> This confirms that your client successfully fetched data from your own REST API.