import socket
import json

print("Set up the address of the server.\n")
host = input("Host: ")
port = int(input("Port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Listenning on {(host, port)}\nWaiting for connection...\n")
    conn, addr = s.accept()
    with conn:
        name = conn.recv(1024)
        print(f"{addr} connected as {name.decode(encoding='utf-8')}\n")
        while True:
            data = conn.recv(1024)
            data = data.decode(encoding='utf-8')
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print(f"{addr} disconnected!")
                break
            print(f"{data['sender']}: {data['msg']}")
            msg = input("\nEnter message: ")
            if msg =='':
                msg = "empty_response"
            msg = json.dumps({"sender":"Server", "msg":msg})
            conn.sendall(bytes(msg, encoding='utf-8'))