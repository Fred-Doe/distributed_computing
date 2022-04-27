import threading
import socket

buff_size = 1024

def server():
    host = input("Server IP: ")
    port = int(input("Server Port: "))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print(f"Server bound to {(host, port)}")
    return server

def start_server():
    clients = []
    server_sock = server()
    server_sock.listen(10)
    print("Server listening for connections...")
    with server_sock:
        while True:
            thread, conn, addr = thread_handler(server_sock)
            clients.append((thread, conn, addr))
            thread.start()
                    

def handle_client(conn, addr):
    with conn:
        while True:
            msg = conn.recv(buff_size)
            if not msg:
                note = "Disconnected"
                # send_to_all(addr, note)
                break
            # send_to_all(addr, msg)
            msg = msg.decode(encoding='utf-8')
            print(f"{addr}: {msg}")

def thread_handler(server):
    conn, addr = server.accept()
    thread = threading.Thread(handle_client, (conn, addr))
    thread.start()
    # return (thread, conn, addr)

def send_to_all(address, msg, socks):
    if msg == 'Disconnected':
        note = (f"{address} Disconnected")
        for sock in socks:
            sock.sendall(note)

def wait_for_client(server):
    try:
        while server:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn,addr))
            thread.start()
            return (thread, conn, addr)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        server.close()


if __name__ == '__main__':
    start_server()
