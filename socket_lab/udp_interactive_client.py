import socket

host = input("Server IP Address: ").strip()
port = int(input("Server Port Number: "))
buff_size = 1024

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with udp_client:
    print("You can communicate with the server now. Enter Quit to end the communication.")
    while True:
        msg = input("Message: ")
        client_msg = bytes(msg, encoding='utf-8')

        if msg.lower().strip() == "quit":
            udp_client.sendto(client_msg, (host, port))
            print("Ending communication...\nCommunication ended.")
            break

        udp_client.sendto(client_msg, (host, port))
        print(f"Message sent to {(host, port)}")

        server_msg, server_addr = udp_client.recvfrom(buff_size)
        server_msg = server_msg.decode('utf-8')

        print(f"Message received from {(host, port)}")
        print(f"{server_addr}: {server_msg}")