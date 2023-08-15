import socket
import threading
from encryption import crypt_message, decrypt_message


def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            break

def start_client():
    key = "100.70b10111001"
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive_message, args=(client, ))
    receive_thread.start()

    while True:
        message = input()
        encrypt_message = crypt_message(message, key)
        client.send(encrypt_message.encode('utf-8'))
        if message.lower() == "quit":
            break

if __name__ == "__main__":
    start_client()