import socket
import json
print("Enter the address of the server you want to connect to.\n")
host = input("Server IP: ")
port = int(input("Server Port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((host, port))
    print("\nEnter 'quit' in the message prompt to close the connection\n")
    while True:
        msg = input("\nEnter message: ")
        if msg == '':
            print("Closing connection...")
            break
        elif msg.strip().lower() == "quit":
            print("Closing connection...")
            break
        enc_msg = bytes(msg, 'utf-8') # Convert string to byte
        c.sendall(enc_msg) 
        data = c.recv(1024)
        msg = data.decode(encoding='utf-8')
        print(f"{msg}")