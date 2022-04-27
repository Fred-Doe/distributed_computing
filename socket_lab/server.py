import  socket

host = "127.0.0.1"
port = 5088

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()
print(f"Listening on {(host,port)}")
conn, addr = server_socket.accept()

with conn:
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"Client with address {addr} is disconnecting")
            break
        print("Data received")
        conn.sendall(data)
server_socket.close()