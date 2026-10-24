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
