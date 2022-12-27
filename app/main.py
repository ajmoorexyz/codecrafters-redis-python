import socket
import threading


def handle_connection(client_connection):
    while True:
        try:
            client_connection.recv(1024)  # receive data from client
            client_connection.send(b"+PONG\r\n")
        except ConnectionError:
            break


def main():
    socket.socket()
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client_connection, _ = server_socket.accept()  # wait for client
        threading.Thread(target=handle_connection, args=(client_connection,)).start()


if __name__ == "__main__":
    main()
