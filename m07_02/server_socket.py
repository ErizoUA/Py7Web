import socket


def main():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    while True:
        message_from_client = conn.recv(1024).decode()
        if not message_from_client:
            print(message_from_client, 'break')
            break
        print(f'Отримано сповіщення: {message_from_client}')
        message = input('>> ')
        conn.send(message.encode())
    conn.close()


if __name__ == '__main__':
    main()
