import socket

host = "127.0.0.1"
port = 5088

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

with client:
    print(f"You are connected to the server on this {(host, port)}")
    client.sendall(b"Hello Server")
    data = client.recv(1024)
print(f"Received: {data!r}")
