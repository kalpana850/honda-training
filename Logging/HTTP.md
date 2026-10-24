# HTTP Requests with Python

1. What is HTTP?
HTTP (Hypertext Transfer Protocol) is a protocol that allows a client, such as Python, to communicate with a server.

Example: A Python program requests weather information from a weather API, and the server sends back the data.

2. How does an HTTP request work?
      
      Client (Python program)
                |
                v
         ( Server / API )
                |
                v
      GET request — asks for data
      
      Response — status code + data

    ( Python receives the response )

3. Important concepts
Term	                     Meaning
Request	          Message sent from the client to the server
Response	      Reply returned by the server
GET	              HTTP method used to retrieve data
Status code	      Number indicating the result of the request
JSON	          A common format for exchanging structured data between systems
API	              An interface that allows applications to communicate

4. Important HTTP methods

Method	        Purpose	                                 Example
GET	          Retrieve data	                       Fetch user details
POST	   Send data to create a resource	       Create a new user
PUT	     Replace an existing resource	         Update all user details
PATCH	  Update part of a resource	               Change a user's email
DELETE	     Delete a resource	                       Delete a user

For this day's practice, focus mainly on GET requests.

5. Common HTTP status codes

Code	                     Meaning
200	OK          —    request successful
400	Bad Request —    invalid request
401	Unauthorized —   authentication required or invalid
403	Forbidden —      access denied
201	Created —        resource created successfully
404	Not Found —      resource not found
500	Internal Server Error — server-side problem

Remember: 2xx generally means success, 4xx indicates a client-side request problem, and 5xx indicates a server-side problem.

6. What is an API?
An API (Application Programming Interface) allows two software applications to communicate.

For example, a weather application can use a weather API to retrieve temperature and forecast information.

An API endpoint is a specific URL through which you access a resource.

Example:
https://jsonplaceholder.typicode.com/todos/1


This sample endpoint returns information about a task.

7. What is JSON?
JSON (JavaScript Object Notation) is a format used to exchange structured data between applications.

Example JSON response:

{
    "id": 1,
    "title": "Learn Python",
    "completed": false
}

Here:
- id is a key, and 1 is its value.
- title is a key, and "Learn Python" is its value.
- completed is a Boolean value: false.
Python can convert JSON into a dictionary using response.json().

8. Python requests library
The requests library makes it easy to send HTTP requests from Python.
