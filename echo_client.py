#!/usr/bin/env python3
# coding: utf-8

import socket


def _main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10000)
    sock.connect(server_address)

    try:
        message = input()
        sock.sendall(message.encode('utf-8'))

        received = 0
        expected = len(message)

        while received < expected:
            data = sock.recv(1024)
            received += len(data)
            print('{}'.format(data.decode('utf-8')))
    finally:
        sock.close()


if __name__ == '__main__':
    _main()
