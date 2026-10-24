# Example 1: Fetch data from an API
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)

    print("Status code:", response.status_code)

    response.raise_for_status()

    data = response.json()

    print("Task title:", data["title"])
    print("Completed:", data["completed"])

except requests.RequestException as error:
    print("Request failed:", error)

# >>network blocked the connection because of SSL certificate verification


# Example 2: Work with JSON(offline)


import json

json_data = """
{
    "id": 1,
    "title": "Learn Python",
    "completed": false
}
"""

data = json.loads(json_data)

print("Task ID:", data["id"])
print("Task title:", data["title"])
print("Completed:", data["completed"])

# >>This demonstrates JSON parsing, but it does not send a real HTTP request.>>