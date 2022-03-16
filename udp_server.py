import socket

host = input("Host IP Address: ").strip()
port = int(input("Host Port Number: "))
buffer_size = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((host, port))
print(f"Listening on {(host, port)}")

while True:
    client_msg, client_addr = udp_server.recvfrom(1024)
    print(f"Client {client_addr} sent a message")
    print(f"{client_addr}: client_msg")

    server_msg = bytes("Hello from the server", encoding='utf-8')
    udp_server.sendto(server_msg, client_addr)