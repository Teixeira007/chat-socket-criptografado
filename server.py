import socket
import threading
from encryption import crypt_message, decrypt_message


def handle_client(client_socket, clients):
    while True:
        try:
            encrypet_message = client_socket.recv(1024).decode('utf-8')
            if not encrypet_message:
                break

            decrypted_message = decrypt_message(encrypet_message, key)
            if decrypted_message == "quit":
                break

            for client in clients:
                if client != client_socket:
                    client.send(decrypted_message.encode('utf-8'))
        except:
            break
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    print(f"[*] Server listening on {host}:{port}")

    clients = []
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"[*] Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_handler.start()

if __name__ == "__main__":
    key = "100.70b10111001"
    start_server()
