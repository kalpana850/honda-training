# Sockets + Security Scripting

# 1. Advanced Socket Programming
Socket programming allows two programs to communicate over a network. Advanced concepts help make communication more reliable, efficient, and secure.

Concept	                     Meaning

TCP socket	             Reliable, ordered data delivery
UDP socket	             Fast communication without guaranteed delivery
Timeout	                 Limits how long a program waits for a response
bind()	                 Assigns a local address and port to a server socket
listen()	             Makes a TCP socket ready to accept connections
accept()	             Accepts an incoming client connection
sendall()	             Sends all provided data or raises an error
recv()	                 Receives data from a socket

Example: TCP socket with timeout

<!-- import socket

try:
    with socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    ) as client:
        client.settimeout(5)

        client.connect(("example.com", 80))
        print("Connected successfully")

except socket.timeout:
    print("Connection timed out")

except OSError as error:
    print(f"Network error: {error}") -->

Explanation:
- Creates a TCP socket.
- Sets a 5-second timeout to avoid waiting indefinitely.
- Connects to the specified server on port 80.
- Handles timeout and network errors safely.
Note: Port 80 is used for HTTP. This example establishes a connection but does not send an HTTP request.

# 2. Security Programming with Python
Security scripting means writing Python scripts that automate tasks while protecting data, systems, and users.

Examples include checking log files, validating input, monitoring network connections, and detecting suspicious activity.
Three essential security hygiene practices

1. Validate user input

Never blindly trust data received from users or networks. Check its type, length, and allowed values.

Example:
<!-- port = input("Enter port: ")

if port.isdigit() and 1 <= int(port) <= 65535:
    print("Valid port")
else:
    print("Invalid port") -->

2. Protect secrets

Never hardcode passwords, API keys, or access tokens in source code or upload them to GitHub.

Example:
<!-- import os

api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("API_KEY is missing") -->

Store secrets in environment variables or an approved secrets manager.

3. Handle errors and logging safely

Handle expected errors, record useful diagnostic information, and avoid exposing passwords or sensitive data in logs.

Example:
<!-- import logging

logging.basicConfig(level=logging.INFO)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Calculation failed") -->

Avoid logging credentials, tokens, or unnecessary personal information.



# 3. More Safe Scripting Practices
- Use least privilege: Run scripts with only the permissions they need.
- Use encryption: Use TLS for sensitive network communication instead of sending data in plaintext.
- Set timeouts: Prevent network operations from hanging indefinitely.
- Limit resources: Restrict input sizes and connection counts to reduce resource-exhaustion risks.
- Keep dependencies updated: Use trusted packages and patch known vulnerabilities.
- Test safely: Test on localhost or systems you are authorized to access.

# 4. Socket Security Review Example
Consider this simplified server code:
<!-- data = client.recv(1024)
print(data.decode()) -->

Potential improvements:
1. Handle decoding errors: Incoming bytes may not be valid UTF-8.
2. Validate input: Never assume received data is safe or correctly formatted.
3. Handle connection errors: A client may disconnect unexpectedly.
4. Avoid sensitive logging: Received data might contain credentials or private information.

A safer decoding approach is:

<!-- try:
    message = data.decode("utf-8", errors="strict")
except UnicodeDecodeError:
    print("Invalid message format") -->

The server should also validate the decoded message before processing it.