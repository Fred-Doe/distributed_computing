from pydoc import cli
import socket

HOST = "127.0.0.1"
PORT = 5080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect((HOST, PORT))
    client_sock.sendall(b"Delta Delta Zeta Zeta Fred")
    data = client_sock.recv(1024)

print(f"Received: {data!r}")