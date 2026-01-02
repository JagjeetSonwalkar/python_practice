import socket
import threading

def handle_send(client_socket):
    """Thread to send messages to server"""
    while True:
        msg = input()
        try:
            client_socket.send(msg.encode())
        except:
            break
        if msg.lower() == "off":
            print("Client logout !!")
            client_socket.close()
            break

def handle_receive(client_socket):
    """Thread to receive messages from server"""
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            if msg.lower() == "off":
                print("Server logout")
                break
            print(f"\t\t\t\t{msg}")
        except ConnectionResetError:
            break

def main():
    host = 'localhost'  # Change to server IP if needed
    port = 122

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Client connected to server at {host}:{port}")

    # Start sending and receiving threads
    threading.Thread(target=handle_send, args=(client_socket,)).start()
    threading.Thread(target=handle_receive, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
