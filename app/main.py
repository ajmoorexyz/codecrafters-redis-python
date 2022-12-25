import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client, addr = server_socket.accept()  # wait for client
    client.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
