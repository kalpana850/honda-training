import requests

url = "http://127.0.0.1:8000/students/1"

response = requests.get(url, timeout=10)

print("Status code:", response.status_code)

data = response.json()

print("Student name:", data["name"])
print("Course:", data["course"])

# Expected output:
#  Status code: 200
#  Student name: Rahul
#  Course: Python

# >> This confirms that your client successfully fetched data from your own REST API.