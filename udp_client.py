import socket

host = input("Server IP Address: ").strip()
port = int(input("Server Port Number: "))
buff_size = 1024

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_msg = bytes("Hello UDP Server", encoding='utf-8')
udp_client.sendto(client_msg, (host, port))
print(f"Message sent to {(host, port)}")

server_msg, server_addr = udp_client.recvfrom(buff_size)

print(f"Message received from {(host, port)}")
print(f"{server_addr}: server_msg")