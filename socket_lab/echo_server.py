import socket

HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT = 5080   # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen()
    print(f"Listening at {HOST} on {PORT}")
    conn, addr = server_sock.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
            conn.sendall(data)

"""
The values passed to .bind() depend on the address family of the socket. In this example, 
you’re using socket.AF_INET (IPv4). So it expects a two-tuple: (host, port).

HOST can be a hostname, IP address, or empty string. If an IP address is used, host should
be an IPv4-formatted address string. The IP address 127.0.0.1 is the standard IPv4 address 
for the loopback interface, so only processes on the host will be able to connect to the server. 
If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

PORT represents the TCP port number to accept connections on from clients. It should be an 
integer from 1 to 65535, as 0 is reserved. Some systems may require superuser privileges if 
the port number is less than 1024.
"""