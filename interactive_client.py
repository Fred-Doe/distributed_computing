import socket
import json
print("Enter the address of the server you want to connect to.\n")
host = input("Host: ")
port = int(input("Port: "))
name = input("Your name: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((host, port))
    print(f"You are connected as {name}")
    c.sendall(bytes(name, encoding="utf-8"))
    print("\nEnter 'quit' in the message prompt to close the connection\n")
    while True:
        msg = input("\nEnter message: ")
        if msg == '':
            print("Closing connection...")
            break
        elif msg.strip().lower() == "quit":
            print("Closing connection...")
            break
        msg = json.dumps({"sender":name, "msg":msg})
        enc_msg = bytes(msg, 'utf-8') # Convert string to byte
        c.sendall(enc_msg) 
        data = c.recv(1024)
        data = data.decode(encoding='utf-8')
        data = json.loads(data)
        if data['msg'] == "empty_response":
            continue
        print(f"{data['sender']}: {data['msg']}")