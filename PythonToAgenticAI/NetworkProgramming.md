# 1. What is Network Programming?
Network programming is the process of creating programs that communicate with each other over a network, such as the internet or a local network.

Example: A web browser communicating with a website's server.

# 2. Client and Server
- Client: The device or program that requests a service or data.
- Server: The device or program that receives the request and sends a response.
Example: When you open YouTube, your browser is the client, and YouTube's server sends back the requested webpage or video data.

# 3. What is a Socket?
A socket is an endpoint for communication between two programs over a network. It allows a client and a server to send and receive data.

Think of a socket like a telephone connection: one side connects, and both sides can communicate.

A socket is commonly identified by an IP address and a port number.
- IP address: Identifies a device on a network.
- Port number: Identifies a particular service or application on that device.
Example: 192.168.1.10:5000

Here, 192.168.1.10 is the IP address and 5000 is the port number.

# 4. Client–Server Flow

               CLIENT
           (Requests data)
                 |
                 V
        Connection established       
(Client socket connects to server socket)
                 |
                 V
               Server
    (Receives request and processes it)
                | ^
                V |        
     Response sent back to the client

Example flow:
1. The client connects to the server.
2. The client sends a request: "Hello, Server!"
3. The server processes the request.
4. The server sends a response: "Hello, Client!"
5. The connection closes when communication is complete.

# 5. TCP vs UDP

TCP	UDP
Reliable data delivery	Delivery is not guaranteed
Establishes a connection	Does not establish a connection first
Used by web browsing and file transfers	Used in gaming, live streaming and real-time communication

# 6. Simple Python Socket Example
Python provides the built-in socket module for network programming.

import socket

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created successfully")
s.close()

Explanation:
- socket.AF_INET: Uses IPv4 addresses.
- socket.SOCK_STREAM: Uses TCP.
- s.close(): Closes the socket and releases resources.
This example creates a socket but does not connect to a server.

# 7. Practice Activity

Client → Connection → Request → Server → Response → Client
For example : a client requests the current time, and the server returns 10:30 AM.