import socket


def main():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input('>> ').lower().strip()
    if len(message) > 0:
        while message != 'exit':
            client_socket.send(message.encode())
            message_from_server = client_socket.recv(256).decode()
            print(f'Отримано сповіщення: {message_from_server}')
            message = input('>> ').lower().strip()
            if len(message) == 0:
                break

    client_socket.close()


if __name__ == '__main__':
    main()
