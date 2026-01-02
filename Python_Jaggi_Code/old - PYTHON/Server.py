import socket
import threading

def handle_send(client_socket):
    """Thread to send messages to client"""
    while True:
        msg = input()
        try:
            client_socket.send(msg.encode())
        except:
            break
        if msg.lower() == "off":
            print("Server is shutting down...")
            client_socket.close()
            break

def handle_receive(client_socket):
    """Thread to receive messages from client"""
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            if msg.lower() == "off":
                print("Client has logged out.")
                break
            print(f"\t\t\t\t{msg}")
        except ConnectionResetError:
            break

def main():
    host = 'localhost'  # Change to remote IP if needed
    port = 122

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on {host}:{port}, waiting for client...")
    client_socket, addr = server_socket.accept()
    print(f"Connected to client: {addr}")

    # Start sending and receiving threads
    threading.Thread(target=handle_send, args=(client_socket,)).start()
    threading.Thread(target=handle_receive, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
