#!/usr/bin/env python3
# coding: utf-8

import socket


def _main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10000)
    sock.bind(server_address)
    sock.listen(128)

    while True:
        connection, (client_address, client_port) = sock.accept()

        try:
            print('Client: {0}:{1}'.format(client_address, client_port))

            while True:
                data = connection.recv(1024)
                if len(data) == 0:
                    break
                print('Recv: {}'.format(data))
                if data:
                    connection.sendall(data)
                    print('Send: {}'.format(data))
                else:
                    break
        finally:
            connection.close()


if __name__ == '__main__':
    _main()
