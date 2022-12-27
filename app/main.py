import socket


def main():
    socket.socket()
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen(3)  # listen for clients
    client, _ = server_socket.accept()  # wait for client
    while True:
        data = client.recv(1024).decode()  # receive data from client
        if not data:
            break
        client.send(b"+PONG\r\n")

    client.close()  # close the socket


if __name__ == "__main__":
    main()
