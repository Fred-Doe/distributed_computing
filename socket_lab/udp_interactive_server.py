import socket

host = input("Host IP Address: ").strip()
port = int(input("Host Port Number: "))
buffer_size = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((host, port))
print(f"Server bound to {(host, port)}")

with udp_server:
    while True:
        client_msg, client_addr = udp_server.recvfrom(buffer_size)
        client_msg = client_msg.decode('utf-8')
        if client_msg.lower().strip() == 'quit':
            print(f"Client {client_addr} stopped communicating")
            break
        print(f"Client {client_addr} sent a message")
        print(f"{client_addr}: {client_msg}")

        server_msg = bytes(input("Message: "), encoding='utf-8')
        udp_server.sendto(server_msg, client_addr)
